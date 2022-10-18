Tutorial CANDLE_DATA_DIR
==========


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


