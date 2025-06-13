build_ml_data_file_name
-----------------------------------------

:funcelse:`improvelib.utils.`:funcname:`build_ml_data_file_name`:funcelse:`(data_format, stage)`

Returns the name of the ML data file in the form of <stage>_data.<format>, e.g. train_data.pt.

Used in *preprocess*, *train*, and *infer*.

.. container:: utilhead:
  
  Parameters:

**data_format** : str
  Format to save the data (e.g. '.tsv'). Values with or without the period ('.') are acceptable.

**stage** : str 
  Stage of the data. Should be one of ['train', 'val', 'test.']


.. container:: utilhead:
  
  Returns:

**ml_data_file_name** : str
  Data file name

.. container:: utilhead:
  
  Example
  
Creates the appropriate file name to save the preprocessed data. For example, in *preprocess*:

.. code-block::
  
  data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage=stage)
  xdf.to_parquet(Path(params["output_dir"]) / data_fname)

Also insures that the appropriate files are loaded in *train* and *infer*. For example, to load training data:
   
.. code-block::

  train_data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="train")
  train_data = pd.read_parquet(Path(params["input_dir"]) / train_data_fname)

