Hyper Parameter Optimization (HPO)
==================================

Requirements
____________

Your model must be CANDLE compliant, and must print the following line to optimize on with the HPO (val_loss is being optimized in this example):

   .. code-block:: python

      print("\nIMPROVE_RESULT val_loss:\t{}\n".format(scores["val_loss"]))

Your model must be containerized and packaged in a singularity image. You can identify the image file by the **\*.sif** suffix. The container should expose the following interface scripts:

+ preprocess.sh
+ train.sh
+ infer.sh


Steps 
_____

1. Install prerequisites
2. :ref:`Create config files <Config Overview>` for experiment. 
3. :ref:`Run <Run>` HPO with supervisor::

    supervisor ${location} ${workflow} ${config}


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
    export PARAM_SET_FILE=${/PATH/TO/GA/PARAMETER/FILE.json}

3. Create config file *cfg-my-settings.sh*:

   .. code-block:: bash

    echo SETTINGS
    
    # General Settings
    export PROCS=4
    export PPN=4
    export WALLTIME=01:00:00
    export NUM_ITERATIONS=3
    export POPULATION_SIZE=2
    
    # GA Settings
    export GA_STRATEGY='mu_plus_lambda'
    export OFFSPRING_PROPORTION=0.5
    export MUT_PROB=0.8
    export CX_PROB=0.2
    export MUT_INDPB=0.5
    export CX_INDPB=0.5
    export TOURNSIZE=4

    # Add any additional settings needed for your system. General settings and system settings need to be set by user, while GA settings don't need to be changed.
    # Default settings for lambda and polaris are given here. 

    # If you have write access to the shared filesystem on your computation system (such as /lambda_stor), 
    # you can save there. If not, make a directory in /tmp or somewhere else you can write.

    # Lambda Settings
    # export CANDLE_CUDA_OFFSET=1
    # export CANDLE_DATA_DIR=/tmp/<user>/data_dir
    
    # Polaris Settings
    # export QUEUE="debug"
    # export CANDLE_DATA_DIR=/home/<user>/data_dir

More information on polaris job submitting (nodes, walltime, queue, etc...) can be found here: https://docs.alcf.anl.gov/polaris/running-jobs/

4. Create parameter file *hyperparams.json*:

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

Make sure to set the hyperparameter space to what you desire. Upper and lower describe bounds of the hyperparameter. Higher sigma causes bigger mutations in the genetic algorithm. More about the hyperparameter file can be found at the hyperparameter configuration file here: https://github.com/ECP-CANDLE/Supervisor/blob/develop/workflows/GA/README.md


Supervisor setup
________________

Set up the environment, omit this step if already installed:

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
    pip install numpy deap
     
    
    
.. _Run:

Example
_______

First, go into the directory where you have your configuration files:

.. code-block:: bash

    cd ~/Experiment

Then, run the command:

.. code-block:: bash

    supervisor ${location} ${workflow} ${config}

Running an HPO experiment on lambda. The model image is in */software/improve/images/*. We will execute the command above with **location** set to *lambda* and **workflow** set to *GA*.

.. code-block:: bash

    supervisor lambda GA cfg-1.sh


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
    # export CANDLE_CUDA_OFFSET=1
    # export CANDLE_DATA_DIR=/tmp/<user>/data_dir
    
    # Polaris Settings
    # export QUEUE="debug"
    # export CANDLE_DATA_DIR=/home/<user>/data_dir


hyperparams.json:

.. code-block:: JSON

    [
    
      {
        "name": "activation",
        "type": "categorical",
        "element_type": "string",
        "values": [
          "softmax",
          "elu",
          "softplus",
          "softsign",
          "relu",
          "tanh",
          "sigmoid",
          "hard_sigmoid",
          "linear"
        ]
      },
    
      {
        "name": "learning_rate",
        "type": "float",
        "lower": 0.000001,
        "upper": 0.2,
        "sigma": 0.05
      },
    
      {
        "name": "batch_size",
        "type": "ordered",
        "element_type": "int",
        "values": [32, 64, 128],
        "sigma": 1
      },
    
      {
        "name": "epochs",
        "type": "constant",
        "value": 5
      }
    
    ]

