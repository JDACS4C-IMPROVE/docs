Module improve.dataloader
=========================
Functionality for IMPROVE data handling.

Functions
---------

    
`common_elements(list1: List, list2: List, verbose: bool = True) ‑> List`
:   Return list of elements that the provided lists have in common.
    
    Args:
        list1: One list.
        list2: Another list.
        verbose: Flag for verbosity. If True, info about computations is displayed. Default: True.
    
    Returns:
        List of common elements.

    
`get_common_samples(df1: pandas.core.frame.DataFrame, df2: pandas.core.frame.DataFrame, ref_col: str) ‑> Tuple[pandas.core.frame.DataFrame, pandas.core.frame.DataFrame]`
:   Search for common data in reference column and retain only .
    
    Args:
        df1, df2 (pd.DataFrame): dataframes
        ref_col (str): the ref column to find the common values
    
    Returns:
        df1, df2 after filtering for common data.
    
    Example:
        Before:
    
        df1:
        col1    ref_col     col3            col4
        CCLE    ACH-000956      Drug_749        0.7153
        CCLE    ACH-000325      Drug_1326       0.9579
        CCLE    ACH-000475      Drug_490        0.213
    
        df2:
        ref_col     col2                col3                col4
        ACH-000956  3.5619370596224327  0.0976107966264223      4.888499735514123
        ACH-000179  5.202025844609336   3.5046203924035524      3.5058909297299574
        ACH-000325  6.016139702655253   0.6040713236688608      0.0285691521967709
    
        After:
    
        df1:
        col1    ref_col     col3            col4
        CCLE    ACH-000956      Drug_749        0.7153
        CCLE    ACH-000325      Drug_1326       0.9579
    
        df2:
        ref_col     col2                col3                col4
        ACH-000956  3.5619370596224327  0.0976107966264223      4.888499735514123
        ACH-000325  6.016139702655253   0.6040713236688608      0.0285691521967709

    
`load_cell_data(fname: Union[pathlib.Path, str], canc_col_name='improve_sample_id', gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol', sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns data frame with specified cell line data.
    
    Args:
        fname: Name of, or Path to, file for reading cell data.
        canc_col_name: Column name that contains the cancer sample ids. Default: "improve_sample_id".
        gene_system_identifier (str or list of str): gene identifier system to use
            options: "Entrez", "Gene_Symbol", "Ensembl", "all", or any list
                     combination of ["Entrez", "Gene_Symbol", "Ensembl"]
        sep: Separator used in data file.
        verbose: Flag for verbosity. If True, info about computations is displayed. Default: True.
    
    Returns:
        pd.DataFrame: dataframe with the cell line data.

    
`load_drug_data(fname: Union[pathlib.Path, str], index: Optional[str] = None, columns: Optional[List] = None, sep: str = '\t', verbose: bool = True) ‑> pandas.core.frame.DataFrame`
:   Returns dataframe with drug features read from specified file.
    Index or columns may be redefined if requested.
    
    Args:
        fname: Name of, or Path to, file for reading drug data.
        index: Name of column to set as index in the data frame read.
        columns: List to rename data frame columns. Default: None, i.e. do not rename columns.
        sep: Separator used in data file.
        verbose: Flag for verbosity. If True, info about computations is displayed. Default: True.
    
    Returns:
        pd.Dataframe: dataframe that contains drug response values.

    
`scale_df(dataf, scaler_name='std', scaler=None, verbose=False)`
:   Returns a dataframe with scaled data.
    
    It can create a new scaler or use the scaler passed or return the
    data as it is. If `scaler_name` is None, no scaling is applied. If
    `scaler` is None, a new scaler is constructed. If `scaler` is not
    None, and `scaler_name` is not None, the scaler passed is used for
    scaling the data frame.
    
    Args:
        dataf: Pandas dataframe to scale.
        scaler_name: Name of scikit learn scaler to apply. Options:
                     ["minabs", "minmax", "std", "none"]. Default: std
                     standard scaling.
        scaler: Scikit object to use, in case it was created already.
                Default: None, create scikit scaling object of
                specified type.
        verbose: Flag specifying if verbose message printing is desired.
                 Default: False, no verbose print.
    
    Returns:
        pd.Dataframe: dataframe that contains drug response values.
        scaler: Scikit object used for scaling.

    
`set_col_names_in_multilevel_dataframe(df: pandas.core.frame.DataFrame, level_map: Dict, gene_system_identifier: Union[str, List[str]] = 'Gene_Symbol') ‑> pandas.core.frame.DataFrame`
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