transform_data
-----------------------------------------

:funcelse:`improvelib.applications.drug_response_prediction.drp_utils.`:funcname:`transform_data`:funcelse:`(df, transform_file_name, preprocess_dir)`


Transforms (imputes, scales, and/or subsets) features based the transformations determined on the training set with :doc:`api_utils_determine_transform`. 
Reads the saved dictionary containing the details needed to perform the specified transformations on all sets, and performs the 
transformations on the given data.

Used in *preprocess*.

.. container:: utilhead:
  
  Parameters:

**df** : pd.DataFrame
  The input feature DataFrame, column names must be feature IDs (e.g. gene names), index must be IDs (e.g. cell line names).

**transform_file_name** : str
  Name of the file name used in :code:`determine_transform()`.

**preprocess_dir** : str
  The directory where the tranformation dictionary was saved. Should be set to params['output_dir'].

.. container:: utilhead:
  
  Returns:

**df** : pd.DataFrame
  The transformed DataFrame.

.. container:: utilhead:
  
  Example

After using the features in the training data to determine the transformation values with :doc:`api_utils_determine_transform`, the 
transformations can be applied as follows:

.. code-block::

    omics_stage = drp.transform_data(omics_stage, 'omics_transform', params['output_dir'])
    drugs_stage = drp.transform_data(drugs_stage, 'drugs_transform', params['output_dir'])




