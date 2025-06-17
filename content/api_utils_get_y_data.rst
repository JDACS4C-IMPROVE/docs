get_y_data
-----------------------------------------

:funcelse:`improvelib.applications.drug_response_prediction.drp_utils.`:funcname:`get_y_data`:funcelse:`(split_file, benchmark_dir, y_data_file, split_id='split_id', sep='\t')`

Gets y data for a given split file.

Used in *preprocess*.

.. container:: utilhead:
  
  Parameters:

**split_file** : str, Path, List of str, List of Path
  Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.

**benchmark_dir** : str, Path
  Path to benchmark data directory.

**y_data_file** : str
  Name of y data file.

**split_id** : str, optional
  Name of column containing the split ID (default: 'split_id').

**sep** : str, optional
  Separator for response file (default: '\t').

.. container:: utilhead:
  
  Returns:

**df** : pd.DataFrame
  Response dataframe for given split.

.. container:: utilhead:
  
  Example

To load y data for the training set:

.. code-block::

    response_train = drp.get_y_data(split_file=params["train_split_file"], 
                                   benchmark_dir=params['input_dir'], 
                                   y_data_file=params['y_data_file'])

Loading y data to preprocess data for all three stages is typically by looping through the stages as follows:

.. code-block::

    stages = {"train": params["train_split_file"],
              "val": params["val_split_file"],
              "test": params["test_split_file"]}

    for stage, split_file in stages.items():

Within this loop, y data for each stage can be loaded with:

.. code-block::

    response_stage = drp.get_y_data(split_file=split_file, 
                        benchmark_dir=params['input_dir'], 
                        y_data_file=params['y_data_file'])
