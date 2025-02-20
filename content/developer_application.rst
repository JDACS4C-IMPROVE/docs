Creating an Application
==========================

IMPROVE is designed for supervised learning models that use tabular data as input.

Identify appropriate models
-----------------------------


Creating application-specific benchmark dataset
--------------------------------------------------

Data should all be tabular data (of any type), with more than one study in the benchmark data. IMPROVE was designed for multilevel data with multiple factors. 
For example, our DRP data has IDs for each factor - drug and cell. 
Each observation has an ID for both drug and cell, and each drug and cell have unique features.

y_data: each row should contain IDs for each factor, followed by the observations.
x_data: each row should contain the ID for a single factor, followed by the features -- each feature type should be in a different file
x_data is prefixed with the name of the feature and then name of feature type (e.g. :code:`drug_SMILES.tsv`).
splits: each split file should be named with the following convention: :code:`<dataset>_split_<n>_<train/val/test>.txt`, where n=[0:9]. Each line in the split file contains the index in the y_data to be used. We use an 80/20/20 (CHECK THIS) train/val/test ratio.

Example

Data should be in a single directory with the following subdirectories:

.. code-block:: bash

    splits_dir/
    ├── x_data
    ├── y_data
    └── splits


Benchmark splits can be created with this script.

Creating a application-specific configuration
-----------------------------------------------



Creating application-specific utilities
-----------------------------------------------