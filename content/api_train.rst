Train API
=================================

IMPROVE general training parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*log_level*
  | **Type:** str
  | **Default:** "DEBUG"
  | **Help:** Set log levels. Default is WARNING. Levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET.

*input_dir*
  | **Type:** str
  | **Default:** "./"
  | **Help:** Base directory for input data. All additional input pathes will be relative to the base input directory.

*output_dir*
  | **Type:** str
  | **Default:** "./"
  | **Help:** Base directory for output data. All additional relative output pathes will be placed into the base output directory.

*config_file*
  | **Type:** str
  | **Default:** None
  | **Help:** Config file in INI format.

*param_log_file*
  | **Type:** str
  | **Default:** "param_log_file.txt"
  | **Help:** Log of final parameters used for run. Saved in output_dir if file name, can be an absolute path.

*data_format*
  | **Type:** str
  | **Default:** ".parquet"
  | **Help:** File format to save the ML data file (e.g., '.pt', '.tfrecords').

*input_supp_data_dir*
  | **Type:** str
  | **Default:** None
  | **Help:** Dir containing supplementary data in addition to benchmark data (usually model-specific data).

*model_file_name*
  | **Type:** str
  | **Default:** "model"
  | **Help:** Filename to store trained model (str is w/o file_format).

*model_file_format*
  | **Type:** str
  | **Default:** ".pt"
  | **Help:** File format to save the trained model.

*epochs*
  | **Type:** int
  | **Default:** 7
  | **Help:** Training epochs.

*learning_rate*
  | **Type:** float
  | **Default:** 7
  | **Help:** Learning rate for the optimizer.

*batch_size*
  | **Type:** int
  | **Default:** 7
  | **Help:** Training batch size.

*val_batch*
  | **Type:** int
  | **Default:** 64
  | **Help:** Validation batch size.

*loss*
  | **Type:** str
  | **Default:** "mse"
  | **Help:** Prediction performance metric to monitor for early stopping during model training (e.g., 'mse', 'rmse').

*patience*
  | **Type:** int
  | **Default:** 20
  | **Help:** Iterations to wait for a validation metric to get worse before stop training.

*metric_type*
  | **Type:** str
  | **Default:** "regression"
  | **Help:** Metrics appropriate for given task. Options are 'regression' or 'classification'.


Drug Response Prediction training parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*y_col_name*
  | **Type:** str
  | **Default:** "auc"
  | **Help:** Column name in the y data file (e.g., response.tsv), that represents the target variable that the model predicts.