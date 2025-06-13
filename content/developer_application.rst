Creating an Application
==========================

IMPROVE is designed for any supervised learning models that use tabular data as input. 

Identify appropriate models
-----------------------------
You can create an IMPROVE application for any tabular data with a benchmark dataset. We suggest considering the following:

* Are there a decent number of publically available models that could be curated?
* Are there large datasets?
* Are there multiple datasets with similar input features and observation types? (Multiple datasets allows for :doc:`using_csa`).

Creating application-specific benchmark dataset
--------------------------------------------------

Data should all be tabular data (of any type), with more than one study in the benchmark data. IMPROVE was designed for multilevel data with multiple factors. 
For example, our DRP data has IDs for each factor - drug and cell. 
Each observation has an ID for both drug and cell, and each drug and cell have unique features.

* y_data: each row should contain IDs for each factor, followed by the observations.
* x_data: each row should contain the ID for a single factor, followed by the features -- each feature type should be in a different file. The x_data is prefixed with the name of the feature and then name of feature type (e.g. :code:`drug_SMILES.tsv`).
* splits: each split file should be named with the following convention: :code:`<dataset>_split_<n>_<train/val/test>.txt`, where n=[0:9]. Each line in the split file contains the index in the y_data to be used. We use an 80/20/20 (CHECK THIS) train/val/test ratio.

Data should be in a single directory with the following subdirectories:

.. code-block:: bash

    splits_dir/
    ├── x_data
    ├── y_data
    └── splits


Benchmark splits can be created with this script.

Creating a new application within improvelib
-----------------------------------------------
Within `improvelib/applications <https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/develop/improvelib/applications>`_, you should create a directory that will hold the application-related scripts.

This directory will be structured as so after the following steps:

.. code-block:: bash

    applications/
    ├── drug_response_prediction
    ├── synergy
    └── <YOUR_APPLICATION>
        ├── config.py
        ├── <YOUR_APPLICATION>_params_def.py
        ├── <YOUR_APPLICATION>_utils.py (optional)
        └── <YOUR_APPLICATION>_statics.py (optional)

.. warning::

    No commits are allowed on the develop branch of `IMPROVE <https://github.com/JDACS4C-IMPROVE/IMPROVE>`_. You must create a new branch.

Creating a application-specific configuration
-----------------------------------------------
To create an application-specific configuration, you will need to create two files: :code:`config.py` and :code:`<APPLICATION>_params_def.py`.

For :code:`config.py` you can use the template here and see an example here. You will need to: 

* change the class names to the name of your application
* change the group to reflect the name of your application
* change the import for the params_def to the location of the parameter definition file (see below)

For :code:`<APPLICATION>_params_def.py` you can use the template here and see an example here. You will need to:

* Fill in the dictionary with the 'name', 'type', 'default' and 'help' for each parameter. Be sure to make sure the parameters are in the list for all stages (train/val/test) that they will be used in.

.. warning::

    Use :code:`str2bool` as the type for boolean parameters or they will be interpreted as a string. Your file will need to include :code:`from improvelib.utils import str2bool`.

Ensure that the import statement in :code:`config.py` matches the location of the parameter definition file for your application and that the names of the parameter definition lists match.

Creating application-specific utilities and statics
----------------------------------------------------
Application-specific utilities and statics are optional, but can be helpful for many application types.

