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

At a high level, the upper and lower describe the bounds of the hyperparameter. Hyperparameters of float, int, ordered, categorical, and constant types are supported, with ordered and categorical hyperparameters supporting float, int, and string types. Log scale exploration is also supported for float and int hyperparameter types.

More specifically, the hyperparameter configuration file has a json format consisting of a
list of json dictionaries, each one of which defines a hyperparameter. Each dictionary has the following required keys:

- name: the name of the hyperparameter (e.g. _epochs_)
- type: determines how the initial population (i.e. the hyperparameter sets) are initialized from the named parameter and how those values are subsequently mutated by the GA. Type is one of `constant`, `int`, `float`, `logical`, `categorical`, or `ordered`.
  - `constant`:
    - each model is initialized with the same specifed value
    - mutation always returns the same specified value
  - `int`:
    - each model is initialized with an int randomly drawn from the range defined by `lower` and `upper` bounds
    - mutation is peformed by adding the results of a random draw from
      a gaussian distribution to the current value, where the gaussian distribution's mu is 0 and its sigma is specified by the `sigma` entry.
  - `float`:
    - each model is initialized with a float randomly drawn from the range defined by `lower` and `upper` bounds
    - mutation is peformed by adding the results of a random draw from
      a gaussian distribution to the current value, where the gaussian distribution's mu is 0 and its sigma is specified by the `sigma` entry.
  - `logical`:
    - each model is initialized with a random boolean.
    - mutation flips the logical value
  - `categorical`:
    - each model is initialized with an element chosen at random from the list of elements in `values`.
    - mutation chooses an element from the `values` list at random
  - `ordered`:
    - each model is inititalized with an element chosen at random from the list of elements in `values`.
    - given the index of the current value in the list of `values`, mutation selects the element _n_ number of indices away, where n is the result of a random draw between 1 and `sigma` and then is negated with a 0.5 probability.

The following keys are required depending on value of the `type` key.

If the `type` is `constant`:

- `value`: the constant value

If the `type` is `int`, or `float`:

- `lower`: the lower bound of the range to draw from
- `upper`: the upper bound of the range to draw from

If the `type` is `categorical`:

- `values`: the list of elements to choose from
- `element_type`: the type of the elements to choose from. One of `int`, `float`, `string`, or `logical`

If the `type` is `ordered`:

- `values`: the list of elements to choose from
- `element_type`: the type of the elements to choose from. One of `int`, `float`, `string`, or `logical`

The following keys are optional depending on value of the `type` key.

If the `type` is `constant` or `float`:

- `use_log_scale`: whether to apply mutation on log_10 of the hyperparameter or not
- `sigma`: the sigma value used by the mutation operator. Roughly, it controls the size of mutations (see above).

If the `type` is `ordered`:

- `sigma`: the sigma value used by the mutation operator. Roughly, it controls the size of mutations (see above).

A sample hyperparameter definition file:

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
            "upper": 0.0001,
            "sigma": 0.1
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
            "values": ["none", "linear", "quadratic", "exponential"]
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

Note that any other keys are ignored by the workflow but can be used to add additional information about the hyperparameter. For example, the sample files could contain a `comment` entry that contains additional information about that hyperparameter and its use.
