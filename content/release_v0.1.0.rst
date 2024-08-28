v0.1.0-alpha
===============

For models previously curated as part of the IMPROVE project, please see the following checklist: 

.. toctree::
   :titlesonly:

   v0.1.0 Checklist <release_v0.1.0_checklist>

Overview
---------
This release TAKE TEXT FROM ALEX

Parameters
------------
Parameters are detailed in :doc:`API`. Of note, the parameters for each step (i.e. preprocess, train, infer) are now separate.

Depreciated Parameters
^^^^^^^^^^^^^^^^^^^^^^^

NATASHA: fill in

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

  .. code-block:: python

    from improvelib.applications.drug_response_prediction.config import DRPPreprocessConfig

  - Train

  .. code-block:: python

    from improvelib.applications.drug_response_prediction.config import DRPTrainConfig

  - Infer

  .. code-block:: python

    from improvelib.applications.drug_response_prediction.config import DRPInferConfig

- If your code uses str2bool, change the import to the following:

  .. code-block:: python

    from improvelib.utils import str2bool

- For other framework functions (previously from :code:`improve import framework as frm`) use:

  .. code-block:: python

    import improvelib.utils as frm

- For DataLoaders in Preprocess, use the following:

  - DrugsLoader

  .. code-block:: python

    import improvelib.applications.drug_response_prediction.drug_utils as drugs

  - OmicsLoader

  .. code-block:: python

    import improvelib.applications.drug_response_prediction.omics_utils as omics

  In the body of the code, references to :code:`drp.OmicsLoader()` should be changed to :code:`omics.OmicsLoader()`

  - DrugResponseLoader

  .. code-block:: python

    import improvelib.applications.drug_response_prediction.drp_utils as drp


Updating main()
^^^^^^^^^^^^^^^^

- Create the cfg object for the appropriate script: 

  - Preprocess

  .. code-block:: python

    cfg = DRPPreprocessConfig()

  - Train

  .. code-block:: python

    cfg = DRPTrainConfig()

  - Infer

  .. code-block:: python

    cfg = DRPInferConfig()

- Initialize parameters. Note that instead of :code:`default_model` now :code:`default_config` is used to specify the default configuration file.

  .. code-block:: python

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

Things have to be in each section now