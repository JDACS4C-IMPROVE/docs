===============================================
Loading Data Using the candle.file_utils Module
===============================================

We saw in the previous example how to create a candle benchmark. Now we will use
the ``candle.file_utils`` methods to set up our input and output directories. Building
on the previous example, we will extend our Example model to load data. The general
functionality is that if the data exists in the data directory, use it, otherwise download
it and then use it.

----

.. code-block:: python

    # Set up input and output directory paths. These will always be
    # relative to os.environ['CANDLE_DATA_DIR'].
    data_dir = gParameters["data_dir"]
    output_dir = gParameters["output_dir"]
    # the following is incorrect and appends extra subdirectories to the path
    # data_dir, output_dir = directory_tree_from_parameters(gParameters)
    print('data_dir: {}\noutput_dir: {}'.format(data_dir, output_dir))

    # prints:
    # data_dir:   /tmp/improve_data_dir/Example/Data
    # putput_dir: /tmp/improve_data_dir/Example/Output/EXP000/RUN000

    # Get machine learning data
    download_filepath = candle.get_file(
        gParameters['train_data'],
        gParameters['data_url'] + "/" + gParameters['train_data']
        datadir = data_dir  # This puts the files in correct path
        cache_subdir = None  # This prevents get_file from creating another subdirectory
    )
    print('download_path: {}'.format(download_filepath))

    # prints:
    # download_path: /tmp/improve_data_dir/Example/Data/example.csv


----

The code above uses the environment variable CANDLE_DATA_DIR as the root to all input
and output paths.

Two new keyword = value pairs are needed in the default model file - ``example_default_model.txt``. These are
``data_url`` and ``train_data``. Additionally, I had to upload ``eample.csv`` to
https://ftp.mcs.anl.gov/pub/candle/public/improve/examples


.. code-block:: text
    
    # set location and name of training data
    data_url="https://ftp.mcs.anl.gov/pub/candle/public/improve/examples"
    train_data="abbreviation:.csv"

----

Putting this together into a running example looks like this:

.. code-block:: python

    import os
    import candle
    # from candle.file_utils import directory_tree_from_parameters
    # from candle.file_utils import get_file
    # from candle import Benchmark
    # from candle import finalize_parameters

    # set CANDLE_DATA_DIR env var. This is normally set externally.
    os.environ['CANDLE_DATA_DIR'] = '/tmp/improve_data_dir'

    # get the directory of this script, so that the default_model.txt
    # file can be found when the benchmark is instanciated.
    filepath = os.path.dirname(os.path.abspath(__file__))

    imp_bmk=candle.Benchmark(
        filepath=filepath,
        defmodel="example_default_model.txt",
        framework="tensorflow"
    )

    # Initialize parameters
    gParameters = candle.finalize_parameters(imp_bmk)

    # Set up input and output directory paths. These will always be
    # relative to os.environ['CANDLE_DATA_DIR'].
    # data_dir, output_dir = directory_tree_from_parameters(gParameters)
    print('data_dir: {}\noutput_dir: {}'.format(gParameters{"data_dir"], gParameters{"output_dir"]))

    # data_dir:   /tmp/improve_data_dir/Example/Data
    # putput_dir: /tmp/improve_data_dir/Example/Output/EXP000/RUN000

    # Get machine learning data
    download_filepath = candle.get_file(
        gParameters['train_data'],
        gParameters['data_url'] + "/" + gParameters['train_data']
        datadir = data_dir  # This puts the files in correct path
        cache_subdir = None  # This prevents get_file from creating another subdirectory
    )
    print('download_path: {}'.format(download_filepath))

This code produces the following output. The first output, model_name and Params come
from the call to finalize_parameters. The rest is print statements in the code above.

.. code-block:: text
    
 $ python ./example.py
 
 model name:  "Example"

 Params:
 {'ckpt_checksum': False,
 'ckpt_directory': './save',
 'ckpt_keep_limit': 1000000,
 'ckpt_keep_mode': 'linear',
 'ckpt_restart_mode': 'auto',
 'ckpt_save_best': True,
 'ckpt_save_best_metric': 'val_loss',
 'ckpt_save_interval': 0,
 'ckpt_save_weights_only': False,
 'ckpt_skip_epochs': 0,
 'data_dir': '/tmp/improve_data_dir/Example/Data',
 'data_type': <class 'numpy.float32'>,
 'data_url': 'https://ftp.mcs.anl.gov/pub/candle/public/improve/examples',
 'experiment_id': 'EXP000',
 'logfile': None,
 'model_name': 'Example',
 'output_dir': '/tmp/improve_data_dir/Example/Output/EXP000/RUN000',
 'profiling': False,
 'rng_seed': 7102,
 'run_id': 'RUN000',
 'shuffle': False,
 'timeout': -1,
 'train_bool': True,
 'train_data': 'example.csv',
 'verbose': False}

 data_dir: /tmp/improve_data_dir/Example/Data
 output_dir: /tmp/improve_data_dir/Example/Output/EXP000/RUN000
 download_path: /tmp/improve_data_dir/Example/Data/example.csv

The code for this example can be found at https://github.com/JDACS4C-IMPROVE/docs/tree/main/example_code
in the example.py and example_default_model.txt files.
