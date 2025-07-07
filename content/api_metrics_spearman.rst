spearman
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`spearman`:funcelse:`(y_true, y_pred)`

Compute Spearman Correlation Coefficient (SCC). Uses `scipy.stats.mstats.spearmanr() <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.spearmanr.html>`_.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**scc** : float
  The computed SCC.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  scc_to_monitor = metr.spearman(y_true, y_pred)



