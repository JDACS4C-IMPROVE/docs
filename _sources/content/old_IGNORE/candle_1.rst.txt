===========================
Creating a CANDLE Benchmark
===========================

In it's most basic form, a CANDLE benchmark will know where to find
the default_model.txt file, read ``keyword=value`` pairs (parameters) from
the ``default_model.txt`` file, and set some other basic parameters. All that
is necessary for the example below is the keyword ``model_name`` in the
``default_model.txt`` file.

----

.. code-block:: python3

  import os
  import candle  # this imports all the public functions you need in the candle namespace
  # None of the following are needed
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

----

The model default params file contains:

.. code-block:: text

  [global]
  model_name="Example"


The output of the print statement inside the call to finalize_parameters"

Note that the data_dir and output_dir params are ALREADY set to the correct sub-paths from CANDLE_DATA_DIR

.. code-block:: text
  
  (base) Toms-MBP:example_code brettin$ python ./example.py 
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
