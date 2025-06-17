Configuration Example with XGBoost for DRP
==========================================================

Two things:

* **Model-specific parameter definitions**: These are specified in the :code:`model_params_def.py` file.
* **Default parameters**: These are specified in the .ini file.


Model-specific parameter definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: python

    from improvelib.utils import str2bool

    preprocess_params = []

    train_params = [
        {"name": "max_depth",
        "type": int,
        "default": 6,
        "help": "Tree HP. Maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit and aggressively consumes memory. Range [1, inf]."
        },
        {"name": "min_child_weight",
        "type": int,
        "default": 1,
        "help": "Tree HP. Minimum sum of instance weight (hessian) needed in a child. The larger min_child_weight is, the more conservative the algorithm will be. Range [0, inf]."
        },
        {"name": "subsample",
        "type": float,
        "default": 1,
        "help": "Tree HP. Subsample ratio of the training instances. Setting it to 0.5 means that XGBoost would randomly sample half of the training data prior to growing trees. and this will prevent overfitting. Subsampling will occur once in every boosting iteration. Range [0, 1]."
        },
        {"name": "colsample_bytree",
        "type": float,
        "default": 1,
        "help": "Tree HP. Fraction of columns used for each tree construction. Lowering this value can prevent overfitting by training on a subset of the features. Range [0, 1]."
        },
        {"name": "gamma",
        "type": int,
        "default": 0,
        "help": "Learning HP. Minimum loss reduction required to make a further partition on a leaf node of the tree. The larger gamma is, the more conservative the algorithm will be. Range [0, inf]."
        },
        {"name": "lambda",
        "type": float,
        "default": 1,
        "help": "Learning HP. L2 regularization term on weights. Increasing this value will make model more conservative. Range [0, 1]."
        },
        {"name": "alpha",
        "type": float,
        "default": 0,
        "help": "Learning HP. L1 regularization term on weights. Increasing this value will make model more conservative Range [0, 1]."
        },
    ]

    infer_params = []




Default parameters
^^^^^^^^^^^^^^^^^^^^


.. code-block::

    [DEFAULT]

    [Preprocess]
    train_split_file = CCLE_split_0_train.txt
    val_split_file = CCLE_split_0_val.txt
    test_split_file = CCLE_split_0_test.txt
    data_format = .parquet
    y_data_file = response.tsv
    cell_transcriptomic_file = cancer_gene_expression.tsv
    cell_transcriptomic_transform = [['subset', 'LINCS_SYMBOL'], ['scale', 'std']]
    drug_mordred_file = drug_mordred.tsv
    drug_mordred_transform = [['scale', 'std']]

    [Train]
    data_format = .parquet
    model_file_name = model
    model_file_format = .json
    learning_rate = 0.3
    patience = 50
    epochs = 300

    [Infer]
    data_format = .parquet
    model_file_name = model
    model_file_format = .json