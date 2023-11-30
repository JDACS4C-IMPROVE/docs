Module python.improve_utils
===========================

Functions
---------

    
`get_common_samples(df1: pandas.core.frame.DataFrame, df2: pandas.core.frame.DataFrame, ref_col: str) ‑> Tuple[pandas.core.frame.DataFrame, pandas.core.frame.DataFrame]`
:   Args:
        df1, df2 (pd.DataFrame): dataframes
        ref_col (str): the ref column to find the common values
    
    Returns:
        df1, df2
    
    Example:
        TODO

    
`get_data_splits(src_raw_data_dir: str, splitdir_name: str, split_file_name: str, rsp_df: pandas.core.frame.DataFrame)`
:   IMPROVE-specific func.
    Read smiles data.
    src_raw_data_dir : data dir where the raw DRP data is stored

    
`get_subset_df(df: pandas.core.frame.DataFrame, ids: list) ‑> pandas.core.frame.DataFrame`
:   Get a subset of the input dataframe based on row ids.

    
`load_copy_number_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns copy number data.
    
    Args:
        gene_system_identifier (str or list of str): gene identifier system to use
            options: "Entrez", "Gene_Symbol", "Ensembl", "all", or any list
                     combination of ["Entrez", "Gene_Symbol", "Ensembl"]
    
    Returns:
        pd.DataFrame: dataframe with the omic data

    
`load_discretized_copy_number_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns discretized copy number data.
    
    Args:
        gene_system_identifier (str or list of str): gene identifier system to use
            options: "Entrez", "Gene_Symbol", "Ensembl", "all", or any list
                     combination of ["Entrez", "Gene_Symbol", "Ensembl"]
    
    Returns:
        pd.DataFrame: dataframe with the omic data

    
`load_dna_methylation_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns methylation data.
    
    Args:
        gene_system_identifier (str or list of str): gene identifier system to use
            options: "Entrez", "Gene_Symbol", "Ensembl", "all", or any list
                     combination of ["Entrez", "Gene_Symbol", "Ensembl"]
    
    Returns:
        pd.DataFrame: dataframe with the omic data

    
`load_gene_expression_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns gene expression data.
    
    Args:
        gene_system_identifier (str or list of str): gene identifier system to use
            options: "Entrez", "Gene_Symbol", "Ensembl", "all", or any list
                     combination of ["Entrez", "Gene_Symbol", "Ensembl"]
    
    Returns:
        pd.DataFrame: dataframe with the omic data

    
`load_mirna_expression_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   

    
`load_mordred_descriptor_data(sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Return Mordred descriptors data.

    
`load_morgan_fingerprint_data(sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Return Morgan fingerprints data.

    
`load_mutation_count_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns mutation count data.
    
    Args:
        gene_system_identifier (str or list of str): gene identifier system to use
            options: "Entrez", "Gene_Symbol", "Ensembl", "all", or any list
                     combination of ["Entrez", "Gene_Symbol", "Ensembl"]
    
    Returns:
        pd.DataFrame: dataframe with the omic data

    
`load_mutation_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   

    
`load_rppa_data(gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   

    
`load_single_drug_response_data(source: str, split: Optional[int] = None, split_type: Union[str, List[str], ForwardRef(None)] = None, y_col_name: str = 'auc', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns datarame with cancer ids, drug ids, and drug response values. Samples
    from the original drug response file are filtered based on the specified
    sources.
    
    Args:
        source (str or list of str): DRP source name (str) or multiple sources (list of strings)
        split(int or None): split id (int), None (load all samples)
        split_type (str or None): one of the following: 'train', 'val', 'test'
        y_col_name (str): name of drug response measure/score (e.g., AUC, IC50)
    
    Returns:
        pd.Dataframe: dataframe that contains drug response values

    
`load_single_drug_response_data_v2(source: str, split_file_name: Union[str, List[str], ForwardRef(None)] = None, y_col_name: str = 'auc', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns datarame with cancer ids, drug ids, and drug response values. Samples
    from the original drug response file are filtered based on the specified
    sources.
    
    Args:
        source (str or list of str): DRP source name (str) or multiple sources (list of strings)
        split(int or None): split id (int), None (load all samples)
        split_type (str or None): one of the following: 'train', 'val', 'test'
        y_col_name (str): name of drug response measure/score (e.g., AUC, IC50)
    
    Returns:
        pd.Dataframe: dataframe that contains drug response values

    
`load_smiles_data(sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   IMPROVE-specific func.
    Read smiles data.
    src_raw_data_dir : data dir where the raw DRP data is stored

    
`load_split_file(source: str, split: Optional[int] = None, split_type: Union[str, List[str], ForwardRef(None)] = None) ‑> List[int]`
:   Args:
        source (str): DRP source name (str)
    
    Returns:
        ids (list): list of id integers

    
`load_split_ids(split_file_name: Union[str, List[str]]) ‑> List[int]`
:   Returns list of integers, representing the rows in the response dataset.
    Args:
        split_file_name (str or list of str): splits file name or list of file names
    
    Returns:
        list: list of integers representing the ids

    
`mse(y, f)`
:   

    
`pearson(y, f)`
:   

    
`r_square(y_true, y_pred)`
:   

    
`read_df(fpath: str, sep: str = ',')`
:   IMPROVE-specific func.
    Load a dataframe. Supports csv and parquet files.
    sep : the sepator in the csv file

    
`rmse(y, f)`
:   

    
`save_preds(df: pandas.core.frame.DataFrame, y_col_name: str, outpath: Union[str, pathlib.PosixPath], round_decimals: int = 4) ‑> None`
:   Save model predictions.
    This function throws errors if the dataframe does not include the expected
    columns: canc_col_name, drug_col_name, y_col_name, y_col_name + "_pred"
    
    Args:
        df (pd.DataFrame): df with model predictions
        y_col_name (str): drug response col name (e.g., IC50, AUC)
        outpath (str or PosixPath): outdir to save the model predictions df
        round (int): round response values 
        
    Returns:
        None

    
`set_col_names_in_multilevel_dataframe(df: pandas.core.frame.DataFrame, level_map: dict, gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol') ‑> pandas.core.frame.DataFrame`
:   Util function that supports loading of the omic data files.
    Returns the input dataframe with the multi-level column names renamed as
    specified by the gene_system_identifier arg.
    
    Args:
        df (pd.DataFrame): omics dataframe
        level_map (dict): encodes the column level and the corresponding identifier systems
        gene_system_identifier (str or list of str): gene identifier system to use
            options: "Entrez", "Gene_Symbol", "Ensembl", "all", or any list
                     combination of ["Entrez", "Gene_Symbol", "Ensembl"]
    
    Returns:
        pd.DataFrame: the input dataframe with the specified multi-level column names

    
`spearman(y, f)`
: