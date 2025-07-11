Curating a Model
===========================

Separating preprocess, train, and infer
----------------------------------------

IMPROVE divides deep learning models into three distinct steps:

#. Data **preprocessing** (converting raw data to machine learning (ML) data and splitting the data)

#. Model **training** and saving the best model (based on early stopping)

#. **Inference** (predicting with the model and saving raw predictions)

- Often community models are written as one or two scripts, encompassing multiple steps of the deep learning model. In order to curate the model using IMPROVE, identify where the code should be divided into preprocess, train, and infer.

- Preprocess should save processed machine learning (ML) data that has been split into training, validation, and testing datasets that can be directly ingested by the deep learning model in train.

- You may have to implement saving of the best model in train, and loading of this model in infer. 

- If the model does not already have functionality to save the split ML data, load the ML data, save the model, or load the model we recommend testing the implementation of this before moving forward.


Place model code in appropriate templates
-------------------------------------------
Templates available in :doc:`curating_templates` and on `GitHub <https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/develop/templates>`_.

- Model code should be placed in :code:`run()`, which is called by :code:`main()`, but :code:`run()` can call other functions as needed.

- Any additional imports should be added as appropriate.

- IMPROVE provided parameters should be used as appropriate so that workflows function properly (e.g. HPO will use the provided :code:`epochs` parameter). Parameters can be retrieved from the params dictionary with the key as so: :code:`params['epochs']`. IMPROVE provided parameters can be found here: :doc:`api_parameters`.

- All scripts have a single :code:`output_dir`. Preprocess and train scripts have a single :code:`input_dir`. The infer script has two input directories, one for the saved model (:code:`input_model_dir`) and one for the ML data for the inference split (:code:`input_data_dir`). These are all set by default to the current working directory, but it is important to ensure that the correct input directories (i.e. model and data) are used in the code in the infer script so that workflows function correctly.

- Other model-specific parameters not included as part of IMPROVE can be defined as described here: :doc:`api_model`. 

- IMPROVE model files should be named as follows, where '<MODEL>' is the name of your model:

  - For preprocessing: :code:`<MODEL>_preprocess_improve.py`

  - For training: :code:`<MODEL>_train_improve.py`

  - For inference: :code:`<MODEL>_infer_improve.py`

Create default configuration file
-----------------------------------
Templates available in :doc:`curating_templates` and on `GitHub <https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/develop/templates>`_. See :doc:`api_config` for more information.

- The config file should contain all the relevant default values for the model's parameters.

- The config file should have three sections: :code:`[Preprocess]`, :code:`[Train]`, and :code:`[Infer]`. 

- For parameters that are used in more than one script (e.g. :code:`model_file_name` in both train and infer), these will have to be set in both the :code:`[Train]` and :code:`[Infer]` sections of the config.

- The default configuation file should be named as follows, where '<MODEL>' is the name of your model: :code:`<MODEL>_params.txt`.

Set up :code:`main()` for your model
-----------------------------------------
There should be :code:`main()` for each script, which does three things: 1) gets the parameters 2) calls :code:`run()` and 3) records the time it takes for the model to run. This is the the :code:`main()` for preprocess in a DRP model:

  .. code-block::

      def main(args):
          cfg = DRPPreprocessConfig()
          params = cfg.initialize_parameters(pathToModelDir=filepath,
                                            default_config="<MODEL>_params.ini",
                                            additional_definitions=preprocess_params)
          timer_preprocess = frm.Timer()
          ml_data_outdir = run(params)
          timer_preprocess.save_timer(dir_to_save=params["output_dir"], 
                                      filename='runtime_preprocess.json', 
                                      extra_dict={"stage": "preprocess"})
          print("\nFinished data preprocessing.")
  
  .. note::

    Remember to use the Config that is appropriate for both your stage (preprocess/train/infer) and your application (DRP, Synergy, etc).

- The first line (:code:`cfg = DRPPreprocessConfig()`) initializes the configuration object for each script as appropriate.

- The second line initializes the parameters. Parameters set by command line (e.g. :code:`--input_dir /my/path/to/dir`) take precedence over the values in the config file, which take precedence over the default values provided by improvelib.
  
  - :code:`pathToModelDir` is the current path in the system. :code:`filepath` is already present in the template by :code:`filepath = Path(__file__).resolve().parent`.
  
  - :code:`default_config` is the default configuration file, as a string.

  - :code:`additional_definitions` is the list of model-specific parameters.

- The third line initializes the Timer.

- The fourth line calls :code:`run()` with the parameters. As dicussed, :code:`run()` contains the model code.

- The fifth line ends the Timer and saves the time to a JSON file in the output_dir.

- The last (optional) line prints a message indicating that the script is finished and ran successfully.

Ensure the model runs with original data
-----------------------------------------

- At this step in the curation process, we recommend running the code with the original data to ensure everything is implemented correctly and the model runs.

- If you have not already done so, set up the environment with the packages needed by the model as you wish. The IMPROVE library can be installed with :code:`pip install improvelib`.

Implement IMPROVE benchmark data
-------------------------------------
To use IMPROVE benchmark data, functions to load the data are provided.

- Download benchmark dataset. This should be in the input folder for preprocess

- Decide which dataset and split you would like to use and list these in the config file. The available datasets and splits are detailed here: :doc:`app_drp_benchmark`. These should be set with the following parameters in the default config in the :code:`[Preprocess]` section: :code:`train_split_file`, :code:`val_split_file`, and :code:`test_split_file`. For example, to use CCLE split #0 add the following to the default config file:

  .. code-block::

    [Preprocess]
    train_split_file = CCLE_split_0_train.txt
    val_split_file = CCLE_split_0_val.txt
    test_split_file = CCLE_split_0_test.txt

- Set the appropriate parameters for the feature types your would like to use. See here for available parameters. 
  See here for details on feature types. This should be the name of the file in the benchmark dataset.
  Alternately, a path to another file can be provided. See here for how to format these files correctly. The available features are detailed here: :doc:`app_drp_benchmark`.

  .. code-block::

    [Preprocess]
    cell_transcriptomics_file = cancer_gene_expression.tsv

- Load the features with :doc:`api_utils_get_x_data` like so:

  .. code-block::

    omics = drp.get_x_data(file = params['cell_transcriptomic_file'], 
                                        benchmark_dir = params['input_dir'], 
                                        column_name = params['canc_col_name'])


  Ensure that the column name is set to the correct parameter for your feature type and application. 
  The column name parameter names for each application can be found here: :doc:`api_preprocess`.

- Determine the transformations on the training set.

- Preprocess the train, val, and test datasets.

- Save the ML data.

- Save the y data.

- Create three objects to load the response data for the three different splits:

  .. code-block::

    response_train = drp.DrugResponseLoader(params, split_file=params["train_split_file"], verbose=False).dfs["response.tsv"]
    response_val = drp.DrugResponseLoader(params, split_file=params["val_split_file"], verbose=False).dfs["response.tsv"]
    response_test = drp.DrugResponseLoader(params, split_file=params["test_split_file"], verbose=False).dfs["response.tsv"]


- Preprocess the data and save in :code:`output_dir`. The implementation of this will depend on your specfic model. Keep in mind that the drug and omics loader provide features for all drugs and cell lines in the benchmark dataset.


If your model uses Supplemental Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There should be a shell script that downloads the data in the repo. Use :code:`input_supp_data_dir` to set the path to this directory.


