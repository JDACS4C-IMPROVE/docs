precision
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`precision`:funcelse:`(y_true, y_pred)`

Compute the precision. Uses sklearn.metrics.precision_score().

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**precision** : float
  The computed precision.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  precision_to_monitor = metr.precision(y_true, y_pred)



