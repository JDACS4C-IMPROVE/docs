Hyper Parameter Optimization (HPO)
==================================

Requirements
____________

- Supervisor code
    - your search path includes the **bin** directory of the Supervisor repository.
- Model 
    - containerized
    - candle interface
    - improve interface 


Steps
_____

1. Create config files
2. Execute workflow with supervisor


.. code-block:: bash
    supervisor ${location} ${workflow} ${config}



*Example:*

Running an HPO experiment on lambda. The model image is in */software/improve/images/*. We will execute the command above with **location** set to *lambda* and **workflow** set to *GA*.
We have a directory called *Experiment* and created a config file named *my-config.sh* in this directory. 


.. code-block:: bash

    supervisor lambda GA my-config.sh


Config file(s)
______________

Example of config files can be found at <https://github.com/ECP-CANDLE/Tests/tree/main/sv-tool/user-case-3>. A confg file includes the following settings:

.. code-block:: bash

    # Model settings
    export CANDLE_MODEL_TYPE="SINGULARITY"
    export MODEL_NAME=${/PATH/TO/SINGULARITY/IMAGE/FILE.sif}
    export PARAM_SET_FILE=${/PATH/TO/GA/PARAMETER/FILE.json}

    # System settings
    export PROCS=


*Example:*

1. ``mkdir Experiment && cd Experiment``
2. Create config file

    .. code-block:: bash

        # Model settings
        export CANDLE_MODEL_TYPE="SINGULARITY"
        export MODEL_NAME=/software/improve/images/GraphDRP.sif
        export PARAM_SET_FILE=my-graphdrp-search.json

        # System settings
        export PROCS=


3. Create parameter file:

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


**swift-t and Supervisor**

Why?

.. code-block:: bash
    git clone https://github.com/ECP-CANDLE/Supervisor.git
    conda install
    # Add path to supervisor to your environment: 
    cd Supervisor && PATH = $PATH:$(pwd)/bin``

**IMPROVE Models**

Your model is packaged in a singularity image. You can identify the image file by the **\*.sif** suffix. The container exposes following interface scripts:

+ preprocess.sh
+ train.sh
+ infer.sh




