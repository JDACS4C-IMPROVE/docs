get_y_data_with_features
-----------------------------------------

:funcelse:`improvelib.applications.drug_response_prediction.drp_utils.`:funcname:`get_y_data_with_features`:funcelse:`(y_data_df, feature_df, column_name)`

Takes a y data DataFrame and feature DataFrame(s) and returns a y data DataFrame
that contains only rows that have available features for the feature type(s) provided. 
All features in the list must have the same ID type (e.g. drug or cell). If a list is given, 
only rows will be retained if all features in the list are available.

Used in *preprocess*.

.. container:: utilhead:
  
  Parameters:

**y_data_df** : pd.DataFrame
  Y data DataFrame.

**feature_df** : pd.DataFrame or List of pd.DataFrame
  Feature DataFrame or a list of feature DataFrames of the same ID (drug or cell). ID must be index, as with all improvelib functions.

**column_name** : str
  Name of ID column for x data.

.. container:: utilhead:
  
  Returns:

**y_data_df** : pd.DataFrame
  Y data DataFrame containing only the rows with features available.

.. container:: utilhead:
  
  Example

Before determining the transformations using the training set, it is important to only use features that are in the training set and have features for both drug and cell.
This can be easily performed by calling :code:`get_y_data_with_features` and :code:`get_features_in_y_data` like so:

.. code-block::

    response_train = drp.get_y_data_with_features(response_train, omics, params['canc_col_name'])
    response_train = drp.get_y_data_with_features(response_train, drugs, params['drug_col_name'])





