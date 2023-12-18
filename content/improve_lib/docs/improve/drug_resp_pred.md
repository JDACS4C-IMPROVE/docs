Module improve.drug_resp_pred
=============================
Functionality for IMPROVE drug response prediction (DRP) models.

Functions
---------

    
`common_elements(list1: List, list2: List, verbose: bool = False) ‑> List`
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

Classes
-------

`DrugResponseLoader(params: Dict, split_file: str, sep: str = '\t', verbose: bool = True)`
:   Class for loading monotherapy drug response data.
    
    Args:
        params : IMPROVE params
        split_file : file name that contains the split ids (rows)
        sep : chararcter separtor in the loaded files (e.g., "  " for tsv files)
    
    Example:
        from improve import drug_resp_pred as drp
        drp_loader = drp.DrugResponseLoader(params)
        print(drp_loader)
        print(dir(drp_loader))
        rsp = drp_loader["response.tsv"]

    ### Static methods

    `check_path(fpath)`
    :

    ### Methods

    `load_all_response_data(self, verbose: str = True)`
    :   ...

    `load_response_data(self, fname)`
    :

`DrugsLoader(params: Dict, sep: str = '\t', verbose: bool = True)`
:   Example:
        from improve import drug_resp_pred as drp
        drugs_loader = drp.DrugsLoader(params)
        print(drugs_loader)
        print(dir(drugs_loader))
        smi = drugs_loader["drug_SMILES.tsv"]

    ### Static methods

    `check_path(fpath)`
    :

    ### Methods

    `load_all_drug_data(self)`
    :   ...

    `load_drug_data(self, fname)`
    :   ...

`OmicsLoader(params: Dict, sep: str = '\t', verbose: bool = True)`
:   Class aggregates methods to load omics data.
    
    Args:
        params : IMPROVE params
        sep : chararcter separtor in the loaded files (e.g., "  " for tsv files)
    
    Example:
        from improve import drug_resp_pred as drp
        omics_loader = drp.OmicsLoader(params)
        print(omics_loader)
        print(dir(omics_loader))
        ge = omics_loader["cancer_gene_expression.tsv"]

    ### Static methods

    `check_path(fpath)`
    :

    ### Methods

    `load_all_omics_data(self)`
    :   Load all omics data appear in self.inp