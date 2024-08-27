Preprocess API
=================================

IMPROVE general preprocess parameters

.. list-table:: 
   :widths: 25 25 25 50
   :header-rows: 1

   * - Parameter
     - Type
     - Default
     - Help
   * - log_level
     - str
     - "DEBUG"
     - 
   * - input_dir
     - str
     - "./"
     - 
   * - output_dir
     - str
     - "./"
     - 
   * - config_file
     - str
     - None
     - 
   * - param_log_file
     - str
     - "param_log_file.txt"
     - 
   * - data_format
     - str
     - ".parquet"
     - 



Drug Response Prediction preprocess parameters

.. list-table:: 
   :widths: 25 25 25 50
   :header-rows: 1

   * - Parameter
     - Type
     - Default
     - Help
   * - y_data_files
     - str
     - "fake"
     - List of files that contain the y (prediction variable) data. Example: [['response.tsv']]
   * - x_data_canc_files
     - str
     - "fake"
     - List of feature files including gene_system_identifer. Example: [['cancer_gene_expression.tsv', ['Gene_Symbol']]] 
   * - x_data_drug_files
     - str
     - "fake"
     - List of feature files. Example: [['drug_SMILES.tsv']]
   * - canc_col_name
     - str
     - "improve_sample_id"
     - Column name in the y (response) data file that contains the cancer sample ids.
   * - drug_col_name"
     - str
     - "improve_chem_id"
     - Column name in the y (response) data file that contains the drug ids.
   * - y_col_name
     - str
     - "auc"
     - Column name in the y data file (e.g., response.tsv), that represents the target variable that the model predicts.
   * - y_data_suffix
     - str
     - "y_data"
     - [Dep] Suffix to compose file name for storing true y dataframe.



