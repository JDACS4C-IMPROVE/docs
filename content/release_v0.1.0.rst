v0.1.0-alpha
===============

For models previously curated as part of the IMPROVE project, please follow the instructions below to update your curated model and see the following checklist: 

.. toctree::
   :titlesonly:

   v0.1.0 Checklist <release_v0.1.0_checklist>

Overview
---------
This release TAKE TEXT FROM ALEX

Also now available on pypi for pip installation.

Parameters
------------
Parameters are detailed in :doc:`API`. Of note, the parameters for each step (i.e. preprocess, train, infer) are now separate.

Depreciated Parameters
^^^^^^^^^^^^^^^^^^^^^^^

NATASHA: fill in

- Preprocess
  - :code:`ml_data_outdir` is now

- Train
  - :code:`train_ml_data_dir`
  - :code:`val_ml_data_dir`
  - :code:`model_outdir`

- Infer
  - :code:`test_ml_data_dir`
  - :code:`model_dir`
  - :code:`infer_outdir`

Updating v0.0.3 curated models
---------------------------------

Updating Environment
^^^^^^^^^^^^^^^^^^^^^^

- Make an environment without candle lib. Since many packages are installed by candlelib, you may need to add other packages to your environment now.

- For now, set the PYTHONPATH as usual, this will be replaced with pip install shortly.

- No environment variables need to be set, the csa_data directory can be set by command line (see below)

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


Updating main()
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

Updating References to Input and Output Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File Structure (input outputs dirs now, include CSA requirements for infer)

Updating the Default Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The new improvelib API now only reads the parameters in the relevant section as each script is run. 
If there are parameters that are used in more than one script (e.g. :code:`model_file_name` in both train and infer), these will have to either 1) be set in both the [Train] and [Infer] sections of the config or 2) set in a section named [GLOBAL].
