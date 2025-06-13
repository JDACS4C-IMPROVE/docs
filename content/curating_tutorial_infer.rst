Inference Script Example with XGBoost for DRP
==========================================================

This script `xgboostdrp_infer_improve.py <https://github.com/JDACS4C-IMPROVE/XGBoost-DRP/blob/develop/xgboostdrp_infer_improve.py>`_ performs inference on the test data using the saved XGBoost model from *train*.
The script generates model predictions and prediction performance scores for the test data. 
The naming convention for the inference script is `MODELNAME_infer_improve.py`. 

**Inputs:**
The directory containing the preprocessed data is set with :code:`params['input_data_dir']` which is set to the same directory as :code:`params['output_dir']` was in the *preprocess* script.
The directory containing the saved model is set with :code:`params['input_model_dir']` which is set to the same directory as :code:`params['output_dir']` was in the *train* script.

* **Processed x data**: Processed feature data for XGBoost model.

  * test_data.parquet

* **Processed y data**: File with true y values and IDs (additional metadata is acceptable).

  * test_y_data.csv

* **Trained model**: The model file name and file format are specified by, respectively, :code:`params["model_file_name"]` and :code:`params["model_file_format"]`.

  * model.json

**Outputs:**
All the outputs from the *infer* script are saved in :code:`params['output_dir']`.

* **Predictions on test data**: The predictions from the best model.

  * :code:`test_y_data_predicted.csv`

* **Prediction performance scores on test data**: The performance scores are calculated using the model predictions and the true y values. 
  Which metrics are calculated differ for regression vs. classification models, specified by :code:`params['metric_type']`.

  * :code:`test_scores.json`

* **Parameter log**: Log of the :code:`params` dictionary.

  * param_log_file.txt

* **Timer log**: Log of the :code:`Timer` dictionary.

  * runtime_preprocess.json


Inference Imports
^^^^^^^^^^^^^^^^^^^
Similar to the imports for the *preprocess* and *train* scripts, this section consists of five basic components:

* **Import basic functionality**: sys, Path, etc.
* **Import core improvelib functionality**: we import this as 'frm' for historical reasons.
* **Import application-specific functionality**: this will need to be changed if curating a model for another application.
* **Import model-specific functionality**: at minimum this should included the model parameter definitions, but can also include other packages your model requires (Polars, numpy, etc).
* **Get file path**: filepath is used by the Config and this line should be present as is.

Notice that here we are using the config for *infer* and we are importing XGBoost under the model-specific imports:

.. code-block:: python

    import sys
    from pathlib import Path
    import pandas as pd

    # Core improvelib imports
    import improvelib.utils as frm
    # Application-specific (DRP) imports
    from improvelib.applications.drug_response_prediction.config import DRPInferConfig

    # Model-specifc imports
    from model_params_def import infer_params
    import xgboost as xgb

    filepath = Path(__file__).resolve().parent

.. note::

    You may need to add imports if your model requires other packages and you may need to change the application-specific imports if using another application.


Inference :code:`run()`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function contains the bulk of the code it loads the preprocessed test data and the trained model, performs gets predictions on the test set, and saves predictions and scores. Here we walk through the function.

**Define the function.** The parameter dictionary must be passed to this function:

.. code-block:: python

    def run(params):

**Build model path** with :doc:`api_utils_build_model_path` and **create the data name** for test set with :doc:`api_utils_build_ml_data_file_name`. 
This ensures consistency in naming. This code should be the same for all models:

.. code-block:: python

    modelpath = frm.build_model_path(model_file_name=params["model_file_name"],
                                     model_file_format=params["model_file_format"],
                                     model_dir=params["input_model_dir"])
    test_data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="test")

**Load the test data.**  
Here we load the test x data with the response values and isolate the y data and drop the y data from the remaining feature data:

.. code-block:: python

    test_data = pd.read_parquet(Path(params["input_data_dir"]) / test_data_fname)

    yte = test_data[[params["y_col_name"]]]
    xte = test_data.drop(columns=[params['y_col_name']])

.. note::

    This may differ based on how you saved the x data in *preprocess*.


**Load the model and compute predictions.**

.. code-block:: python

    # Load model
    model = xgb.XGBRegressor()
    model.load_model(str(modelpath))

    # Compute predictions
    test_pred = model.predict(xte)
    test_true = yte.values.squeeze()

.. note::

    The implementation of this will vary depending on your model. The predictions and ground truth should be numpy arrays.

**Save raw predictions in dataframe.**
The predictions from the model on the validation data as well as the ground truth are saved with :doc:`api_utils_store_predictions_df`.

.. code-block:: python

    frm.store_predictions_df(
        y_true=test_true, 
        y_pred=test_pred, 
        stage="test",
        y_col_name=params["y_col_name"],
        output_dir=params["output_dir"],
        input_dir=params["input_data_dir"]
    )

.. note::

    The variables :code:`val_true` and :code:`val_pred` can be whatever you use in your script, but the rest should be the same.
    :code:`y_true` is optional and ground truth is not required for inference.
    :code:`params['y_col_name']` can be changed in the configuration file.

**Compute performance scores.**
Performance scores on the test data are calculated and saved with :doc:`api_utils_compute_performance_scores`.

.. code-block:: python

    if params["calc_infer_scores"]:
        test_scores = frm.compute_performance_scores(
            y_true=test_true, 
            y_pred=test_pred, 
            stage="test",
            metric_type=params["metric_type"],
            output_dir=params["output_dir"]
        )

.. note::

    The variables :code:`val_true` and :code:`val_pred` can be whatever you use in your script, but the rest should be the same.
    If ground truth is not available, :code:`params["calc_infer_scores"]` can be set to :code:`False`.
    :code:`params['metric_type']` can be changed in the configuration file, if using a classification model instead of a regression model.

**Return True**

.. code-block:: python

    return True


Inference :code:`main()` and main guard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Similar to the :code:`main()` function in *preprocess* and *train*, this is called upon script execution and gets the parameters, calls :code:`run()`, and records the time it takes for the model to run. Each line is explained below:

* The first line (:code:`cfg = DRPInferConfig()`) initializes the configuration object for each script as appropriate.
* The second line initializes the parameters. Parameters set by command line (e.g. :code:`--input_data_dir /my/path/to/dir`) take precedence over the values in the config file, which take precedence over the default values provided by improvelib.
  
  * :code:`pathToModelDir` is the current path in the system. :code:`filepath` is already present in the template by :code:`filepath = Path(__file__).resolve().parent`.
  * :code:`default_config` is the default configuration file, as a string.
  * :code:`additional_definitions` is the list of model-specific parameters.
* The third line initializes the :doc:`api_utils_Timer`.
* The fourth line calls :code:`run()` with the parameters. As dicussed, :code:`run()` contains the model code.
* The fifth line ends the :doc:`api_utils_Timer` and saves the time to a JSON file in the output_dir.
* The last (optional) line prints a message indicating that the script is finished and ran successfully.


.. code-block:: python

    def main(args):
        cfg = DRPInferConfig()
        params = cfg.initialize_parameters(pathToModelDir=filepath,
                                        default_config="xgboostdrp_params.ini",
                                        additional_definitions=infer_params)
        timer_infer = frm.Timer()    
        status = run(params)
        timer_infer.save_timer(dir_to_save=params["output_dir"], 
                            filename='runtime_infer.json', 
                            extra_dict={"stage": "infer"})
        print("\nFinished model inference.")

.. note::

    You will need to change the name of :code:`default_config` to the one for your model, and the Config if you are using an application other than DRP.

The main guard below prevents unintended execution and should be present as is:

.. code-block:: python

    if __name__ == "__main__":
        main(sys.argv[1:])