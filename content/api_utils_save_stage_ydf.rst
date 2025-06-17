save_stage_ydf
-----------------------------------------

:funcelse:`improvelib.utils.`:funcname:`save_stage_ydf`:funcelse:`(ydf, stage, output_dir)`

Saves a subset of y data samples. The "subset" refers to one of the three stages involved in developing ML models, 'train', 'val', or 'test'.
Saves the :code:`ydf` in the :code:`output_dir` with the file name <stage>_y_data.csv.

Used in *preprocess*.

.. container:: utilhead:
  
  Parameters:

**ydf** : pd.DataFrame
  DataFrame with y data samples for the specified stage. This should only include the samples that have feature data. 
  The minimum columns to be saved are the columns coorresponding to the IDs (e.g. for DRP, the cancer cell ID and drug ID)
  and the :code:`y_col_name` (e.g. for DRP, usually 'auc').

**stage** : str 
  Stage of the data. Should be one of ['train', 'val', 'test.']

**output_dir** : str
  The output directory where the preprocessed data is saved. Should be :code:`params['output_dir']`.


.. container:: utilhead:
  
  Returns:

None

.. container:: utilhead:
  
  Example

.. code-block::
  
  frm.save_stage_ydf(ydf, stage, params["output_dir"])

Add a bit about best practices to coordinate data.

