bacc
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`bacc`:funcelse:`(y_true, y_pred)`

Compute balanced accuracy. Uses sklearn.metrics.balanced_accuracy_score().

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**bacc** : float
  The computed balanced accuracy.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  bacc_to_monitor = metr.bacc(y_true, y_pred)



