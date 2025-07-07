determine_transform
-----------------------------------------

:funcelse:`improvelib.utils.`:funcname:`determine_transform`:funcelse:`(x_data_df, x_data_name, x_transform_list, output_dir)`

Sets the transformations (imputations, scaling, and/or subsetting) features based on a list of lists of [[strategy, subtype]]. 
Saves a dictionary containing the details needed to perform the specified transformations on all sets.

The following [strategy, subtype] can be specified for transformations:

* :code:`impute`

  * :code:`zero`: imputes all NaN with zeros
  * :code:`mean`: imputes all NaN with the mean of the whole DataFrame
  * :code:`mean_col`: imputes all NaN with the mean, column-wise
  * :code:`median`: imputes all NaN with the median of the whole DataFrame
  * :code:`median_col`: imputes all NaN with the median, column-wise

* :code:`scale`

  * :code:`std` or :code:`StandardScaler`: scales with `sklearn.preprocessing.StandardScaler() <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html>`_
  * :code:`minmax` or :code:`MinMaxScaler`: scales with `sklearn.preprocessing.MinMaxScaler() <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html>`_
  * :code:`minabs` or :code:`MinAbsScaler`: scales with `sklearn.preprocessing.MinAbsScaler() <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html>`_
  * :code:`robust` or :code:`RobustScaler`: scales with `sklearn.preprocessing.RobustScaler() <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html>`_

* :code:`subset`

  * :code:`L1000_SYMBOL`: subsets with L1000, should be used if column names are gene symbols
  * :code:`L1000_ENTREZ`: subsets with L1000, should be used if column names are Entrez
  * :code:`L1000_SYMBOL`: subsets with LINCS, should be used if column names are gene symbols
  * :code:`high_variance`: subsets to columns where the variance is higher than 0.8
  * :code:`<YOUR/PATH/TO/FILE>`: custom subsetting - file must be a plain text list of column names, with each name on a new line

.. warning::

  Determining transformations should be done on only the features in the training set. See the example below.


Used in *preprocess*.

.. container:: utilhead:
  
  Parameters:

**x_data_df** : pd.DataFrame
  The input DataFrame, column names must be Entrez IDs, index must be IDs.

**x_data_name** : str
  Name for the saved tranformation dictionary (.json will be added). 

**x_transform_list** : List of Lists of str
  List of lists of [[strategy, subtype]], e.g. [['subset', 'L1000_SYMBOL'], ['scale', 'StandardScaler']].

**output_dir** : str
  The output directory where the results should be saved. Should be set to params['output_dir'].

.. container:: utilhead:
  
  Returns:

None

.. container:: utilhead:
  
  Example

Before determining the transformations using the training set, it is important to only use features that are in the training set and have features for both drug and cell.
This can be easily performed by calling :doc:`api_utils_get_y_data_with_features` and :doc:`api_utils_get_features_in_y_data` like so:

.. code-block::

    print("Find intersection of training data.")
    response_train = drp.get_y_data_with_features(response_train, omics, params['canc_col_name'])
    response_train = drp.get_y_data_with_features(response_train, drugs, params['drug_col_name'])
    omics_train = drp.get_features_in_y_data(omics, response_train, params['canc_col_name'])
    drugs_train = drp.get_features_in_y_data(drugs, response_train, params['drug_col_name'])

Once your data contains only the features necessary for the training set, transformations can be determined:

.. code-block::

    print("Determine transformations.")
    drp.determine_transform(omics_train, 'omics_transform', omics_transform, params['output_dir'])
    drp.determine_transform(drugs_train, 'drugs_transform', drugs_transform, params['output_dir'])


