Setting Parameters
=================================

A default configuration file is provided for every model and overrides the default value provided by improvelib. 
Parameters can be changed via alternate config file or by command line.
Parameters provided by command line have the highest priority and override parameters set by the configuration file.

Writing a config file
-----------------------
Each config file has three sections, :code:`[Preprocess]`, :code:`[Train]`, and :code:`[Infer]`. 
Each section is used independently for the relevant scripts and therefore parameters that are used in more than one script should be set in each relevant section.

Example config file (GraphDRP):

.. code-block:: bash

    [Preprocess]
    train_split_file = CCLE_split_0_train.txt
    val_split_file = CCLE_split_0_val.txt
    test_split_file = CCLE_split_0_test.txt
    data_format = .pt
    y_data_files = [["response.tsv"]]
    x_data_canc_files = [["cancer_gene_expression.tsv", ["Gene_Symbol"]]]
    x_data_drug_files = [["drug_SMILES.tsv"]]
    use_lincs = True
    scaling = std

    [Train]
    data_format = .pt
    model_file_name = model
    model_file_format = .pt
    epochs = 150
    batch_size = 256
    val_batch = 256
    learning_rate = 0.0001
    loss = mse
    early_stop_metric = mse
    patience = 20
    ckpt_save_interval = 5
    model_arch = GINConvNet
    log_interval = 30
    cuda_name = cuda:7

    [Infer]
    data_format = .pt
    model_file_name = model
    model_file_format = .pt
    infer_batch = 256
    cuda_name = cuda:7

Using an alternate config file
--------------------------------

To use an alternate config file, specify the name of the config file on the command line like so:

.. code-block:: bash

    python mymodel_preprocess_improve.py --config_file my_alternate_config.ini

Setting parameters by command line
-----------------------------------

All parameters can be set by command line, which will override the same parameter set by the config, or default value if the value is not set by the config file.
For example, we can specific a different output directory and number of epochs like so:

.. code-block:: bash

    python mymodel_preprocess_improve.py --output_dir /path/to/my/different/outdir --epochs 100

    


