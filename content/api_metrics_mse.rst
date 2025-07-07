mse
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`mse`:funcelse:`(y_true, y_pred)`

Compute Mean Squared Error (MSE). Uses `sklearn.metrics.mean_square_error() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html>`_.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**mse** : float
  The computed MSE.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  mse_to_monitor = metr.mse(y_true, y_pred)


