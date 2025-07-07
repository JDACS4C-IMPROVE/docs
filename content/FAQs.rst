Frequently Asked Questions
==============================


Is it possible to use IMPROVE without Conda?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The models can be run without Conda, provided you install the requirements by another method. 
Currently, the workflows require Conda in order to separate the workflow environment from the 
model environment.

Can I use classification or regression models?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can use either! All of our DRP models are regression models, but we have :doc:`a Synergy model <Models-Synergy-DeepDDS>` that is a classification model. 
Be sure to change the parameter :code:`metric_type` to :code:`classification` in *train* and *infer*. 
You will have to implement a binarization step in *preprocess*. Here's an example:

.. code-block:: python

    synergy_bins = [-np.inf, params['cutoff'], np.inf]
    synergy_labels = [0, 1]
    y_data_stage['label'] = pd.cut(np.array(y_data_stage[params['y_col_name']]), bins=synergy_bins, labels=synergy_labels)


We recommend adding a preprocess parameter for a cutoff in :code:`model_params_def.py`, so this can be changed via command line or workflows like in the example above. Here's an example:

.. code-block:: python

    preprocess_params = [
        {"name": "cutoff",
        "type": float,
        "default": 9.24,
        "help": "Cutoff for binarization. 10 was used in the paper, 9.24 is used for updated DrugComb v1.5 to allow for the same number of positive samples. ",
        },
    ]

Additionally, some classification metrics used the target scores (typically the probability estimates of the positive class). 
You'll need to pass these values in *train* and *infer* to :doc:`api_utils_compute_performance_scores` like so:

.. code-block:: python

    val_scores = frm.compute_performance_scores(
        y_true=T,
        y_pred=Y,
        stage="val",
        metric_type=params["metric_type"],
        output_dir=params["output_dir"],
        y_prob=S
    )

