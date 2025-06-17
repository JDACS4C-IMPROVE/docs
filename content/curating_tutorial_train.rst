Training Script Example with XGBoost for DRP
==========================================================

This script `xgboostdrp_train_improve.py <https://github.com/JDACS4C-IMPROVE/XGBoost-DRP/blob/develop/xgboostdrp_train_improve.py>`_ executes XGBoost training with the processed data from *preprocess*.
The script generates a trained model, and model predictions, and prediction performance scores calculated using the validation data.
When the model converges (i.e., prediction performance stops improving on validation data), the model is saved into a file.
The naming convention for the preprocessing script is `<MODEL>_preprocess_improve.py`.
 
**Inputs:**
The directory containing the preprocessed data is set with :code:`params['input_dir']` which is set to the same directory as :code:`params['output_dir']` was in the *preprocess* script. 
The train data and val data are loaded and used for, respectively, model training and early stopping.

* **Processed x data**: Processed feature data for XGBoost model.

  * train_data.parquet
  * val_data.parquet

* **Processed y data**: File with true y values and IDs (additional metadata is acceptable).

  * train_y_data.csv
  * val_y_data.csv

**Outputs:**
All the outputs from the *train* script are saved in :code:`params['output_dir']`.

* **Trained model**: The model file name and file format are specified by, respectively, :code:`params["model_file_name"]` and :code:`params["model_file_format"]`.

  * model.json

* **Predictions on validation data**: The predictions from the best model.

  * :code:`val_y_data_predicted.csv`

* **Prediction performance scores on validation data**: The performance scores are calculated using the model predictions and the true y values. 
  Which metrics are calculated differ for regression vs. classification models, specified by :code:`params['metric_type']`.

  * :code:`val_scores.json`

* **Parameter log**: Log of the :code:`params` dictionary.

  * param_log_file.txt

* **Timer log**: Log of the :code:`Timer` dictionary.

  * runtime_preprocess.json

Training Imports
^^^^^^^^^^^^^^^^^^^
Similar to the imports for the *preprocess* script, this section consists of five basic components:

* **Import basic functionality**: sys, Path, etc.
* **Import core improvelib functionality**: we import this as 'frm' for historical reasons.
* **Import application-specific functionality**: this will need to be changed if curating a model for another application.
* **Import model-specific functionality**: at minimum this should included the model parameter definitions, but can also include other packages your model requires (Polars, numpy, etc).
* **Get file path**: filepath is used by the Config and this line should be present as is.

Notice that here we are using the config for *train* and we are importing XGBoost under the model-specific imports:

.. code-block:: python

    import sys
    from pathlib import Path
    import pandas as pd

    # Core improvelib imports
    import improvelib.utils as frm
    # Application-specific (DRP) imports
    from improvelib.applications.drug_response_prediction.config import DRPTrainConfig

    # Model-specifc imports
    from model_params_def import train_params
    import xgboost as xgb

    filepath = Path(__file__).resolve().parent 

.. note::

    You may need to add imports if your model requires other packages and you may need to change the application-specific imports if using another application.


Training :code:`run()`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function contains the bulk of the code: it loads the preprocessed data, trains the model, and saves the model and prediction and scores on the validation data. Here we walk through the function.

**Define the function.** The parameter dictionary must be passed to this function:

.. code-block:: python

    def run(params):

**Build model path** with :doc:`api_utils_build_model_path` and **create the data names** for train and val sets with :doc:`api_utils_build_ml_data_file_name`. 
This ensures consistency in naming. This code should be the same for all models:

.. code-block:: python

    modelpath = frm.build_model_path(
        model_file_name=params["model_file_name"],
        model_file_format=params["model_file_format"],
        model_dir=params["output_dir"]
    )
    train_data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="train")
    val_data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="val")


**Load the train and val data.**  
Here we load the stage x data with the response values and isolate the y data and drop the y data from the remaining feature data:

.. code-block:: python

    train_data = pd.read_parquet(Path(params["input_dir"]) / train_data_fname)
    val_data = pd.read_parquet(Path(params["input_dir"]) / val_data_fname)

    # Train data
    ytr = train_data[[params["y_col_name"]]]
    xtr = train_data.drop(columns=[params['y_col_name']])

    # Val data
    yvl = val_data[[params["y_col_name"]]]
    xvl = val_data.drop(columns=[params['y_col_name']])

.. note::

    This may differ based on how you saved the x data in *preprocess*.


**Prepare, train, and save model.**
Here we create a dictionary for the parameters for XGBoost with the value set to the IMPROVE parameters so that if a 
parameter is changed (e.g. on the command line, or via HPO workflows) it is properly used in the XGBoost model.
We also initialize the XGBRegressor, fit the model using the validation set for early stopping, save the model to the modelpath, 
and delete the model to preserve memory.

.. code-block:: python

    xgb_args = {'learning_rate': params['learning_rate'],
                'n_estimators': params['epochs'],
                'early_stopping_rounds': params['patience'],
                'max_depth': params['max_depth'],
                'min_child_weight': params['min_child_weight'],
                'subsample': params['subsample'],
                'colsample_bytree': params['colsample_bytree'],
                'gamma': params['gamma'],
                'lambda': params['lambda'],
                'alpha': params['alpha'],
                }
    
    model = xgb.XGBRegressor(objective='reg:squarederror', **xgb_args)
    model.fit(xtr, ytr, eval_set=[(xvl, yvl)])
    model.save_model(str(modelpath))
    del model

.. note::

    This will look very different depending on the implementation of your model. Key aspects to include are:

    * Using the improvelib parameters for :code:`params['learning_rate']`, :code:`params['epochs']`, and :code:`params['patience']` (see :doc:`api_train` for other parameters).
    * Unhardcoding other model-specific parameters that users may want to change (see :doc:`curating_tutorial_config` and :doc:`api_model` for more details).
    * Using the validation set for early stopping.
    * Saving the model with the modelpath.

**Load best model and compute predictions.**

.. code-block:: python

    # Load the best saved model (as determined based on val data)
    model = xgb.XGBRegressor()
    model.load_model(str(modelpath))

    # Compute predictions
    val_pred = model.predict(xvl)
    val_true = yvl.values.squeeze()

.. note::

    The implementation of this will vary depending on your model. The predictions and ground truth should be numpy arrays.

**Save raw predictions in dataframe.**
The predictions from the model on the validation data as well as the ground truth are saved with :doc:`api_utils_store_predictions_df`.

.. code-block:: python

    frm.store_predictions_df(
        y_true=val_true, 
        y_pred=val_pred, 
        stage="val",
        y_col_name=params["y_col_name"],
        output_dir=params["output_dir"],
        input_dir=params["input_dir"]
    )

.. note::

    The variables :code:`val_true` and :code:`val_pred` can be whatever you use in your script, but the rest should be the same.
    :code:`params['y_col_name']` can be changed in the configuration file.

**Compute performance scores.**
Performance scores on the validation data are calculated and saved with :doc:`api_utils_compute_performance_scores`.


.. code-block:: python

    val_scores = frm.compute_performance_scores(
        y_true=val_true, 
        y_pred=val_pred, 
        stage="val",
        metric_type=params["metric_type"],
        output_dir=params["output_dir"]
    )

.. note::

    The variables :code:`val_true` and :code:`val_pred` can be whatever you use in your script, but the rest should be the same.
    :code:`params['metric_type']` can be changed in the configuration file, if using a classification model instead of a regression model.

**Return the validation scores**

.. code-block:: python

    return val_scores


Training :code:`main()` and main guard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Similar to the :code:`main()` function in *preprocess* this is called upon script execution and gets the parameters, calls :code:`run()`, and records the time it takes for the model to run. Each line is explained below:

* The first line (:code:`cfg = DRPTrainConfig()`) initializes the configuration object for each script as appropriate.
* The second line initializes the parameters. Parameters set by command line (e.g. :code:`--input_dir /my/path/to/dir`) take precedence over the values in the config file, which take precedence over the default values provided by improvelib.
  
  * :code:`pathToModelDir` is the current path in the system. :code:`filepath` is already present in the template by :code:`filepath = Path(__file__).resolve().parent`.
  * :code:`default_config` is the default configuration file, as a string.
  * :code:`additional_definitions` is the list of model-specific parameters.
* The third line initializes the :doc:`api_utils_Timer`.
* The fourth line calls :code:`run()` with the parameters. As dicussed, :code:`run()` contains the model code.
* The fifth line ends the :doc:`api_utils_Timer` and saves the time to a JSON file in the output_dir.
* The last (optional) line prints a message indicating that the script is finished and ran successfully.


.. code-block:: python

    def main(args):
        cfg = DRPTrainConfig()
        params = cfg.initialize_parameters(pathToModelDir=filepath,
                                        default_config="xgboostdrp_params.ini",
                                        additional_definitions=train_params)
        timer_train = frm.Timer()    
        val_scores = run(params)
        timer_train.save_timer(dir_to_save=params["output_dir"], 
                            filename='runtime_train.json', 
                            extra_dict={"stage": "train"})
        print("\nFinished model training.")

.. note::

    You will need to change the name of :code:`default_config` to the one for your model, and the Config if you are using an application other than DRP.

The main guard below prevents unintended execution and should be present as is:

.. code-block:: python

    if __name__ == "__main__":
        main(sys.argv[1:])



