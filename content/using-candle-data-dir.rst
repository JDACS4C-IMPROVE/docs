Tutorial CANDLE_DATA_DIR
==========

We can assume that CANDLE_DATA_DIR is an environment variable that contains a path
to the data directory. In the example below, I set it manually inside the code so
that the get_file function can be demonstrated.

.. code-block:: python

  import candle
  import os
  
  # Assumes CANDLE_DATA_DIR is an environment variable
  os.environ['CANDLE_DATA_DIR'] = '/tmp/data_dir'
  
  fname='raw_data.tar.gz'
  origin='ftp://ftp.mcs.anl.gov/pub/candle/public/improve/hidra/raw_data.tar.gz'
  
  # Download and unpack the data in CANDLE_DATA_DIR
  candle.file_utils.get_file(fname, origin)
  
  # Do it again to confirm it's not re-downloading
  candle.file_utils.get_file(fname, origin)

Generally, the input data is specified on the command line. For our purposes, it
needs to be set in the default_model.txt config file. The relevant CANDLE params
are:

.. code-block::

  [--train_data TRAIN_DATA]
  [--val_data VAL_DATA]
  [--test_data TEST_DATA]
  [--output_dir OUTPUT_DIR]
  [--data_url DATA_URL]
  
So the above code block for input data could look something like the following when using
the CANDLE initialize_parameters() method.

.. code-block:: python

  import candle
  import os
  
  # Assumes CANDLE_DATA_DIR is an environment variable
  os.environ['CANDLE_DATA_DIR'] = '/tmp/data_dir'
  
  data_url=gParameters['data_url']
  data_url=data_url+'/' if not data_url.endswith('/')
  
  train_data = gParameters['train_data']
  val_data = gParameters['val_data']
  test_data = gParameters['test_data']
  
  # Download and unpack the data in CANDLE_DATA_DIR
  candle.file_utils.get_file(train_data, data_url + train_data)
  candle.file_utils.get_file(val_data, data_url + val_data)
  candle.file_utils.get_file(test_data, data_url + test_data)

  
  # Do it again to confirm it's not re-downloading
  candle.file_utils.get_file(train_data, data_url + train_data)
  candle.file_utils.get_file(val_data, data_url + val_data)
  candle.file_utils.get_file(test_data, data_url + test_data)
