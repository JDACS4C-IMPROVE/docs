get_common_samples
-----------------------------------------

:funcelse:`improvelib.utils.`:funcname:`get_common_samples`:funcelse:`(df1, df2, ref_col)`

Search for common data in a reference column and retain only those rows.

Provided as a helper function.

.. container:: utilhead:
  
  Parameters:

**df1** : pd.DataFrame
  First DataFrame.

**df2** : pd.DataFrame
  Second DataFrame.

**ref_col** : str
  The reference column to find the common values.

.. container:: utilhead:
  
  Returns:

**df1, df2** : Tuple of pd.DataFrames
  DataFrames after filtering for common data.

.. container:: utilhead:
  
  Example

