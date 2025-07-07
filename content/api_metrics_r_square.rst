r_square
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`r_square`:funcelse:`(y_true, y_pred)`

Compute R2 Coefficient. Uses `sklearn.metrics.r2_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html>`_.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**r2** : float
  The computed R2.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  r2_to_monitor = metr.r_square(y_true, y_pred)



