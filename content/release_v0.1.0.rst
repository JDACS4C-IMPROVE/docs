v0.1.0-alpha
===============

To ensure compatibility with the IMPROVE software release `v0.1.0-alpha`, please update your curated model. Follow the instructions below and refer to the checklist at the bottom of the page. In addition, use models `GraphDRP <https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/develop>`_ and `LGBM <https://github.com/JDACS4C-IMPROVE/LGBM/tree/develop>`_ as examples. `TODO` make sure links for the models are correct!

Overview
---------
IMPROVE version `0.1.0-alpha` aims to expand the user base and encourage broader adoption of the software. This version features updates to accommodate various users and contributors, both internal and external, including those involved with the development of the core IMPROVE library, application-specific modules (such as drug response prediction and drug property prediction), benchmark datasets, and model contributions. Additionally, this version provides a simplified and more user-friendly interface, as demonstrated by intuitive help outputs, comprehensive READMEs, and documentation that facilitate easy switching between versions.

This version is now available on pypi for pip installation. `TODO`: update pypi AND link here

Parameters
------------
Parameters are detailed in :doc:`API`. Of note, the parameters for each step (i.e. preprocess, train, infer) are now separate.

Deprecated Parameters
^^^^^^^^^^^^^^^^^^^^^^^

- Preprocess

  - :code:`ml_data_outdir` is now :code:`output_dir`

- Train

  - :code:`train_ml_data_dir` is now :code:`input_dir`

  - :code:`val_ml_data_dir` is now :code:`input_dir`

  - :code:`model_outdir` is now :code:`output_dir`

  - :code:`y_data_preds_suffix`, :code:`json_scores_suffix`, and :code:`pred_col_name_suffix` are now hard-coded.

- Infer

  - :code:`test_ml_data_dir` is now :code:`input_data_dir`

  - :code:`model_dir` is now :code:`input_model_dir`

  - :code:`infer_outdir` is now :code:`output_dir`

  - :code:`y_data_preds_suffix`, :code:`json_scores_suffix`, and :code:`pred_col_name_suffix` are now hard-coded.

  - :code:`test_batch` is now :code:`infer_batch`.

Updating v0.0.3 curated models
---------------------------------

DRP Benchmarks v2 update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Benchmarks no longer have a triple header, and are flexibly loaded. Documentation will be fully updated after push to develop.

- Delete:

  .. code-block::

    import improvelib.applications.drug_response_prediction.drug_utils as drugs_utils
    import improvelib.applications.drug_response_prediction.omics_utils as omics_utils

- Example change for omics:

  .. code-block::

    omics_obj = omics_utils.OmicsLoader(params)
    ge = omics_obj.dfs['cancer_gene_expression.tsv']


  to

  .. code-block::

    ge = drp.get_cell_transcriptomics(file = params['cell_transcriptomic_file'], 
                                    benchmark_dir = params['input_dir'], 
                                    cell_column_name = params['canc_col_name'], 
                                    norm = params['cell_transcriptomic_transform'])
    ge = ge.reset_index()

- Example change for drug:

  .. code-block::

    drugs_obj = drugs_utils.DrugsLoader(params)
    md = drugs_obj.dfs['drug_mordred.tsv']


  to

  .. code-block::

    md = drp.get_drug_mordred(file = params['drug_mordred_file'], 
                benchmark_dir = params['input_dir'], 
                drug_column_name = params['drug_col_name'])

- Example change for response (change all instances):

  .. code-block::

    rsp_tr = drp.DrugResponseLoader(params,
                                    split_file=params["train_split_file"],
                                    verbose=False).dfs["response.tsv"]


  to

  .. code-block::

    rsp_tr = drp.get_response_data(split_file=params["train_split_file"], 
                                   benchmark_dir=params['input_dir'], 
                                   response_file=params['y_data_file'])





Updating Environment
^^^^^^^^^^^^^^^^^^^^^^

- Make an environment without candle lib. Since many packages are installed by candlelib, you may need to add other packages to your environment now.

- For now, set the PYTHONPATH as usual, this will be replaced with pip install shortly. You can also run this `bash script <https://github.com/JDACS4C-IMPROVE/GraphDRP/blob/framework-api/setup_improve.sh>`_ with :code:`source setup_improve.sh` to set up the environment. Running this script will clone IMPROVE repo, checkout the required branch, and set the PYTHONPATH (it will also download the csa benchmark dataset if it's not already downloaded).

- No environment variables need to be set, the IMPROVE_DATA_DIR directory is now set by command line with :code:`--input_dir your/path/to/csa_data/raw_data` or in the config.

Updating Import Statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- For initalizing parameters, there is a different import for each of the three scripts:

  - Preprocess

  .. code-block::

    from improvelib.applications.drug_response_prediction.config import DRPPreprocessConfig

  - Train

  .. code-block::

    from improvelib.applications.drug_response_prediction.config import DRPTrainConfig

  - Infer

  .. code-block::

    from improvelib.applications.drug_response_prediction.config import DRPInferConfig

- If your code uses str2bool, change the import to the following:

  .. code-block::

    from improvelib.utils import str2bool

- For other framework functions (previously from :code:`improve import framework as frm`) use:

  .. code-block::

    import improvelib.utils as frm

- For DataLoaders in Preprocess, use the following:

  - DrugsLoader

  .. code-block::

    import improvelib.applications.drug_response_prediction.drug_utils as drugs_utils

  - OmicsLoader

  .. code-block::

    import improvelib.applications.drug_response_prediction.omics_utils as omics_utils

  In the body of the code, references to :code:`drp.OmicsLoader()` and :code:`drp.DrugssLoader()` should be changed to :code:`omics_utils.OmicsLoader()` and :code:`drugs_utils.DrugsLoader()`, respectively.

  - DrugResponseLoader

  .. code-block:: 

    import improvelib.applications.drug_response_prediction.drp_utils as drp


Updating :code:`main()`
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Create the cfg object for the appropriate script: 

  - Preprocess

  .. code-block::

    cfg = DRPPreprocessConfig()

  - Train

  .. code-block::

    cfg = DRPTrainConfig()

  - Infer

  .. code-block::

    cfg = DRPInferConfig()

- Use relevant parameters for each of the model scripts as :code:`additional_definitions`. For example, in the infer script use :code:`additional_definitions = infer_params` instead of :code:`additional_definitions = preprocess_params + train_params + infer_params`

- Initialize parameters. Note that instead of :code:`default_model` now :code:`default_config` is used to specify the default configuration file.

  .. code-block::

    params = cfg.initialize_parameters(
        pathToModelDir=filepath,
        default_config="your_configuration_file.txt",
        additional_definitions=additional_definitions
    )

Updating IMPROVE Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Building paths is now done automatically. This line should be removed:

  .. code-block::

    params = frm.build_paths(params)

- Update the name of :code:`build_ml_data_name` to :code:`build_ml_data_file_name` in *preprocess*, *train*, and *infer* and update the arguments. Parameters are now explicitly passed. See example:

  .. code-block::

    frm.build_ml_data_file_name(data_format=params["data_format"], stage="test")

- Update the arguments in :code:`build_model_path` in *train* and *infer*. Parameters are now explicitly passed. Make sure :code:`model_dir` is :code:`params["output_dir"]` in *train* and :code:`params["input_model_dir"]` in *infer*. See example for *infer*:

  .. code-block::

    frm.build_model_path(model_file_name=params["model_file_name"], 
        model_file_format=params["model_file_format"], 
        model_dir=params["input_model_dir"])

- Update the arguments in :code:`save_stage_ydf` in *preprocess*. Parameters are now explicitly passed. See example:

  .. code-block::

    frm.save_stage_ydf(ydf=rsp, stage=stage, output_dir=params["output_dir"])

- Update the arguments in :code:`store_predictions_df` in *train* and *infer*. Parameters are now explicitly passed. See example:

  .. code-block::

    frm.store_predictions_df(
        y_true=val_true, 
        y_pred=val_pred, 
        stage="val",
        y_col_name=params["y_col_name"],
        output_dir=params["output_dir"]
    )

- Update the arguments in :code:`compute_performance_scores` in *train* and *infer*. Note "performance" is now spelled correctly. Parameters are now explicitly passed. The parameter :code:`metric_type` is set to regression by default and should not need to be changed for DRP models. See example:

  .. code-block::

    val_scores = frm.compute_performance_scores(
        y_true=val_true, 
        y_pred=val_pred, 
        stage="val",
        metric_type=params["metric_type"],
        output_dir=params["output_dir"]
    )

- In *infer*, :code:`compute_performance_scores` should only be called if :code:`calc_infer_scores` is :code:`True`. Wrap this in an :code:`if` statement. See example:

  .. code-block::

    if params["calc_infer_scores"]:
        test_scores = frm.compute_performance_scores(
            y_true=test_true, 
            y_pred=test_pred, 
            stage="test",
            metric_type=params["metric_type"],
            output_dir=params["output_dir"]
        )

- If your code uses :code:`compute_metrics` (usually in *train*), update the arguments. See example:

  .. code-block::

    compute_metrics(train_true, train_pred, params["metric_type"])

- The list :code:`metrics_list` is not required now and should be deleted. This list is hard-coded in :code:`compute_metrics` using :code:`metric_type`.

- In *infer*, make sure that :code:`run()` does not return test_scores, as this is now only generated if :code:`calc_infer_scores` is :code:`True`.



Updating References to Input and Output Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All scripts have a single :code:`output_dir`. Preprocess and train scripts have a single :code:`input_dir`. 
The infer script has two input directories, one for the saved model (:code:`input_model_dir`) and one for the ML data for the inference split (:code:`input_data_dir`). 
These are all set by default to the current working directory, but it is important to ensure that the correct input directories (i.e. model and data) are used in the code in the infer script so that workflows function correctly.

Updating Model-specific Parameter Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Model-specific parameter definitions should be in a file named :code:`model_params_def.py`. This file should contain three lists, one for each script (see below). These lists should be imported into the appropriate scripts (e.g. for *preprocess* use :code:`from model_params_def import preprocess_params`). For more information see :doc:`api_model`.

  .. code-block::

    from improvelib.utils import str2bool

    preprocess_params = []
    train_params = []
    infer_params = []


Updating the Default Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The new improvelib API now only reads the parameters in the relevant section as each script is run. 
If there are parameters that are used in more than one script (e.g. :code:`model_file_name` in both train and infer), these will have to be set in both the [Train] and [Infer] sections of the config.

Changes to Running Code
^^^^^^^^^^^^^^^^^^^^^^^^

- The path to csa_data can be set in the config or by command line. See example:

  .. code-block::

    python graphdrp_preprocess_improve.py --input_dir /your/path/to/csa_data/raw_data

- The default input and output directories are current working directory, but can be set in the config or by command line. Remember :code:`input_dir` should not be used in *infer*, use :code:`input_data_dir` and :code:`input_model_dir`. See example:

  .. code-block::

    python graphdrp_infer_improve.py --input_data_dir /your/path/to/data --input_model_dir /your/path/to/model --output_dir /your/path/to/results


- With the above changes to :code:`compute_performance_scores` in *Infer*, inference scores will not automatically be computed. Set :code:`calc_infer_scores = True` in the config or :code:`--calc_infer_scores True` on the command line.

If your model uses Supplemental Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There should be a shell script that downloads the data in the repo. Use :code:`input_supp_data_dir` to set the path to this directory.


INTERNAL USE - Curated Model Checklist - v0.1.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All of the following should be completed for the update of curated models from the legacy version (v0.0.3) to the latest version (v0.1.0).

- Tag the legacy version 

  - Make sure your model works with the legacy version (tagged v0.0.3-beta) of the IMPROVE lib. https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/v0.0.3-beta This means that all 3 model scripts run with the csa benchmark datasets.

  - Update the README.md to follow the same structure as much as possible in these examples. Make sure the install instructions refer to the v0.0.3-beta tag. Code should have :code:`setup_improve.sh` and :code:`download_csa.sh`.
    
    - https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/legacy-v0.0.3-beta

    - https://github.com/JDACS4C-IMPROVE/LGBM/tree/legacy-v0.0.3-beta

  - Create branch legacy-v0.0.3-beta. See examples:
  
    - https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/legacy-v0.0.3-beta

    - https://github.com/JDACS4C-IMPROVE/LGBM/tree/legacy-v0.0.3-beta

  - Create tag v0.0.3-beta with :code:`git tag v0.0.3-beta` then :code:`git push origin v0.0.3-beta`. See examples:

    - https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/v0.0.3-beta

    - https://github.com/JDACS4C-IMPROVE/LGBM/tree/v0.0.3-beta

- Change environment and code with the above instructions and confirm it runs successfully. This code should stay on the develop branch for now.

- Code should not use environmental variables.

- Code should not be dependent on candlelib.

- In infer, use :code:`input_model_dir` and :code:`input_data_dir` as appropriate so the CSA workflow functions properly.

- Parameters should be defined in model_params_def.py and these lists imported into the appropriate scripts (i.e. preprocess, train, infer).

- Default config should be named MODELNAME_params.txt.

- Update readme to include new instructions for set up of environment with pip installation of improvelib (and without candlelib).

- Update :code:`setup_improve.sh` to the correct improvelib branch (:code:`improve_branch="develop"`).

- Check the documentation page for your model (:doc:`app_drp_models`) and make sure it is accurate. Tell Natasha if it isn't.

- Send Natasha a list of your model-specific parameters (or a link to them).

- Tell Alex the model has been updated according to this page.
