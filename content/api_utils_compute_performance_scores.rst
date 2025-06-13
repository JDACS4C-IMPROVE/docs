compute_performance_scores
-----------------------------------------

:funcelse:`improvelib.utils.`:funcname:`compute_performance_scores`:funcelse:`(ytrue, y_pred, stage, metric_type, output_dir, y_prob = None)`

Evaluate predictions according to specified metrics. Scores are stored in specified path and returned.

Used in *train* and *infer*.

.. container:: utilhead:
  
  Parameters:

**y_true** : np.array
  Array with ground truth values.

**y_pred** : np.array
  Array with model predictions.

**stage** : str 
  Specify if evaluation is with respect to val or test set ('val', or 'test').

**metric_type** : str 
  Either 'classification' or 'regression'.

**output_dir** : str
  The output directory where the results should be saved. Should be :code:`params['output_dir']`.

**y_prob** : np.array, optional
  Array with target scores from classification model, defaults to None.


.. container:: utilhead:
  
  Returns:

**scores** : dict
  Metrics evaluated and corresponding scores.

.. container:: utilhead:
  
  Example

To evaluate validation predictions in *train*:

.. code-block::
  
    val_scores = frm.compute_performance_scores(
        y_true=val_true, 
        y_pred=val_pred, 
        stage="val",
        metric_type=params["metric_type"],
        output_dir=params["output_dir"]
    )

When evaluating inference predictions in *infer*, best practice is to wrap the call to :code:`compute_performance_scores()` in 
:code:`if params["calc_infer_scores"]:` so that scores are only calculated when ground truth is available:

.. code-block::

    if params["calc_infer_scores"]:
        test_scores = frm.compute_performance_scores(
            y_true=test_true, 
            y_pred=test_pred, 
            stage="test",
            metric_type=params["metric_type"],
            output_dir=params["output_dir"]
        )
