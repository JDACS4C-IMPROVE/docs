v1.0.0
===============

To ensure compatibility with the IMPROVE software release v1.0.0, please update your curated model. 
Follow the instructions below and refer to the checklist at the bottom of the page. 
In addition, use models `GraphDRP <https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/develop>`_ 
and `LGBM <https://github.com/JDACS4C-IMPROVE/LGBM/tree/develop>`_ as examples. 

Overview
---------
IMPROVE version v1.0.0 provides greater flexibility to accomodate diverse applications and workflows, and simplifies the API for 
easier model curation to encourage broader adoption of the software.  
Additionally, this version provides a simplified and more user-friendly interface, as demonstrated by intuitive help outputs, 
comprehensive READMEs, and documentation that facilitate easy switching between versions.



Parameters
------------


DRP Benchmarks v2 update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Benchmark dataframes no longer have a triple header, and are flexibly loaded. This allows users to use data other than benchmark data to run models (for more information, see :doc:`using_external_data`).

- All data must adhere to the standards outlined here. Of note, in x data the ID is always the index.

- Delete:

  .. code-block::

    import improvelib.applications.drug_response_prediction.drug_utils as drugs_utils
    import improvelib.applications.drug_response_prediction.omics_utils as omics_utils

- Example change for omics:

  .. code-block::

    omics_obj = omics_utils.OmicsLoader(params)
    ge = omics_obj.dfs['cancer_gene_expression.tsv']


  to

  .. code-block::

    ge = frm.get_x_data(file = params['cell_transcriptomic_file'], 
                        benchmark_dir = params['input_dir'], 
                        column_name = params['canc_col_name'])
    ge = ge.reset_index()

- Example change for drug:

  .. code-block::

    drugs_obj = drugs_utils.DrugsLoader(params)
    md = drugs_obj.dfs['drug_mordred.tsv']


  to

  .. code-block::

    md = frm.get_x_data(file = params['drug_mordred_file'], 
                    benchmark_dir = params['input_dir'], 
                    column_name = params['drug_col_name'])

- Example change for response (change all instances):

  .. code-block::

    rsp_tr = drp.DrugResponseLoader(params,
                                    split_file=params["train_split_file"],
                                    verbose=False).dfs["response.tsv"]


  to

  .. code-block::

    rsp_tr = drp.get_y_data(split_file=params["train_split_file"], 
                                   benchmark_dir=params['input_dir'], 
                                   y_data_file=params['y_data_file'])


Add updates to parameter file.


All references to 'response' have been changed to y data for consistency and clarity.
