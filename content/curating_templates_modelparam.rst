Model-Specific Parameter Definition Template
==============================================

Below is a template for defining model-specific parameters. 
If no params are required by the model, then it should be an empty list.
The file should be saved as :code:`model_params_def.py` so that each list is imported correctly by the model scripts.
For more information on setting model-specific parameters see :doc:`api_model`.

.. code-block:: python

    from improvelib.utils import str2bool

    preprocess_params = [
        {"name": "name1",
        "type": str2bool,
        "default": True,
        "help": "Help goes here",
        },
        {"name": "name2",
        "type": str,
        "default": "text",
        "help": "Help goes here.",
        },
        {"name": "name3",
        "type": int,
        "default": 2,
        "help": "Help goes here.",
        },
    ]

    train_params = [
        {"name": "name4",
        "type": float,
        "default": .02,
        "help": "Help goes here."
        },
    ]

    infer_params = []