pearson
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`pearson`:funcelse:`(y_true, y_pred)`

Compute Pearson Correlation Coefficient (PCC). Uses scipy.stats.mstats.pearsonr().

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**pcc** : float
  The computed PCC.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  pcc_to_monitor = metr.pearson(y_true, y_pred)



