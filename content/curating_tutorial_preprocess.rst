Preprocessing Script Example with XGBoost for DRP
==========================================================

This script `xgboostdrp_preprocess_improve.py <https://github.com/JDACS4C-IMPROVE/XGBoost-DRP/blob/develop/xgboostdrp_preprocess_improve.py>`_. preprocesses raw benchmark data and generates ML data files for the XGBoost prediction model.
The naming convention for the preprocessing script is `<MODEL>_preprocess_improve.py`. 

**Inputs:**
The benchmark data directory is set with :code:`params['input_dir']`. Alternate data can be provided, see :doc:`using_external_data`.
Models can use any of the provided benchmark studies/splits by changing the value of :code:`param['train_split_file']`, :code:`param['val_split_file']`, and :code:`param['test_split_file']`.

* **y_data**: The file with the factor IDs and observation values.

  * response.tsv

* **x_data**: Files with the factor IDs and features for each feature type.

  * cancer_gene_expression.tsv
  * drug_mordred.tsv

* **splits** List of split_nums to use from the response file. 

  * CCLE_split_0_train.txt
  * CCLE_split_0_val.txt
  * CCLE_split_0_test.txt

.. Note::

    The x_data used by your model may be different. Use the appropriate parameter(s) for your application to specify which data 
    is used by your model (e.g. :code:`params['cell_transcriptomic_file']`). 
    Information about the parameters can be found here: :doc:`api_preprocess`.
    

**Outputs:**
All the outputs from the *preprocess* script are saved in :code:`params[output_dir]`. The processed x and y data are used as inputs to the ML/DL prediction model in the *train* and *infer* scripts.

* **Processed x data**: Processed feature data for XGBoost model.

  * train_data.parquet
  * val_data.parquet
  * test_data.parquet

* **Tranformation dictionaries**: Dictionaries that contain the transformations as determined by the test set.

  * drug_transform.json
  * omics_transform.json

* **Processed y data**: File with true y values and IDs (additional metadata is acceptable).

  * train_y_data.csv
  * val_y_data.csv
  * test_y_data.csv
 
* **Parameter log**: Log of the :code:`params` dictionary.

  * param_log_file.txt

* **Timer log**: Log of the :code:`Timer` dictionary.

  * runtime_preprocess.json


.. Note::

    The y data files should be generated with the standardized names with :doc:`api_utils_save_stage_ydf` regardless of the model being curated.
    The format of the x data files can differ depending on the model and is specified with :code:`params['data_format']`.
    In addition to the data files mentioned above, the preprocessing script can be used to save additional utility data required in *train* and *infer*.


Preprocessing Imports
^^^^^^^^^^^^^^^^^^^^^^
This section consists of five basic components:

* **Import basic functionality**: sys, Path, etc.
* **Import core improvelib functionality**: we import this as 'frm' for historical reasons.
* **Import application-specific functionality**: this will need to be changed if curating a model for another application.
* **Import model-specific functionality**: at minimum this should included the model parameter definitions, but can also include other packages your model requires (Polars, numpy, etc).
* **Get file path**: filepath is used by the Config and this line should be present as is.

.. code-block:: python

    import sys
    from pathlib import Path
    import pandas as pd

    # Core improvelib imports
    import improvelib.utils as frm
    # Application-specific (DRP) imports
    from improvelib.applications.drug_response_prediction.config import DRPPreprocessConfig
    import improvelib.applications.drug_response_prediction.drp_utils as drp

    # Model-specifc imports
    from model_params_def import preprocess_params

    filepath = Path(__file__).resolve().parent

.. note::

    You may need to add imports if your model requires other packages and you may need to change the application-specific imports if using another application.

Preprocessing :code:`run()`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function contains the bulk of the code: it loads the benchmark data, checks the feature data, determines the tranformation 
values on the training set, preprocesses the data for the train, val, and test sets, and saves the preprocessed ML data. 
Here we walk through the function.

**Define the function.** The parameter dictionary must be passed to this function:

.. code-block:: python

    def run(params):


**Load feature data.** We load the feature data with :doc:`api_utils_get_x_data`.

.. code-block:: python

  print("Load omics data.")
  omics = frm.get_x_data(file = params['cell_transcriptomic_file'], 
                         benchmark_dir = params['input_dir'], 
                         column_name = params['canc_col_name'])

  print("Load drug data.")
  drugs = frm.get_x_data(file = params['drug_mordred_file'], 
                         benchmark_dir = params['input_dir'], 
                         column_name = params['drug_col_name'])


**Validity check of feature representations.** This is not needed for this model. 

.. note:: 

  If you are using any features for which some of the information may not be valid, here you will want to check the validity of the features
  and remove them from the feature dataframe if needed. We highly recommend this for any preprocess that uses RDKit, as converting to :code:`mol`
  often returns None or an error. Another scenario is if drug target information is used and not all drugs have target information.

**Determine preprocessing on training data.** Tranformation include subsetting to certain features, imputing any missing values, or 
scaling the data. For example, in this XGBoost model we have set :code:`cell_transcriptomic_transform = [['subset', 'LINCS_SYMBOL'], ['scale', 'std']]`
which will first subset the genes to only those in the LINCS1000 set, and then apply the standard scaler to the data. 
See :doc:`api_utils_determine_transform` for more information on all the available transformations.

First we load the y (response) data for the training split with :doc:`api_utils_get_y_data` and remove any NaN values for the data we are using (in this case AUC).

.. code-block:: python

    print("Load train response data.")
    response_train = frm.get_y_data(split_file=params["train_split_file"], 
                                   benchmark_dir=params['input_dir'], 
                                   y_data_file=params['y_data_file'])
    response_train = response_train.dropna(subset=[params['y_col_name']])

Next we find the y data that has matching features for all the feature types we are using (for XGBoost we are using 
transcriptomics for cell line features and Mordred descriptors for drug features) with :doc:`api_utils_get_y_data_with_features`.
Then we subset to the features that are present in this training y data set with :doc:`api_utils_get_features_in_y_data`.

.. code-block:: python
    
    print("Find intersection of training data.")
    response_train = frm.get_y_data_with_features(response_train, omics, params['canc_col_name'])
    response_train = frm.get_y_data_with_features(response_train, drugs, params['drug_col_name'])
    omics_train = frm.get_features_in_y_data(omics, response_train, params['canc_col_name'])
    drugs_train = frm.get_features_in_y_data(drugs, response_train, params['drug_col_name'])

Then we determine the transformation values on the features that are in the training set for the transformations specified in the parameters
(here :code:`params['cell_transcriptomic_transform']` and :code:`params['cell_mordred_transform']`) using :doc:`api_utils_determine_transform`.
This saves the values of the transformation to a dictionary that will be used later to transform each (train, val, test) dataset.

.. code-block:: python

    print("Determine transformations.")
    frm.determine_transform(omics_train, 'omics_transform', params['cell_transcriptomic_transform'], params['output_dir'])
    frm.determine_transform(drugs_train, 'drugs_transform', params['drug_mordred_transform'], params['output_dir'])

**Construct ML data for every stage (train, val, test).** We highly recommend doing the preprocessing of the data in a 
loop to ensure the preprocessing is the same for all three stage datasets. We set up the loop as follows:

.. code-block:: python

   stages = {"train": params["train_split_file"],
              "val": params["val_split_file"],
              "test": params["test_split_file"]}

   for stage, split_file in stages.items():
       print(f"Prepare data for stage {stage}.")

Inside this loop we find intersection of the data, transform the data, merge the data, and save the data. 
First we load the response data, remove NaN values for our data, and find the intersection of the data with :doc:`api_utils_get_y_data`, 
:doc:`api_utils_get_y_data_with_features`, and :doc:`api_utils_get_features_in_y_data`:

.. code-block:: python

        print(f"Find intersection of {stage} data.")
        response_stage = frm.get_y_data(split_file=split_file, 
                                benchmark_dir=params['input_dir'], 
                                y_data_file=params['y_data_file'])
        response_stage = response_stage.dropna(subset=[params['y_col_name']])
        response_stage = frm.get_y_data_with_features(response_stage, omics, params['canc_col_name'])
        response_stage = frm.get_y_data_with_features(response_stage, drugs, params['drug_col_name'])
        omics_stage = frm.get_features_in_y_data(omics, response_stage, params['canc_col_name'])
        drugs_stage = frm.get_features_in_y_data(drugs, response_stage, params['drug_col_name'])

Next we tranform the data using the dictionary we created above with :doc:`api_utils_transform_data`:

.. code-block:: python

        print(f"Transform {stage} data.")
        omics_stage = frm.transform_data(omics_stage, 'omics_transform', params['output_dir'])
        drugs_stage = frm.transform_data(drugs_stage, 'drugs_transform', params['output_dir'])

Then we assign the response columns to y_df_cols so we can pull out these columns to save later. 
We use pandas.merge to merge all the features. Shuffling the data is optional, depending on your model.

.. code-block:: python

        print(f"Merge {stage} data")
        y_df_cols = response_stage.columns.tolist()
        data = response_stage.merge(omics_stage, on=params["canc_col_name"], how="inner")
        data = data.merge(drugs_stage, on=params["drug_col_name"], how="inner")
        data = data.sample(frac=1.0).reset_index(drop=True) # shuffle

Finally we save the x data and the y data. The x data file name is determined with :doc:`api_utils_build_ml_data_file_name`.
The y data is saved with :doc:`api_utils_save_stage_ydf`. In this implementation, we add the y values (:code:`params['y_col_name']`) 
to the x data file, and we will isolate this column in the *train* script, but this can be omitted and the saved y dataframe can be used.

.. code-block:: python

        print(f"Save {stage} data")
        xdf = data.drop(columns=y_df_cols)
        xdf[params['y_col_name']] = data[params['y_col_name']]
        data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage=stage)
        xdf.to_parquet(Path(params["output_dir"]) / data_fname)
        # [Req] Save y dataframe for the current stage
        ydf = data[y_df_cols]
        frm.save_stage_ydf(ydf, stage, params["output_dir"])

.. note::

  There is flexibility in how this is implemented, but it is essential that the y data is saved with the IDs and ground truth, 
  in the same order as the features to ensure the predictions and scores are saved accurately.

**Return the output directory.**

.. code-block:: python

   return params["output_dir"]s


Preprocessing :code:`main()` and main guard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :code:`main()` function is called upon script execution and gets the parameters, calls :code:`run()`, and records the time it takes for the model to run. Each line is explained below:

* The first line (:code:`cfg = DRPPreprocessConfig()`) initializes the configuration object for each script as appropriate.
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
        cfg = DRPPreprocessConfig()
        params = cfg.initialize_parameters(pathToModelDir=filepath,
                                           default_config="xgboostdrp_params.ini",
                                           additional_definitions=preprocess_params)
        timer_preprocess = frm.Timer()
        ml_data_outdir = run(params)
        timer_preprocess.save_timer(dir_to_save=params["output_dir"], 
                                    filename='runtime_preprocess.json', 
                                    extra_dict={"stage": "preprocess"})
    print("\nFinished data preprocessing.")

.. note::

    You will need to change the name of :code:`default_config` to the one for your model, and the Config if you are using an application other than DRP.

The main guard below prevents unintended execution and should be present as is:

.. code-block:: python

    if __name__ == "__main__":
        main(sys.argv[1:])
