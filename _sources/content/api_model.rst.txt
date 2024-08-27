Creating Model-specific parameters
=================================

Model-specific parameters should be defined as a list of dictionaries, where each dictionary is a parameter with the following attributes: name, type, default, and help. 
Other attributes that are compatible with argpase can also be specified, see argparse.ArgumentParser.add_argument() (LINK) for more information.
Defining a parameter with the same name as an existing IMPROVE or application-specific parameter is not allowed.

.. code-block:: python

    my_params_example = [
        {
            # name of the argument
            "name": "y_data_files",
            # type of the argument
            "type": str,
            # number of arguments that should be consumed
            "nargs": "+",
            # help message
            "help": "List of files that contain the y (prediction variable) data.",
        },
        {
            # name of the argument
            "name": "supplement",
            # type of the argument
            "type": str,
            # number of arguments that should be consumed
            "nargs": 2,
            # name of the argument in usage messages
            "metavar": ("FILE", "TYPE"),
            # action to be taken when this argument is encountered
            "action": "append",
            # default value of the argument
            "default": [ ('a' , 'b')],
            "help": "Supplemental data tuple FILE and TYPE. FILE is in INPUT_DIR.",   # help message
        }
    ]



For clarity, we recommend putting model-specific parameter definitions in a separate file and importing the list to each model script (i.e. preprocess, train, infer).
You can all model-specific parameters in a single list, or in separate lists for preprocess, train, and infer. This list is passed to initalize_parameters in the main() as additional_definitions.



