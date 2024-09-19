Configuration File Template
================================

Below is an example of a configuration file. You should place the values of parameters (IMPROVE, application-specific, and model-specific) under each appropriate section (preprocess, train, and infer).
The file should be named :code:`mymodel_params.txt` where 'mymodel' is the name of your model.

.. code-block:: 

    [Preprocess]
    train_split_file = CCLE_split_0_train.txt
    val_split_file = CCLE_split_0_val.txt
    test_split_file = CCLE_split_0_test.txt
    data_format = .pt
    y_data_files = [["response.tsv"]]
    x_data_canc_files = [["cancer_gene_expression.tsv", ["Gene_Symbol"]]]
    x_data_drug_files = [["drug_SMILES.tsv"]]

    [Train]
    data_format = .pt
    model_file_name = model
    model_file_format = .pt
    epochs = 50
    batch_size = 256
    val_batch = 256
    learning_rate = 0.0001
    patience = 10


    [Infer]
    data_format = .pt
    model_file_name = model
    model_file_format = .pt
    infer_batch = 256