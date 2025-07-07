roc_auc
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`roc_auc`:funcelse:`(y_true, y_prob)`

Compute the Receiver Operating Characteristic AUC. Uses `sklearn.metrics.roc_auc_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html>`_.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_prob** : np.ndarray
  Target scores made by the model.

.. container:: utilhead:
  
  Returns:

**roc_auc** : float
  The computed Receiver Operating Characteristic AUC.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  roc_auc_to_monitor = metr.roc_auc(y_true, y_pred)



