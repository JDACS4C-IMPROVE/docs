recall
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`recall`:funcelse:`(y_true, y_pred)`

Compute the recall. Uses `sklearn.metrics.recall_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html>`_.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**recall** : float
  The computed recall.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  recall_to_monitor = metr.recall(y_true, y_pred)



