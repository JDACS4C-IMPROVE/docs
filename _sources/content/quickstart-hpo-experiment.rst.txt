Hyper Parameter Optimization (HPO)
==================================

Requirements
____________

Your model must be CANDLE compliant.

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

Example of config files can be found at <https://github.com/ECP-CANDLE/Tests/tree/main/sv-tool/user-case-3>. Create with the following steps:

1. ``mkdir Experiment && cd Experiment``

2. Create config file *my-config.sh*:

   .. code-block:: bash

       # Model settings
       export CANDLE_MODEL_TYPE="SINGULARITY"
       export MODEL_NAME=${/PATH/TO/SINGULARITY/IMAGE/FILE.sif}
       export PARAM_SET_FILE=${/PATH/TO/GA/PARAMETER/FILE.json}
       # If you have write access to /lambda_stor, you can save on the shared
       # filesystem. If not, make a directory in /tmp
       export CANDLE_DATA_DIR=/tmp/my_username

       # System settings
       export PROCS=3 # minimum 3 

3. Create parameter file *my-param-space.json*:

    .. code-block:: JSON

        [
            {

                "name": "activation",
                "type": "categorical",
                "element_type": "string",
                "values": [
                    "softmax","elu","softplus","softsign","relu","tanh","sigmoid","hard_sigmoid","linear"
                ]
            },
            {
                "name": "optimizer",
                "type": "categorical",
                "element_type": "string",
                "values": ["adam", "rmsprop"]
            },
            {
                "name": "dropout",
                "type": "float",
                "lower": 0.0,
                "upper": 0.9,
                "sigma": 0.045
            },
            {
                "name": "batch_size",
                "type": "ordered",
                "element_type": "int",
                "values": [16, 32, 64, 128, 256],
                "sigma": 1
            },
            {
                "name": "epochs",
                "type": "constant",
                "value": 5
            }
        ]


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

.. code-block:: bash

    supervisor ${location} ${workflow} ${config}

Running an HPO experiment on lambda. The model image is in */software/improve/images/*. We will execute the command above with **location** set to *lambda* and **workflow** set to *GA*.
We have a directory called *Experiment* and created a config file named *my-config.sh* in this directory: 

.. code-block:: bash

    supervisor lambda GA Experiment/my-config.sh


.. _Config Example:

my-config.sh:

.. code-block:: bash

    # Model settings
    export CANDLE_MODEL_TYPE="SINGULARITY"
    export MODEL_NAME=/software/improve/images/HiDRA.sif
    export PARAM_SET_FILE=~/Experiment/my-param-space.json
    export CANDLE_DATA_DIR=/tmp/demo

    # System settings
    export PROCS=3


my-param-space.json:

.. code-block:: JSON

        [
            {
                "name": "batch_size",
                "type": "ordered",
                "element_type": "int",
                "values": [16, 32, 64, 128, 256],
                "sigma": 1
            },
            {
                "name": "epochs",
                "type": "constant",
                "value": 5
            }
        ]

