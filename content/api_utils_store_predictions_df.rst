store_predictions_df
-----------------------------------------

:funcelse:`improvelib.utils.`:funcname:`store_predictions_df`:funcelse:`(y_pred, y_col_name, stage, output_dir, input_dir = None, y_true = None, round_decimals = 4)`

Save predictions with accompanying dataframe.

This allows to trace original data evaluated (e.g. drug and cell pairs) if corresponding dataframe is available (output from :code:`save_stage_ydf` in *preprocess*), in which case the whole structure as well as the model predictions are stored. 
If the dataframe is not available, only ground truth and model predictions are stored.

Used in *train* and *infer*.

.. container:: utilhead:
  
  Parameters:

**y_pred** : np.array
  Model predictions.

**y_col_name** : str
  Name of the column in the y_data predicted on (e.g. 'auc', 'ic50').

**stage** : str 
  Specify if evaluation is with respect to val or test set ('val', or 'test').

**output_dir** : str
  The output directory where the results should be saved. Should be :code:`params['output_dir']`.

**y_true** : np.array, optional
  Ground truth, if available.

**input_dir** : str, optional
  Directory where df with ground truth with metadata is stored.

**round_decimals** : int, optional
  Number of decimals in output (default is 4).


.. container:: utilhead:
  
  Returns:

None

.. container:: utilhead:
  
  Example

To store validation predictions in *train*:

.. code-block::
  
    frm.store_predictions_df(
        y_true=val_true, 
        y_pred=val_pred, 
        stage="val",
        y_col_name=params["y_col_name"],
        output_dir=params["output_dir"],
        input_dir=params["input_dir"]
    )

To store inference predictions in *infer*, when ground truth is available:

.. code-block::

    frm.store_predictions_df(
        y_true=test_true, 
        y_pred=test_pred, 
        stage="test",
        y_col_name=params["y_col_name"],
        output_dir=params["output_dir"],
        input_dir=params["input_data_dir"]
    )
