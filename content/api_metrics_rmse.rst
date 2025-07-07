rmse
-----------------------------------------

:funcelse:`improvelib.metrics.`:funcname:`rmse`:funcelse:`(y_true, y_pred)`

Compute Root Mean Squared Error (RMSE). Uses `sklearn.metrics.root_mean_square_error() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html>`_ for sklearn v1.4.0 and higher, 
`sklearn.metrics.mean_square_error(squared=False) <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html>`_ for sklearn v0.22.0 up to v1.4.0 and the square root of `sklearn.metrics.mean_square_error() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html>`_ for lower versions.

Used in :doc:`api_metrics_compute_metrics` and can be used directly.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.ndarray
  Ground truth.

**y_pred** : np.ndarray
  Predictions made by the model.

.. container:: utilhead:
  
  Returns:

**rmse** : float
  The computed RMSE.

.. container:: utilhead:
  
  Example

This function is called by :doc:`api_metrics_compute_metrics` which is called by :doc:`api_utils_compute_performance_scores`, which also saves the scores.

You can use this function directly, for example during model training like so:

.. code-block::
  
  import improvelib.metrics as metr
  rmse_to_monitor = metr.rmse(y_true, y_pred)



