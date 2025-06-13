Preprocess Parameters
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




Synergy preprocess parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*y_data_file*
  | **Type:** str
  | **Default:** "synergy.tsv"
  | **Help:** File that contains the y (prediction variable) data.

*cell_transcriptomic_file*
  | **Type:** str
  | **Default:** None
  | **Help:** "'cell_transcriptomics.tsv' for benchmark data or path to the transcriptomics data. None if not used."

*cell_transcriptomic_transform*
  | **Type:** str
  | **Default:** None
  | **Help:** "List of lists with the type of transformation and the option. Transformations will be performed in the order of the outer list. For example, [['normalize', 'zscale'], ['subset', 'L1000']] will first normalize the data with z-scaling and then subset to genes in L1000. For subset, a path to a text file with Entrez IDs separated by new lines can be given. None if not used."

*cell_cnv_file*
  | **Type:** str
  | **Default:** None
  | **Help:** "'cell_cnv_continuous.tsv' or 'cell_cnv_discretized.tsv' for benchmark data or path to the CNV data. None if not used."

*cell_cnv_transform*
  | **Type:** str
  | **Default:** None
  | **Help:** "List of lists with the type of transformation and the option. Transformations will be performed in the order of the outer list. For example, [['normalize', 'zscale'], ['subset', 'L1000']] will first normalize the data with z-scaling and then subset to genes in L1000. For subset, a path to a text file with Entrez IDs separated by new lines can be given. None if not used."

*cell_mutation_file*
  | **Type:** str
  | **Default:** None
  | **Help:** "'cell_mutation_delet.tsv' or 'cell_mutation_nonsynon.tsv' for benchmark data or path to the mutation data. None if not used."

*cell_mutation_transform*
  | **Type:** str
  | **Default:** None
  | **Help:** "List of lists with the type of transformation and the option. Transformations will be performed in the order of the outer list. For example, [['normalize', 'zscale'], ['subset', 'L1000']] will first normalize the data with z-scaling and then subset to genes in L1000. For subset, a path to a text file with Entrez IDs separated by new lines can be given. None if not used."

*drug_smiles_file*
  | **Type:** str
  | **Default:** None
  | **Help:** "'drug_smiles.tsv' or 'drug_smiles_canonical.tsv' for benchmark data or path to the SMILES data. None if not used."

*drug_mordred_file*
  | **Type:** str
  | **Default:** None
  | **Help:** "'drug_mordred.tsv' for benchmark data or path to the Mordred data. None if not used."

*drug_infomax_file*
  | **Type:** str
  | **Default:** None
  | **Help:** "'drug_infomax.tsv' for benchmark data or path to the Infomax data. None if not used."

*drug_ecfp_file*
  | **Type:** str
  | **Default:** None
  | **Help:** "'drug_ecfp[2/4/6]_nbits[256/1024].tsv' for benchmark data or path to the ECFP data. None if not used."

*cell_column_name*
  | **Type:** str
  | **Default:** "DepMapID"
  | **Help:** "Column name in the y (response) data file that contains the cancer sample IDs."

*drug_column_name*
  | **Type:** str
  | **Default:** "DrugID"
  | **Help:** "Column name in the y (response) data file that contains the cancer sample IDs."

*drug_1_column_name*
  | **Type:** str
  | **Default:** "DrugID_row"
  | **Help:** "Column name in the y (response) data file that contains the first drug IDs."

*drug_2_column_name*
  | **Type:** str
  | **Default:** "DrugID_col"
  | **Help:** "Column name in the y (response) data file that contains the second drug IDs."

*y_col_name*
  | **Type:** str
  | **Default:** "loewe"
  | **Help:** "Column name in the y data file (e.g., synergy.tsv), that represents the target variable that the model predicts. In synergy prediction problem it can be one of ['loewe', 'bliss', 'zip', 'hsa', 'smean', 'css']."
