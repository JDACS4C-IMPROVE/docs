aupr
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`aupr`:funcelse:`(y_true, y_prob)`

Compute the Precision-Recall curve AUC. Uses `sklearn.metrics.precision_recall_curve() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html>`_ 
and `sklearn.metrics.auc() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html>`_.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_prob** : np.ndarray
  Target scores made by the model.

.. container:: utilhead:
  
  Returns:

**aupr** : float
  The computed Precision-Recall curve AUC.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  aupr_to_monitor = metr.aupr(y_true, y_pred)



