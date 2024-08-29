Creating Model-Specific Parameters
====================================

Model-specific parameters should be defined as a list of dictionaries, where each dictionary is a parameter with the following attributes: name, type, default, and help. 
Other attributes that are compatible with argparse can also be specified, see `argparse.ArgumentParser.add_argument() <https://docs.python.org/3/library/argparse.html#the-add-argument-method>`_ for more information.
Defining a parameter with the same name as an existing IMPROVE or application-specific parameter is not allowed.

.. code-block:: 

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
You can put all model-specific parameters in a single list, or in separate lists for preprocess, train, and infer. This list is passed to initalize_parameters in the :code:`main()` as additional_definitions.

For example, in :code:`mymodel_param_definitions.py` you can have:

.. code-block:: 

    mymodel_preprocess_params = [
        {
            "name": "scaling_type",
            "type": str,
            "default": "StandardScaler",
            "help": "Type of scikitlearn scaling to use.",
        }
    ]
    mymodel_train_params = [
        {
            "name": "model_arch",
            "default": "GINConvNet",
            "choices": ["GINConvNet", "GATNet", "GAT_GCN", "GCNNet"],
            "type": str,
            "help": "Model architecture to run."}
        }
    ]
    mymodel_infer_params = [
        {
            "name": "print_time",
            "type": str2bool,
            "default": "False",
            "help": "Whether to print the time or not.",
        }
    ]

The appropriate list can then be imported into the appropriate script. For example, in :code:`model_preprocess_improve.py` we would add the following:

.. code-block:: 

    from mymodel_param_definitions import mymodel_preprocess_params


Then this list of parameter definitions is passed to :code:`cfg.initialize_parameters` in :code:`main()`:

.. code-block::

    params = cfg.initialize_parameters(
        pathToModelDir=filepath,
        default_config="model_default_params.txt",
        default_model=None,
        additional_cli_section=None,
        additional_definitions=mymodel_preprocess_params,
        required=None
    )




