Module improve.metrics
======================
Functionality for Computing Metrics in IMPROVE.

Functions
---------

    
`compute_metrics(y_true, y_pred, metrics)`
:   Compute the specified set of metrics.
    
    Parameters
    ----------
    y_true : numpy array
        True values to predict.
    y_pred : numpy array
        Prediction made by the model.
    metrics: python list
        List of metrics to compute.
    
    Returns
    -------
    eval: python dictionary
        A dictionary of evaluated metrics.

    
`mse(y_true, y_pred)`
:   Compute Mean Squared Error (MSE).
    
    Parameters
    ----------
    y_true : numpy array
        True values to predict.
    y_pred : numpy array
        Prediction made by the model.
    
    Returns
    -------
        float value corresponding to MSE. If several outputs, errors of all outputs are averaged with uniform weight.

    
`pearson(y_true, y_pred)`
:   Compute Pearson Correlation Coefficient (PCC).
    
    Parameters
    ----------
    y_true : numpy array
        True values to predict.
    y_pred : numpy array
        Prediction made by the model.
    
    Returns
    -------
        float value corresponding to PCC.

    
`r_square(y_true, y_pred)`
:   Compute R2 Coefficient.
    
    Parameters
    ----------
    y_true : numpy array
        True values to predict.
    y_pred : numpy array
        Prediction made by the model.
    
    Returns
    -------
        float value corresponding to R2. If several outputs, scores of all outputs are averaged with uniform weight.

    
`rmse(y_true, y_pred)`
:   Compute Root Mean Squared Error (RMSE).
    
    Parameters
    ----------
    y_true : numpy array
        True values to predict.
    y_pred : numpy array
        Prediction made by the model.
    
    Returns
    -------
        float value corresponding to RMSE. If several outputs, errors of all outputs are averaged with uniform weight.

    
`spearman(y_true, y_pred)`
:   Compute Spearman Correlation Coefficient (SCC).
    
    Parameters
    ----------
    y_true : numpy array
        True values to predict.
    y_pred : numpy array
        Prediction made by the model.
    
    Returns
    -------
        float value corresponding to SCC.

    
`str2Class(str)`
: