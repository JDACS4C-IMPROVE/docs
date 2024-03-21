Hyper Parameter Optimization (HPO)
==================================

Requirements
____________

The following are the requirements as a model curator for others to run HPO on your model.



IMPROVE MODEL (Defined for Containerization)
____________________________________________

Your model must be IMPROVE compliant, reading arguments from a '.txt' file and overwriting with command-line arguments. Your model must also be defined in a 'def' file for singularity containerization. Default definition files can be found in the `IMPROVE Singularity repository <https://github.com/JDACS4C-IMPROVE/Singularity>`_. The container should expose the following interface scripts:

+ preprocess.sh
+ train.sh
+ infer.sh


To test your scripts with containerization, it's recommended you build a container and run the following commands (customized with your arguments):

.. code-block:: bash

    singularity exec --bind $IMPROVE_DATA_DIR:/IMPROVE_DATA_DIR <path_to_sif_file>.sif preprocess.sh /IMPROVE_DATA_DIR \ 
    --train_split_file <dataset>_split_0_train.txt --val_split_file <dataset>_split_0_val.txt \ 
    --ml_data_outdir /IMPROVE_DATA_DIR/<desired_outdir>

.. code-block:: bash
    singularity exec --nv --bind $IMPROVE_DATA_DIR:/IMPROVE_DATA_DIR <path_to_sif_file>.sif train.sh <gpu_num> /IMPROVE_DATA_DIR \ 
--train_ml_data_dir <path> --val_ml_data_dir <dir> --model_outdir <path> --test_ml_data_dir <path>



HYPERPARAMETER SPACE
____________________

You will also need to define the hyperparameter space, which will override the arguments in the .txt file. For this reason, any pathing arguments needed for your train script will also need to be defined as 'constant' hyperparameters in the space (such as train_ml_data_dir below).

The upper and lower describe the bounds of the hyperparameter. Hyperparameters of float, int, ordered, categorical, and constant types are supported, with ordered and categorical hyperparameters supporting float, int, and string types. Log scale exploration is also supported for float and int hyperparameter types. More about additional customization and methods can be found here: https://github.com/ECP-CANDLE/Supervisor/blob/develop/workflows/GA/README.md


1. Create parameter file *hyperparams.json*:

    .. code-block:: JSON

        [

          {
            "name": "train_ml_data_dir",
            "type": "constant",
            "value": "<train_data_dir>"
          },
          {
            "name": "val_ml_data_dir",
            "type": "constant",
            "value": "<val_data_dir>"
          },
          {
            "name": "model_outdir",
            "type": "constant",
            "value": "<desired_outdir>"
          },

          {
            "name": "learning_rate",
            "type": "float",
            "use_log_scale": true,
            "lower": 0.000001,
            "upper": 0.0001
          },
          {
            "name": "num_layers",
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
