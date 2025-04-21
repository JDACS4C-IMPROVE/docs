Utility Functions
====================

IMPROVE general utility functions
-----------------------------------------

The following functions are part of improvelib and should be used to standardize aspects of the workflow.

.. topic:: build_ml_data_file_name

    Returns the name of the ML data file in the form of <stage>_data.<format>, e.g. train_data.pt.

    Used in *preprocess*, *train*, and *infer*.

    Args:
        data_format (str)
        
        stage (str)
    
    Returns:
        str: data file name

.. topic:: build_model_path

    Returns the path to save/load the trained model.

    Used in *train* and *infer*.

    Args:
        model_file_name (str): Name of model file

        model_file_format (str): Type of file for model (e.g. '.pt')

        model dir (Path or str): Directory path to save the model

    Returns:
        pathlib.Path: path to model

.. topic:: save_stage_ydf

    Save a subset of y data samples (rows of the input dataframe).
    The "subset" refers to one of the three stages involved in developing ML models, including: "train", "val", or "test".

    Used in *preprocess*.

    Args:
        ydf (pd.DataFrame): Dataframe with y data samples

        stage (str) : Either 'train', 'val', or 'test'

        output_dir (str): Directory to save to

    Returns:
        None

.. topic:: store_predictions_df

    Save predictions with accompanying dataframe.

    This allows to trace original data evaluated (e.g. drug and cell pairs) if corresponding dataframe is available(output from :code:`save_stage_ydf` in *preprocess*), in which case the whole structure as well as the model predictions are stored. 
    If the dataframe is not available, only ground truth and model predictions are stored.
    
    Used in *train* and *infer*.

    Args:
        y_pred (np.array): Model predictions

        y_col_name (str): Name of the column in the y_data predicted on (e.g. 'auc', 'ic50')

        stage (str): Specify if evaluation is with respect to val or test set ('val', or 'test')

        output_dir (str): Directory to write results

        y_true (Optional: np.array): Ground truth 

        input_dir (Optional: str): Directory where df with ground truth with metadata is stored

        round_decimals (Optional: int): Number of decimals in output (default is 4)

.. topic:: compute_performance_scores

    Evaluate predictions according to specified metrics. Scores are stored in specified path and returned.

    Used in *train* and *infer*.

    Args:
        y_true (np.array): Array with ground truth values

        y_pred (np.array): Array with model predictions

        stage (str): Specify if evaluation is with respect to val or test set ('val', or 'test')

        metric_type (str): Either 'classification' or 'regression'

        output_dir (str): Directory to write results

    Returns:
        dict: metrics evaluated and corresponding scores


IMPROVE Drug Response Prediction Utility Functions
-------------------------------------------------------

Drug Utility Functions (drug_utils)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. topic:: class DrugsLoader

    Class to load and manage drug data.

    Args:
        params (Dict): IMPROVE parameters.

        sep (str): Character separator in the loaded files (e.g., "\t" for TSV files).

        verbose (bool): Whether to print detailed loading information.

    Attributes:
        smiles_fname (str): Filename for SMILES data.

        mordred_fname (str): Filename for Mordred descriptors.

        ecfp4_512bit_fname (str): Filename for ECFP4 512-bit data.

        known_file_names (List[str]): List of known drug data filenames.

        params (Dict): Configuration parameters for loading data.

        sep (str): Separator used in data files.

        inp (List): List of input drug data files.

        drug_col_name (str): Column name for drug identifiers.

        x_data_path (str): Path to the directory containing drug data files.

        dfs (Dict[str, pd.DataFrame]): Dictionary to store loaded dataframes, keyed by filename.

        verbose (bool): Flag to control verbosity of output.

        inp_fnames (List[str]): List of input filenames extracted from inp.

    Example:
        .. code-block::

            from improve import drug_resp_pred as drp
            params = {
                "x_data_drug_files": "[['drug_SMILES.tsv'], ['drug_mordred.tsv'], ['drug_ecfp4_nbits512.tsv']]",
                "drug_col_name": "DrugID",
                "x_data_path": "/path/to/drug/data"
            }
            drugs_loader = drp.DrugsLoader(params)
            print(drugs_loader)
            print(dir(drugs_loader))
            smi = drugs_loader["drug_SMILES.tsv"]



Omics Utility Functions (omics_utils)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. topic:: class OmicsLoader

    Class aggregates methods to load omics data.

    Args:
        params (Dict): IMPROVE parameters.

        sep (str): Character separator in the loaded files (e.g., "\t" for TSV files).

        verbose (bool): Flag for verbosity.

    Attributes:
        copy_number_fname (str): Filename for copy number data.

        discretized_copy_number_fname (str): Filename for discretized copy number data.

        dna_methylation_fname (str): Filename for DNA methylation data.

        gene_expression_fname (str): Filename for gene expression data.

        miRNA_expression_fname (str): Filename for miRNA expression data.

        mutation_count_fname (str): Filename for mutation count data.

        mutation_long_format_fname (str): Filename for mutation data in long format.

        mutation_fname (str): Filename for mutation data in parquet format.

        rppa_fname (str): Filename for RPPA data.

        known_file_names (List[str]): List of known omics data filenames.

        params (Dict): Configuration parameters for loading data.

        sep (str): Separator used in data files.

        inp (List): List of input omics data files.

        x_data_path (str): Path to the directory containing omics data files.

        canc_col_name (str): Column name for indexing in the data files.

        dfs (Dict[str, pd.DataFrame]): Dictionary to store loaded dataframes, keyed by filename.

        verbose (bool): Flag to control verbosity of output.

        inp_fnames (List[str]): List of input filenames extracted from inp.

    Example:
        .. code-block::

            from improve import drug_resp_pred as drp
            params = {
                "x_data_canc_files": "[['cancer_gene_expression.tsv', 'Gene_Symbol'], "
                                    "['cancer_copy_number.tsv', 'Entrez']]",
                "canc_col_name": "SampleID",
                "x_data_path": "/path/to/omics/data"
            }
            omics_loader = drp.OmicsLoader(params)
            print(omics_loader)
            print(dir(omics_loader))
            gene_expression_data = omics_loader["cancer_gene_expression.tsv"]



Response Utility Functions (drp_utils)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. topic:: get_common_samples

    Search for common data in a reference column and retain only those rows.

    Args:
        df1 (pd.DataFrame): First dataframe.

        df2 (pd.DataFrame): Second dataframe.

        ref_col (str): The reference column to find the common values.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Tuple of DataFrames after filtering for common data.

.. topic:: common_elements

    Return a list of elements that the provided lists have in common.

    Args:
        list1 (List): One list.

        list2 (List): Another list.

        verbose (bool): Flag for verbosity. If True, info about computations is displayed. Default is False.

    Returns:
        List: List of common elements.

.. topic:: class DrugResponseLoader

    Class for loading monotherapy drug response data.

    Args:
        params (Dict): IMPROVE parameters.

        split_file (str): File name that contains the split ids (rows).

        sep (str): Character separator in the loaded files (e.g., "\t" for TSV files).

        verbose (bool): Flag for verbosity. Default is True.

    Attributes:
        response_fname (str): Default response file name.

        known_file_names (List[str]): List of known file names.

        params (Dict): Parameters for loading data.

        sep (str): Separator used in data files.

        inp (List): Parsed input data files.

        y_col_name (str): Column name for the target variable.

        canc_col_name (str): Column name for cancer sample identifiers.

        drug_col_name (str): Column name for drug identifiers.

        y_data_path (str): Path to the directory containing y data files.

        split_fpath (Path): Path to the file containing split identifiers.

        dfs (Dict[str, pd.DataFrame]): Dictionary to store loaded dataframes.

        verbose (bool): Verbosity flag.

    Example:
        .. code-block::

            from improve import drug_resp_pred as drp
            drp_loader = drp.DrugResponseLoader(params)
            print(drp_loader)
            print(dir(drp_loader))
            rsp = drp_loader["response.tsv"]


IMPROVE Synergy utility functions
-----------------------------------------

The following functions are part of improvelib and should be used to standardize aspects of the workflow.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.

.. topic:: get_all_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        train_split_file (Union[str, Path, list of str, list of Path]): Name of train split file if in benchmark data, otherwise path to train split file. Can be a list of str or Path.
        
        val_split_file (Union[str, Path, list of str, list of Path]): Name of val split file if in benchmark data, otherwise path to val split file. Can be a list of str or Path.
        
        test_split_file (Union[str, Path, list of str, list of Path]): Name of test split file if in benchmark data, otherwise path to test split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for all splits with col 'split' denoting split type ('train', 'val', or 'test').


.. topic:: get_cell_transcriptomics

    Gets cell transcriptomics. Sets index to cell ID and sets dtype to float64.

    Used in *preprocess*.

    Args:
        file (Union[str, Path]): Name of cell transcriptomics file if in benchmark data, otherwise path to cell transcriptomics file. 
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        cell_column_name (str): Name of ID column for cell data.
        
        norm (list): Normalization to perform on this data.
    
    Returns:
        pd.DataFrame: cell transcriptomics data (with normalization if specified), index set to cell ID.

.. topic:: get_cell_cnv

    Gets cell Copy Number Variation. Sets index to cell ID and sets dtype to float64.

    Used in *preprocess*.

    Args:
        file (Union[str, Path]): Name of cell Copy Number Variation file if in benchmark data, otherwise path to cell Copy Number Variation file. 
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        cell_column_name (str): Name of ID column for cell data.
        
        norm (list): Normalization to perform on this data.
    
    Returns:
        pd.DataFrame: cell Copy Number Variation data (with normalization if specified), index set to cell ID.

.. topic:: get_cell_mutations

    Gets cell mutation. Sets index to cell ID and sets dtype to float64.

    Used in *preprocess*.

    Args:
        file (Union[str, Path]): Name of cell mutation file if in benchmark data, otherwise path to cell mutation file. 
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        cell_column_name (str): Name of ID column for cell data.
        
        norm (list): Normalization to perform on this data.
    
    Returns:
        pd.DataFrame: cell mutation data (with normalization if specified), index set to cell ID.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        response_file (str): Name of response file (default: 'synergy.tsv')
        
        sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.

.. topic:: get_response_data

    Gets response data for a given split file.

    Used in *preprocess*.

    Args:
        * split_file (Union[str, Path, list of str, list of Path]): Name of split file if in benchmark data, otherwise path to split file. Can be a list of str or Path.
        
        * benchmark_dir (Union[str, Path]): Path to benchmark data directory.
        
        * response_file (str): Name of response file (default: 'synergy.tsv')
        
        * sep (str): Separator for response file (default: '\t').
    
    Returns:
        pd.DataFrame: Response dataframe for given split.