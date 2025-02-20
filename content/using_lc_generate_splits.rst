Learning Curve Split Generator
=================================

This repository contains scripts to generate data splits for learning curve
analysis (LCA) using drug response response data from various sources. The
scripts provide the ability to create progressive sizes of training sets,
allowing to analyze model performance as a function of the amount of training
data.

Requirements
-----------------

* Python 3.x
* Pandas
* NumPy

Installation and Setup
------------------------

You can install the required packages using :code:`pip`:

.. code-block:: bash

    pip install pandas numpy


Parameter Configuration
--------------------------

This workflow uses command line parameters are as follows:

* :code:`--data_file_path`: Full path to the input data file. For DRP models with benchmark data this should be '/csa_data/raw_data/y_data/response.tsv'
* :code:`--splits_dir`: Full path to the directory where the split files will be saved.
* :code:`--lc_sizes`: Number of subset sizes to generate (default: 10).
* :code:`--min_size`: The lower bound for the subset size (default: 128).
* :code:`--max_size`: The upper bound for the subset size (default: None, which sets it to the length of the dataset).
* :code:`--lc_step_scale`: Scale of progressive sampling of subset sizes in a learning curve (options: linear, log, log2,log10).


Usage
---------

Run :code:`generate_lc_split_files.py` to generates learning curve data splits based on the provided parameters:

.. code-block:: bash

    python generate_lc_split_files.py --data_file_path <path_to_data_file> \
        --splits_dir <path_to_splits_directory> \
        --lc_sizes <number_of_sizes> \
        --min_size <minimum_size> \
        --max_size <maximum_size> \
        --lc_step_scale <scale>

Example:

.. code-block:: bash

    python generate_lc_split_files.py \
        --data_file_path ../../../csa_data/raw_data/y_data/response.tsv \
        --splits_dir ../../../csa_data/raw_data/splits \
        --lc_sizes 10 \
        --min_size 1024 \
        --lc_step_scale log


Alternatively, run the bash script :code:`gen_lc_splits.sh`:

.. code-block:: bash

    bash gen_lc_splits.sh PATH_TO_DATA_FILE PATH_TO_SPLITD_DIR


The script invokes the Python script :code:`generate_lc_split_files.py` with parameters
such as the data file path, splits directory, LC sizes, min LC size, max LC size,
and the scaling method for size increments.

Output
--------

The output consists of multiple text files in the specified splits directory.
Each file contains indices of rows corresponding to the specified learning curve
sizes.
