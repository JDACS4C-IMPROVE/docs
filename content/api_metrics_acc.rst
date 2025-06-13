acc
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`acc`:funcelse:`(y_true, y_pred)`

Compute accuracy. Uses sklearn.metrics.accuracy_score().

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**acc** : float
  The computed accuracy.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  acc_to_monitor = metr.acc(y_true, y_pred)



