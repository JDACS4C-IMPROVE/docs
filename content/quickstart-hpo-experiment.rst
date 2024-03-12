Hyper Parameter Optimization (HPO)
==================================

Requirements
____________

Your model must be CANDLE compliant, containerized, and packaged in a singularity image. You can identify the image file by the **\*.sif** suffix. Default definition files can be found in the `IMPROVE Singularity repository <https://github.com/JDACS4C-IMPROVE/Singularity>`_. The container should expose the following interface scripts:

+ preprocess.sh
+ train.sh
+ infer.sh


Steps 
_____

1. Install prerequisites
2. Preprocess data
3. :ref:`Create config files <Config Overview>` for experiment. 
4. :ref:`Run <Run>` HPO with supervisor::
        supervisor ${location} ${workflow} ${config}
4. :ref:`Analysis <Analysis>`


.. _Config Overview:

Create config files
___________________

A directory with copy-and-customize config files can be found at <https://github.com/ECP-CANDLE/Tests/tree/main/sv-tool/deap-generic>, along with a README about the settings used. Create with the following steps:

1. ``mkdir Experiment && cd Experiment``

2. Create config file *cfg-1.sh*:

   .. code-block:: bash

    source_cfg -v cfg-my-settings.sh
    
    export CANDLE_MODEL_TYPE="SINGULARITY"
    export MODEL_NAME=${/PATH/TO/SINGULARITY/IMAGE/FILE.sif}
    export PARAM_SET_FILE=${/PATH/TO/GA/PARAMETER/FILE.json} #e.g hyperparams.json

3. Create config file *cfg-my-settings.sh*:

   .. code-block:: bash

    echo SETTINGS
    
    # General Settings
    export PROCS=4
    export PPN=4
    export WALLTIME=01:00:00
    export NUM_ITERATIONS=3
    export POPULATION_SIZE=2
    
    # GA Settings (optional)
    export GA_STRATEGY='mu_plus_lambda'
    export OFFSPRING_PROPORTION=0.5
    export MUT_PROB=0.8
    export CX_PROB=0.2
    export MUT_INDPB=0.5
    export CX_INDPB=0.5
    export TOURNSIZE=4

    # Add any additional settings needed for your system. General settings and system settings need to be set by the user, while GA settings don't need to be changed.
    # Default settings for lambda and polaris are given here. 

    # If you have write access to the shared filesystem on your computation system (such as /lambda_stor), 
    # you can save there. If not, make a directory in /tmp or somewhere else you can write.

    # Lambda Settings
    # export CANDLE_DATA_DIR=/tmp/<user>/data_dir
    
    # Polaris Settings
    # export QUEUE="debug"
    # export CANDLE_DATA_DIR=/home/<user>/data_dir

More information on Polaris job submitting (nodes, walltime, queue, etc...) can be found here: https://docs.alcf.anl.gov/polaris/running-jobs/

4. Create parameter file *hyperparams.json*:

    .. code-block:: JSON

        [

          {
            "name": "train_ml_data_dir",
            "type": "constant",
            "value": "/tmp/weaverr/Data/ml_data/GraphDRP/CCLE-CCLE/split_0"
          },
          {
            "name": "val_ml_data_dir",
            "type": "constant",
            "value": "/tmp/weaverr/Data/ml_data/GraphDRP/CCLE-CCLE/split_0"
          },
          {
            "name": "model_outdir",
            "type": "constant",
            "value": "/tmp/weaverr/Data/out_models/GraphDRP/CCLE/split_0"
          },

          {
            "name": "learning_rate",
            "type": "float",
            "use_log_scale": true,
            "lower": 0.000001,
            "upper": 0.0001
          },
          {
            "name": "canc_num_layers",
            "type": "int",
            "lower": 1,
            "upper": 9
          },
          {
            "name": "batch_size",
            "type": "ordered",
            "element_type": "int",
            "values": [16, 32, 64, 128, 256, 512],
            "sigma": 1
          },
          {
            "name": "warmup_type",
            "type": "ordered",
            "element_type": "string",
            "values": ["none", "linear", "quadratic", "exponential"],
            "sigma": 0.5
          },
          {
            "name": "optimizer",
            "type": "categorical",
            "element_type": "string",
            "values": [
              "Adam",
              "SGD",
              "RMSprop"
            ]
          },

          {
            "name": "epochs",
            "type": "constant",
            "value": 150
          }
        
        ]

Make sure to set the hyperparameter space to what you desire, the above file is an example. The upper and lower describe the bounds of the hyperparameter. Hyperparameters of float, int, ordered, categorical, and constant types are supported, with ordered and categorical hyperparameters supporting float, int, and string types. Log scale exploration is also supported for float and int hyperparameter types. More about additional customization and methods can be found here: https://github.com/ECP-CANDLE/Supervisor/blob/develop/workflows/GA/README.md


Supervisor setup
________________

Set up the environment; omit this step if already installed:

.. code-block:: bash

    # Create environment
    conda create --name IMPROVE python=3.9.16
    conda activate IMPROVE

    # Supervisor for running HPO/GA
    git clone https://github.com/ECP-CANDLE/Supervisor.git
    git checkout develop
    cd Supervisor && PATH=$PATH:$(pwd)/bin

    # swift-t
    conda install --yes -c conda-forge -c swift-t swift-t
    # python libraries
    pip install numpy deap
     
    

Example
_______

First, go into the directory where you have your configuration files:

.. code-block:: bash

    cd ~/Experiment

Then, run the command:

.. code-block:: bash

    supervisor ${location} ${workflow} ${config}

Running an HPO experiment on lambda. The model image is in */software/improve/images/*. We will execute the command above with **location** set to *conda* and **workflow** set to *GA*. This will use the defaults from your conda environment.

.. code-block:: bash

    supervisor conda GA cfg-1.sh


.. _Config Example:

cfg-1.sh:

.. code-block:: bash

    source_cfg -v cfg-my-settings.sh
    
    export CANDLE_MODEL_TYPE="SINGULARITY"
    export MODEL_NAME=/software/improve/images/DeepTTC.sif
    export PARAM_SET_FILE=hyperparams.json


cfg-my-settings.sh:

.. code-block:: bash

    echo SETTINGS
    
    # General Settings
    export PROCS=4
    export PPN=4
    export WALLTIME=01:00:00
    export NUM_ITERATIONS=1
    export POPULATION_SIZE=2
    
    # GA Settings
    export STRATEGY='mu_plus_lambda'
    export OFF_PROP=0.5
    export MUT_PROB=0.8
    export CX_PROB=0.2
    export MUT_INDPB=0.5
    export CX_INDPB=0.5
    export TOURNAMENT_SIZE=4
    
    # Lambda Settings
    # export CANDLE_CUDA_OFFSET=2
    # export CANDLE_DATA_DIR=/tmp/<user>/data_dir
    
    # Polaris Settings
    # export QUEUE="debug"
    # export CANDLE_DATA_DIR=/home/<user>/data_dir


hyperparams.json:

.. code-block:: JSON

    [
    
      {
        "name": "learning_rate",
        "type": "float",
        "lower": 0.000001,
        "upper": 0.0001,
        "sigma": 0.00005
      },
    
      {
        "name": "batch_size",
        "type": "ordered",
        "element_type": "int",
        "values": [256, 512, 1028],
        "sigma": 1
      },
    
      {
        "name": "epochs",
        "type": "constant",
        "value": 5
      }
    
    ]



Debugging
_______

While/after running HPO, there will be ``model.log`` files which contain the important information regarding that model's run. They can be found at ``<candle_data_dir>/<model_name>/Output/EXP<number>/run_<number>``. To debug, use a ``grep -r "ABORT"`` in the experiment directory ``<candle_data_dir>/<model_name>/Output/EXP<number>`` to find which run file which is causing the error in your workflow, ``cd run_<number>`` to navigate there, and ``cat model.log`` to observe the abort and what error caused it. Observing the ``MODEL_CMD`` (which tells the hyperparameters) and the ``IMPROVE_RESULT`` (which tells the  evaluation of those hyperparameters) can also be helpful.



Results
_______

After running HPO, there will be the turbine output and experiment directories. The ``turbine_output`` directory is found in the same directory as the config files and contains a ``final_result_<number>`` file which puts the HPO results in a table. The experiment directory is found at ``<candle_data_dir>/<model_name>/Output/EXP<number>`` and contains the ``output.csv`` file which has ALL the hpo parameters and results automatically parsed. The experiment directory also contains the hyperparams.json file you used to help remember the hyperparameter space you explored.



.. _Analysis:

Analysis
_______

To analyze the HPO run, there are two recommended methods. The first provides a ranking of hyperparameter choices. The second provides a ranking and visualization:

(1) Firstly, the user could run the following commands in the experiment directory. The user is required to define the number of hyperparameters. In the example hyperparams.json file given, this would be 3 (learning_rate, batch_size, epochs). The sorted, unique choices of hyperparameters are put into a new ``sorted_unique_output.csv`` file.

.. code-block:: bash

    num_hyperparams=3
    num_columns=$((num_hyperparams + 1))
    (head -n 1 output.csv && tail -n +2 output.csv | sort -t, -k$num_columns -n | uniq) > sorted_unique_output.csv

(2) Secondly, the user could secure copy the output.csv file, then use google colab to show tables and plot. The secure copy command should be run in your terminal (not logged into Argonne's computation system) as the following: ``scp <user>@<computation_address>:~/path/to/your/output.csv \path\on\local\computer``. For example, as secure copy command could look like: ``scp weaverr@polaris.alcf.anl.gov:~/data_dir/DeepTTC-testing/Output/finished_EXP060/output.csv \Users\rylie\Argonne\HPO``. Note that this assumes the user is using Unix. If running a Unix-like system on Windows, the command will look like ``scp <user>@<computation_address>:~/path/to/your/output.csv /c/Users/username/Path/On/Local/Computer``.

Once the file is secure copied to your local computer, it can be loaded into and used in google colab. A generalizable, plug-and-play colab file is being made for easy use. Simply make a copy and follow the instructions: https://colab.research.google.com/drive/1Us5S9Ty7qGtibT5TcwM9rTE7EIA9V33t?usp=sharing
