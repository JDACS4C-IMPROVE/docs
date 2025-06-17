Infer Parameters
=================================

IMPROVE general inference parameters
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

*infer_batch*
  | **Type:** int
  | **Default:** 64
  | **Help:** Inference batch size.

*model_file_name*
  | **Type:** str
  | **Default:** "model"
  | **Help:** Filename to store trained model (str is w/o file_format).

*model_file_format*
  | **Type:** str
  | **Default:** ".pt"
  | **Help:** File format to save the trained model.

*loss*
  | **Type:** str
  | **Default:** "mse"
  | **Help:** Prediction performance metric to monitor for early stopping during model training (e.g., 'mse', 'rmse').

*input_data_dir*
  | **Type:** str
  | **Default:** "./"
  | **Help:** Dir where data for inference is stored.

*input_model_dir*
  | **Type:** str
  | **Default:** "./"
  | **Help:** Dir where model is stored.

*calc_infer_scores*
  | **Type:** str2bool
  | **Default:** False
  | **Help:** Calculate scores in the inference script (this is optional; should not be required during inference).

*metric_type*
  | **Type:** str
  | **Default:** "regression"
  | **Help:** Metrics appropriate for given task. Options are 'regression' or 'classification'.


Drug Response Prediction inference parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*y_col_name*
  | **Type:** str
  | **Default:** "auc"
  | **Help:** Column name in the y data file (e.g., response.tsv), that represents the target variable that the model predicts.

Synergy inference parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*y_col_name*
  | **Type:** str
  | **Default:** "loewe"
  | **Help:** "Column name in the y data file (e.g., synergy.tsv), that represents the target variable that the model predicts. In synergy prediction problem it can be one of ['loewe', 'bliss', 'zip', 'hsa', 'smean', 'css']."
