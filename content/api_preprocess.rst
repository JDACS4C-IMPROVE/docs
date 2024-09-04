Preprocess API
=================================

IMPROVE general preprocess parameters
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

*x_data_dir*
  | **Type:** str
  | **Default:** "x_data"
  | **Help:** Dir name that contains the files with features data (x data).

*y_data_dir*
  | **Type:** str
  | **Default:** "y_data"
  | **Help:** Dir name that contains the files with target data (y data).

*splits_dir*
  | **Type:** str
  | **Default:** "splits"
  | **Help:** Dir name that contains files that store split ids of the y data file.

*train_split_file*
  | **Type:** str
  | **Default:** "fake"
  | **Help:** The path to the file that contains the train split ids (e.g., 'split_0_train_id', 'split_0_train_size_1024').

*val_split_file*
  | **Type:** str
  | **Default:** "fake"
  | **Help:** The path to the file that contains the val split ids (e.g., 'split_0_val_id').

*test_split_file*
  | **Type:** str
  | **Default:** "fake"
  | **Help:** The path to the file that contains the test split ids (e.g., 'split_0_test_id').




Drug Response Prediction preprocess parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*y_data_files*
  | **Type:** str
  | **Default:** "fake"
  | **Help:** List of files that contain the y (prediction variable) data. Example: [['response.tsv']].

*x_data_canc_files*
  | **Type:** str
  | **Default:** "fake"
  | **Help:** List of feature files including gene_system_identifer. Example: [['cancer_gene_expression.tsv', ['Gene_Symbol']]].

*x_data_drug_files*
  | **Type:** str
  | **Default:** "fake"
  | **Help:** List of feature files. Example: [['drug_SMILES.tsv']].

*canc_col_name*
  | **Type:** str
  | **Default:** "improve_sample_id"
  | **Help:** Column name in the y (response) data file that contains the cancer sample ids.

*drug_col_name*
  | **Type:** str
  | **Default:** "improve_chem_id"
  | **Help:** Column name in the y (response) data file that contains the drug ids.

*y_col_name*
  | **Type:** str
  | **Default:** "auc"
  | **Help:** Column name in the y data file (e.g., response.tsv), that represents the target variable that the model predicts.




