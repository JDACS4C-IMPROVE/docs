Curating a Model
===========================
NATASHA: finish this

Separating preprocess, train, and infer
----------------------------------------

IMPROVE divides deep learning models into three distinct steps NATASHA

Often community models are written as one or two scripts, encompassing multiple steps of the deep learning model.
In order to curate the model using IMPROVE, identify where the code should be divided into preprocess, train, and infer.
Preprocess should save processed machine learning (ML) data that has been split into training, validation, and testing datasets that can be directly ingested by the deep learning model in train.
You may have to implement saving of the best model in train, and loading of this model in infer. 
If the model does not already have functionality to save the split ML data, load the ML data, save the model, or load the model we recommend testing the implementation of this before moving forward.


Place model code in appropriate templates
-------------------------------------------
Templates available HERE - NATASHA.

- Model code should be placed in run(), which is called by main(), but run() can call other functions as needed.

- Any additional imports should be added as appropriate.

- IMPROVE provided parameters should be used as appropriate so that workflows function properly (e.g. HPO will use the provided :code:`epochs` parameter). Parameters can be retrieved from the params dictionary with the key like :code:`params[epochs]`

- All scripts have a single :code:`output_dir`. Preprocess and train scripts have a single :code:`input_dir`. The infer script has two input directories, one for the saved model (:code:`input_model_dir`) and one for the ML data for the inference split (:code:`input_data_dir`). These are all set by default to the current working directory, but it is important to ensure that the correct input directories (i.e. model and data) are used in the code in the infer script so that workflows function correctly.

- Other model-specific parameters not included as part of IMPROVE can be defined as described here: :doc:`api_model`.

- IMPROVE model files should be named as follows, where 'model' is the name of your model:
  - For preprocessing: :code:`model_preprocess_improve.py`
  - For training: :code:`model_train_improve.py`
  - For inference: :code:`model_infer_improve.py`

Create default configuration file
-----------------------------------
Template available HERE - NATASHA. See :doc:`api_config` for more information.

- The config file should contain all the relevant default values for the model's parameters.

- The config file should have three sections: :code:`[Preprocess]`, :code:`[Train]`, and :code:`[Infer]`. You may also include the section :code:`[GLOBAL]` and parameters set here will be seen by all three scripts.

- For parameters that are used in more than one script (e.g. :code:`model_file_name` in both train and infer), these will have to either 1) be set in both the [Train] and [Infer] sections of the config or 2) set in a section named [GLOBAL].

- The default configuation file should be named as follows, where 'model' is the name of your model: :code:`model_default_params.txt`.

Set up main() for your model
------------------------------
There are three required lines in main() for each script. This is the the main() for preprocess:

  .. code-block::
    def main(args):
        cfg = DRPPreprocessConfig()
        params = cfg.initialize_parameters(
            pathToModelDir=filepath,
            default_config="model_default_params.txt",
            default_model=None,
            additional_cli_section=None,
            additional_definitions=preprocess_params,
            required=None
        )
        output_dir = run(params)

- The first line (:code:`cfg = DRPPreprocessConfig()`) initializes the configuration object for each script as appropriate.

- The second line initializes the parameters. Parameters set by command line (e.g. :code:`--input_dir /my/path/to/dir`) take precedence over the values in the config file, which take precedence over the default values provided by improvelib.
  
  - :code:`pathToModelDir` is the current path in the system. :code:`filepath` is already present in the template by :code:`filepath = Path(__file__).resolve().parent`
  
  - :code:`default_config` is the default configuration file, as a string.

  - :code:`default_model`

  - :code:`additional_cli_section`

  - :code:`additional_definitions`

  - :code:`required`

- The third line calls run() with the parameters. As dicussed, run() contains the model code.

Ensure the model runs with original data
-----------------------------------------

- At this step in the curation process, we recommend running the code with the original data to ensure everything is implemented correctly and the model runs.

- Set up the environment with the packages needed by the model as you wish. Install the IMPROVE library with :code:`pip install improvelib`.

Implement IMPROVE benchmark data
-------------------------------------
To use IMPROVE benchmark Drug Response Prediction data, data loaders are provided.

- Download benchmark dataset. This should be in the input folder for preprocess

- Decide which dataset and split you would like to use and list these in the config file. The available datasets and splits are detailed here: :doc:`app_drp_benchmark`. 
These should be set with the following parameters in the default config in the :code:`[Preprocess]` section: :code:`train_split_file`, :code:`val_split_file`, and :code:`test_split_file`.
For example, to use CCLE split #0 add the following to the default config file:

  .. code-block::

    [Preprocess]
    train_split_file = CCLE_split_0_train.txt
    val_split_file = CCLE_split_0_val.txt
    test_split_file = CCLE_split_0_test.txt


- Build the paths for the benchmark dataset as follows (this is already present in the template):

  .. code-block::

    params = frm.build_paths(params)

- Create objects to load the features for drugs and cells (omics) loader as follows:

  .. code-block::

    drugs_obj = drugs.DrugsLoader(params)
    omics_obj = omics.OmicsLoader(params)

  You can retrieve the necessary features dataframe as follows:

  .. code-block::

    gene_expression = omics_obj.dfs['cancer_gene_expression.tsv']
    mordred = drugs_obj.dfs['drug_mordred.tsv']

  The available features are detailed here: :doc:`app_drp_benchmark`

- Create three objects to load the response data for the three different splits:

  .. code-block::

    response_train = drp.DrugResponseLoader(params, split_file=params["train_split_file"], verbose=False).dfs["response.tsv"]
    response_val = drp.DrugResponseLoader(params, split_file=params["val_split_file"], verbose=False).dfs["response.tsv"]
    response_test = drp.DrugResponseLoader(params, split_file=params["test_split_file"], verbose=False).dfs["response.tsv"]


- Preprocess the data and save in :code:`output_dir`. The implementation of this will depend on your specfic model. Keep in mind that the drug and omics loader provide features for all drugs and cell lines in the benchmark dataset.




