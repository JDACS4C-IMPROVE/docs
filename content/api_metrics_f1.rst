f1
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`f1`:funcelse:`(y_true, y_pred)`

Compute the F1 score. Uses `sklearn.metrics.f1_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html>`_.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**f1** : float
  The computed F1 score.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  f1_to_monitor = metr.f1(y_true, y_pred)



