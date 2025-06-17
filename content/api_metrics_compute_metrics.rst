compute_metrics
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`compute_metrics`:funcelse:`(y_true, y_pred, metric_type, y_prob = None)`

Compute the specified set of metrics.

If the :code:`metric_type` is :code:`'regression'` the metrics returned inclue: mse, rmse, pcc, scc, and r2.

If the :code:`metric_type` is :code:`'classification'` the metrics returned inclue: acc, recall, precision, f1, kappa, and bacc.

If the :code:`metric_type` is :code:`'classification'` and :code:`y_prob` is specfied, the metrics returned will also include: roc_auc and aupr.

Used in :doc:`api_utils_compute_performance_scores` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

**metric_type** : str
  Type of metrics to compute ('classification' or 'regression').

**y_prob** : np.ndarray, optional
  Target scores made by the classification model. Optional, defaults to None.


.. container:: utilhead:
  
  Returns:

**scores** : dict
  A dictionary of evaluated metrics.
  Keys for regression: ["mse", "rmse", "pcc", "scc", "r2"]
  Keys for classification without y_prob: ["acc", "recall", "precision", "f1", "kappa", "bacc"]
  Keys for classification with y_prob: ["acc", "recall", "precision", "f1", "kappa", "bacc", "roc_auc", "aupr"]

.. container:: utilhead:
  
  Raises:

**ValueError**
  If an invalid metric_type is provided.

.. container:: utilhead:
  
  Example

:code:`compute_metrics` is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use :code:`compute_metrics` to access scores, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  scores = metr.compute_metrics(y_true, y_pred, metric_type)
  mse_to_monitor = scores['mse']


