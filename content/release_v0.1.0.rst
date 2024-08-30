v0.1.0-alpha
===============

.. For models previously curated as part of the IMPROVE project (version `v0.0.3-beta`), please follow the instructions below to update your curated model and see the checklist at the bottom of the page. 
To ensure compatibility with the IMPROVE software release `v0.1.0-alpha`, please update your curated model. Follow the instructions below and refer to the checklist at the bottom of the page. In addition, use models `GraphDRP <https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/develop>`_ and `LGBM <https://github.com/JDACS4C-IMPROVE/LGBM/tree/develop>`_ as examples. `TODO` make sure links for the models are correct!

Overview
---------
IMPROVE version `0.1.0-alpha` aims to expand the user base and encourage broader adoption the software. This version features updates to accommodate various users and contributors, both internal and external, including those involved with the development of the core IMPROVE library, application-specific modules (such as drug response prediction and drug property prediction), benchmark datasets, and model contributions. Additionally, this version provides a simplified and more user-friendly interface, as demonstrated by intuitive help outputs, comprehensive READMEs, and documentation that facilitate easy switching between versions.

This version is now available on pypi for pip installation. `TODO`: update pypi AND link here

Parameters
------------
Parameters are detailed in :doc:`API`. Of note, the parameters for each step (i.e. preprocess, train, infer) are now separate.

Depreciated Parameters
^^^^^^^^^^^^^^^^^^^^^^^

NATASHA: fill in

- Preprocess

  - :code:`ml_data_outdir` is now :code:`output_dir`

- Train

  - :code:`train_ml_data_dir` is now :code:`input_dir`

  - :code:`val_ml_data_dir` is now :code:`input_dir`

  - :code:`model_outdir` is now :code:`output_dir`

- Infer

  - :code:`test_ml_data_dir` is now :code:`input_data_dir`

  - :code:`model_dir` is now :code:`input_model_dir`

  - :code:`infer_outdir` is now :code:`output_dir`

Updating v0.0.3 curated models
---------------------------------

Updating Environment
^^^^^^^^^^^^^^^^^^^^^^

- Make an environment without candle lib. Since many packages are installed by candlelib, you may need to add other packages to your environment now.

- For now, set the PYTHONPATH as usual, this will be replaced with pip install shortly.

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

    import improvelib.applications.drug_response_prediction.drug_utils as drugs

  - OmicsLoader

  .. code-block::

    import improvelib.applications.drug_response_prediction.omics_utils as omics

  In the body of the code, references to :code:`drp.OmicsLoader()` should be changed to :code:`omics.OmicsLoader()`

  - DrugResponseLoader

  .. code-block:: 

    import improvelib.applications.drug_response_prediction.drp_utils as drp


Updating :code:`main()`
^^^^^^^^^^^^^^^^

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

- Use relevant parameters for each of the model scripts as :code:`additional_definitions`. 
For example, in the infer script use :code:`additional_definitions = infer_params` instead of :code:`additional_definitions = preprocess_params + train_params + infer_params`

- Initialize parameters. Note that instead of :code:`default_model` now :code:`default_config` is used to specify the default configuration file.

  .. code-block::

    params = cfg.initialize_parameters(
        pathToModelDir=filepath,
        default_config="your_configuration_file.txt",
        default_model=None,
        additional_cli_section=None,
        additional_definitions=additional_definitions,
        required=None
    )


If your model uses Supplemental Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There should be a shell script that downloads the data in the repo. Use :code:`input_supp_data_dir` to set the path to this directory.


Updating References to Input and Output Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All scripts have a single :code:`output_dir`. Preprocess and train scripts have a single :code:`input_dir`. 
The infer script has two input directories, one for the saved model (:code:`input_model_dir`) and one for the ML data for the inference split (:code:`input_data_dir`). 
These are all set by default to the current working directory, but it is important to ensure that the correct input directories (i.e. model and data) are used in the code in the infer script so that workflows function correctly.


Updating the Default Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The new improvelib API now only reads the parameters in the relevant section as each script is run. 
If there are parameters that are used in more than one script (e.g. :code:`model_file_name` in both train and infer), these will have to either 1) be set in both the [Train] and [Infer] sections of the config or 2) set in a section named [GLOBAL].


INTERNAL USE - Curated Model Checklist - v0.1.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All of the following should be completed for the update of curated models from the legacy version (v0.0.3) to the latest version (v0.1.0).

- Tag the legacy version 

  - Make sure your model works with the legacy version (tagged v0.0.3-beta) of the IMPROVE lib. https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/v0.0.3-beta This means that all 3 model scripts run with the csa benchmark datasets.

  - Update the README.md to follow the same structure as much as possible in these examples. Make sure the install instructions refer to the v0.0.3-beta tag.
    
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

- Default config should be named model_default_params.txt.

- Update readme to include new instructions for set up of environment with pip installation of improvelib (and without candlelib).

- Check the documentation page for your model (:doc:`app_drp_models`) and make sure it is accurate. Tell Natasha if it isn't.

- Send Natasha a list of your model-specific parameters (or a link to them).

- Tell Alex the model has been updated according to this page.