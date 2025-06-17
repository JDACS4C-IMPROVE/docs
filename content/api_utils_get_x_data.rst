get_x_data
-----------------------------------------

:funcelse:`improvelib.applications.drug_response_prediction.drp_utils.`:funcname:`get_x_data`:funcelse:`(file, benchmark_dir, column_name, dtype=None)`

Gets x data. Sets index to ID. Sets dtype if specified.

Used in *preprocess*.

.. container:: utilhead:
  
  Parameters:

**file** : str, Path
  Name of x data file if in benchmark data, otherwise path to x data file.

**benchmark_dir** : str, Path
  Path to benchmark data directory.

**column_name** : str
  Name of ID column for x data.

**dtype** : str, optional
  The dtype to enforce for this x data (default: None).

.. container:: utilhead:
  
  Returns:

**data** : pd.DataFrame
  DataFrame of x data (with dtype if specified), index set to ID.

.. container:: utilhead:
  
  Example

To load transcriptomics data:

.. code-block::

    omics = drp.get_x_data(file = params['cell_transcriptomic_file'], 
                                        benchmark_dir = params['input_dir'], 
                                        column_name = params['canc_col_name'])

To load mordred data:

.. code-block::

    drugs = drp.get_x_data(file = params['drug_mordred_file'], 
                    benchmark_dir = params['input_dir'], 
                    column_name = params['drug_col_name'])


