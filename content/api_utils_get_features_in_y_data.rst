get_features_in_y_data
-----------------------------------------

:funcelse:`improvelib.applications.drug_response_prediction.drp_utils.`:funcname:`get_features_in_y_data`:funcelse:`(feature_df, y_data_df, column_name)`

Takes a feature DataFrame and a y data DataFame and returns the feature DataFrame that 
contains only features that are present in the given y data DataFrame.

Used in *preprocess*.

.. container:: utilhead:
  
  Parameters:

**feature_df** : pd.DataFrame
  Feature DataFrame. ID must be index, as with all improvelib functions.

**y_data_df** : pd.DataFrame
  Y data DataFrame.

**column_name** : str
  Name of ID column for x data.

.. container:: utilhead:
  
  Returns:

**feature_df** : pd.DataFrame
  Feature DataFrame containing only the rows with features that are used in the y data.

.. container:: utilhead:
  
  Example

Before determining the transformations using the training set, it is important to only use features that are in the training set and have features for both drug and cell.
This can be easily performed by calling :code:`get_y_data_with_features` and :code:`get_features_in_y_data` like so:

.. code-block::

    print("Find intersection of training data.")
    response_train = drp.get_y_data_with_features(response_train, omics, params['canc_col_name'])
    response_train = drp.get_y_data_with_features(response_train, drugs, params['drug_col_name'])
    omics_train = drp.get_features_in_y_data(omics, response_train, params['canc_col_name'])
    drugs_train = drp.get_features_in_y_data(drugs, response_train, params['drug_col_name'])





