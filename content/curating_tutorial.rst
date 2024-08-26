===========================
Tutorial
===========================
NATASHA: UPDATE THIS

IMPROVE comparison workflows require that prediction models adhere a unified code interface.

In the realm of supervised learning models, three fundamental components exist: data preparation, model training and hyperparameter optimization (HPO), and performance evaluation [`1 <https://www.frontiersin.org/articles/10.3389/fmed.2023.1086097/full>`_].
Recognizing this norm, we propose to establish three distinct scripts, with each script dedicated to one of these essential components.
By establishing this convention and separating the components into separate scripts we aim to enhance code readability, provenance, and maintainability.
The first script handles **preprocessing** of input data, the second manages model **training**, and the third enables the utilization of the model in **inference** mode.
All these scripts should be organized in a modular and flexible manner to enable seamless combination, integration, and workflow generation.
This modular separation of components aims to facilitate an efficient and manageable workflow design and implemenation.

| To adhere the unified code interface, model repositories are required to provide a python script for each of the three components and one text file specifying default parameter values. All three scripts utilize functionality from `IMPROVE library <https://github.com/JDACS4C-IMPROVE/IMPROVE>`_.

| 1. :ref:`Preprocessing <Preprocessing>`. Preprocessing transforms benchmark data (a.k.a *raw data*) into model specific input data (a.k.a *Machine Learning (ML) data*). An example of *raw data* and *ML data* in the context of :ref:`drug response prediction<Drug Response Prediction>` (DRP) are described in :ref:`applications <Applications>`.
| 2. :ref:`Training <Training>`. Training and optimization of the model. This often includes :ref:`hyperparameter optimization (HPO) <Hyper Parameter Optimization (HPO)>` and early stopping with validation data to mitigate overfitting.
| 3. :ref:`Inference <Inference>`. Computing predictions and evaluating model prediction performance using the preprocessed data (from step 1) and the trained model (from step 2).
| 4. :ref:`Parameter file <Parameter file>`. A file that contains default parameters for the three scripts.

.. figure:: ../images/ML_pipeline_steps.png
    :width: 600
    :align: center

    General steps in developing and using prediction model.

In the sections below, we provide an example of the three scripts, showing the use of a `LightGBM <https://lightgbm.readthedocs.io/en/stable/>`_ model for drug response prediction. 
The :ref:`cross-study analysis benchmark data<Benchmark Data for Cross-Study Analysis>` is used for the analysis.
In these scripts, the interface, the required code components and the utilization of `IMPROVE library <https://github.com/JDACS4C-IMPROVE/IMPROVE>`_ are demonstrated.
The whole code associated with this example can found in `this repo <https://github.com/JDACS4C-IMPROVE/LGBM/tree/develop>`_.

In the code examples below, required code sections are designated with *[Req]*. These sections refer to functionality that models must integrate in their scripts.





Preprocessing
---------------------------------
.. https://stackoverflow.com/questions/18632781/how-to-make-an-internal-link-to-a-heading-in-sphinx-restructuredtext-without-cre
This script preprocesses raw benchmark data (e.g., :ref:`cross-study analysis<Benchmark Data for Cross-Study Analysis>`) and generates data files for a LightGBM prediction model.
The naming convention for the preprocessing script is `MODELNAME_preprocess_improve.py`. For example: `lgbm_preprocess_improve.py <https://github.com/JDACS4C-IMPROVE/LGBM/blob/master/lgbm_preprocess_improve.py>`_.

All the outputs from the preprocessing script are saved in ``params["ml_data_outdir"]``.

| **Outputs from running the preprocessing script**:

1. **Model input data files.**
    This script creates three data files corresponding to train, validation, and test data.
    These data files are used as inputs to the ML/DL prediction model in the :ref:`training <Training>` and :ref:`inference <Inference>` scripts.
    The way that data is structured in these data files is highly dependent on the prediction model. Therefore, the :ref:`training <Training>` and :ref:`inference <Inference>` scripts should provide and utilize appropriate functionality for data loading and passing it to the model.
    The file format is specified by ``params["data_format"]``.
    For example:
        | LightGBM model: ``train_data.csv``, ``val_data.csv``, ``test_data.csv``
        | GraphDRP model: ``train_data.pt``, ``val_data.pt``, ``test_data.pt``

2. **Y data files.**
    The script also creates DataFrames with true Y values and additional metadata.
    Regardless of the prediction model, the script generates:
        ``train_y_data.csv``, ``val_y_data.csv``, and ``test_y_data.csv``.

Note that in addition to the data files mentioned above, the preprocessing script can be used to save additional utility data required by the data loader.

Below is a preprocessing script that takes :ref:`cross-study analysis benchmark data<Benchmark Data for Cross-Study Analysis>` and generates training, validation, and test data files. The script below is available in `this repo <https://github.com/JDACS4C-IMPROVE/LGBM/blob/master/lgbm_preprocess_improve.py>`_. Another example for a preprocessing script can be found in the `repo <https://github.com/JDACS4C-IMPROVE/GraphDRP/blob/develop/graphdrp_preprocess_improve.py>`_ for DL model, GraphDRP.

.. raw:: html

   <details>
   <summary><a>Preprocessing script (click to expand)</a></summary>

.. code-block:: python

    import sys
    from pathlib import Path
    from typing import Dict

    import pandas as pd
    import joblib

    # [Req] IMPROVE/CANDLE imports
    from improve import framework as frm
    from improve import drug_resp_pred as drp

    # Model-specifc imports
    from model_utils.utils import gene_selection, scale_df

    filepath = Path(__file__).resolve().parent # [Req]

    # ---------------------
    # [Req] Parameter lists
    # ---------------------
    # Two parameter lists are required:
    # 1. app_preproc_params
    # 2. model_preproc_params
    # 
    # The values for the parameters in both lists should be specified in a
    # parameter file that is passed as default_model arg in
    # frm.initialize_parameters().

    # 1. App-specific params (App: monotherapy drug response prediction)
    # Note! This list should not be modified (i.e., no params should added or
    # removed from the list.
    # 
    # There are two types of params in the list: default and required
    # default:   default values should be used
    # required:  these params must be specified for the model in the param file
    app_preproc_params = [
    {"name": "y_data_files", # default
        "type": str,
        "help": "List of files that contain the y (prediction variable) data. \
                Example: [['response.tsv']]",
    },
    {"name": "x_data_canc_files", # required
        "type": str,
        "help": "List of feature files including gene_system_identifer. Examples: \n\
                1) [['cancer_gene_expression.tsv', ['Gene_Symbol']]] \n\
                2) [['cancer_copy_number.tsv', ['Ensembl', 'Entrez']]].",
    },
    {"name": "x_data_drug_files", # required
        "type": str,
        "help": "List of feature files. Examples: \n\
                1) [['drug_SMILES.tsv']] \n\
                2) [['drug_SMILES.tsv'], ['drug_ecfp4_nbits512.tsv']]",
    },
    {"name": "canc_col_name",
        "default": "improve_sample_id", # default
        "type": str,
        "help": "Column name in the y (response) data file that contains the cancer sample ids.",
    },
    {"name": "drug_col_name", # default
        "default": "improve_chem_id",
        "type": str,
        "help": "Column name in the y (response) data file that contains the drug ids.",
    },
    ]

    # 2. Model-specific params (Model: LightGBM)
    # All params in model_preproc_params are optional.
    # If no params are required by the model, then it should be an empty list.
    model_preproc_params = [
    {"name": "use_lincs",
        "type": frm.str2bool,
        "default": True,
        "help": "Flag to indicate if landmark genes are used for gene selection.",
    },
    {"name": "scaling",
        "type": str,
        "default": "std",
        "choice": ["std", "minmax", "miabs", "robust"],
        "help": "Scaler for gene expression and Mordred descriptors data.",
    },
    {"name": "ge_scaler_fname",
        "type": str,
        "default": "x_data_gene_expression_scaler.gz",
        "help": "File name to save the gene expression scaler object.",
    },
    {"name": "md_scaler_fname",
        "type": str,
        "default": "x_data_mordred_scaler.gz",
        "help": "File name to save the Mordred scaler object.",
    },
    ]

    # [Req] Combine the two lists (the combined parameter list will be passed to
    # frm.initialize_parameters() in the main().
    preprocess_params = app_preproc_params + model_preproc_params
    # ---------------------

    # [Req]
    def run(params: Dict):
    """ Run data preprocessing.

    Args:
        params (dict): dict of CANDLE/IMPROVE parameters and parsed values.

    Returns:
        str: directory name that was used to save the preprocessed (generated)
            ML data files.
    """

    # ------------------------------------------------------
    # [Req] Build paths and create output dir
    # ------------------------------------------------------
    # Build paths for raw_data, x_data, y_data, splits
    params = frm.build_paths(params)  

    # Create output dir for model input data (to save preprocessed ML data)
    frm.create_outdir(outdir=params["ml_data_outdir"])

    # ------------------------------------------------------
    # [Req] Load X data (feature representations)
    # ------------------------------------------------------
    # Use the provided data loaders to load data that is required by the model.
    #
    # Benchmark data includes three dirs: x_data, y_data, splits.
    # The x_data contains files that represent feature information such as
    # cancer representation (e.g., omics) and drug representation (e.g., SMILES).
    #
    # Prediction models utilize various types of feature representations.
    # Drug response prediction (DRP) models generally use omics and drug features.
    #
    # If the model uses omics data types that are provided as part of the benchmark
    # data, then the model must use the provided data loaders to load the data files
    # from the x_data dir.
    print("\nLoads omics data.")
    omics_obj = drp.OmicsLoader(params)
    # print(omics_obj)
    ge = omics_obj.dfs['cancer_gene_expression.tsv'] # return gene expression

    print("\nLoad drugs data.")
    drugs_obj = drp.DrugsLoader(params)
    # print(drugs_obj)
    md = drugs_obj.dfs['drug_mordred.tsv'] # return the Mordred descriptors
    md = md.reset_index()  # TODO. implement reset_index() inside the loader

    # ------------------------------------------------------
    # Further preprocess X data
    # ------------------------------------------------------
    # Gene selection (based on LINCS landmark genes)
    if params["use_lincs"]:
        genes_fpath = filepath/"landmark_genes"
        ge = gene_selection(ge, genes_fpath, canc_col_name=params["canc_col_name"])

    # Prefix gene column names with "ge."
    fea_sep = "."
    fea_prefix = "ge"
    ge = ge.rename(columns={fea: f"{fea_prefix}{fea_sep}{fea}" for fea in ge.columns[1:]})

    # ------------------------------------------------------
    # Create feature scaler
    # ------------------------------------------------------
    # Load and combine responses
    print("Create feature scaler.")
    rsp_tr = drp.DrugResponseLoader(params,
                                    split_file=params["train_split_file"],
                                    verbose=False).dfs["response.tsv"]
    rsp_vl = drp.DrugResponseLoader(params,
                                    split_file=params["val_split_file"],
                                    verbose=False).dfs["response.tsv"]
    rsp = pd.concat([rsp_tr, rsp_vl], axis=0)

    # Retian feature rows that are present in the y data (response dataframe)
    # Intersection of omics features, drug features, and responses
    rsp = rsp.merge(ge[params["canc_col_name"]], on=params["canc_col_name"], how="inner")
    rsp = rsp.merge(md[params["drug_col_name"]], on=params["drug_col_name"], how="inner")
    ge_sub = ge[ge[params["canc_col_name"]].isin(rsp[params["canc_col_name"]])].reset_index(drop=True)
    md_sub = md[md[params["drug_col_name"]].isin(rsp[params["drug_col_name"]])].reset_index(drop=True)

    # Scale gene expression
    _, ge_scaler = scale_df(ge_sub, scaler_name=params["scaling"])
    ge_scaler_fpath = Path(params["ml_data_outdir"]) / params["ge_scaler_fname"]
    joblib.dump(ge_scaler, ge_scaler_fpath)
    print("Scaler object for gene expression: ", ge_scaler_fpath)

    # Scale Mordred descriptors
    _, md_scaler = scale_df(md_sub, scaler_name=params["scaling"])
    md_scaler_fpath = Path(params["ml_data_outdir"]) / params["md_scaler_fname"]
    joblib.dump(md_scaler, md_scaler_fpath)
    print("Scaler object for Mordred:         ", md_scaler_fpath)

    del rsp, rsp_tr, rsp_vl, ge_sub, md_sub

    # ------------------------------------------------------
    # [Req] Construct ML data for every stage (train, val, test)
    # ------------------------------------------------------
    # All models must load response data (y data) using DrugResponseLoader().
    # Below, we iterate over the 3 split files (train, val, test) and load
    # response data, filtered by the split ids from the split files.

    # Dict with split files corresponding to the three sets (train, val, and test)
    stages = {"train": params["train_split_file"],
                "val": params["val_split_file"],
                "test": params["test_split_file"]}

    for stage, split_file in stages.items():

        # --------------------------------
        # [Req] Load response data
        # --------------------------------
        rsp = drp.DrugResponseLoader(params,
                                        split_file=split_file,
                                        verbose=False).dfs["response.tsv"]

        # --------------------------------
        # Data prep
        # --------------------------------
        # Retain (canc, drug) responses for which both omics and drug features
        # are available.
        rsp = rsp.merge(ge[params["canc_col_name"]], on=params["canc_col_name"], how="inner")
        rsp = rsp.merge(md[params["drug_col_name"]], on=params["drug_col_name"], how="inner")
        ge_sub = ge[ge[params["canc_col_name"]].isin(rsp[params["canc_col_name"]])].reset_index(drop=True)
        md_sub = md[md[params["drug_col_name"]].isin(rsp[params["drug_col_name"]])].reset_index(drop=True)

        # Scale features
        ge_sc, _ = scale_df(ge_sub, scaler=ge_scaler) # scale gene expression
        md_sc, _ = scale_df(md_sub, scaler=md_scaler) # scale Mordred descriptors

        # --------------------------------
        # [Req] Save ML data files in params["ml_data_outdir"]
        # The implementation of this step, depends on the model.
        # --------------------------------
        # [Req] Build data name
        data_fname = frm.build_ml_data_name(params, stage)

        print("Merge data")
        data = rsp.merge(ge_sc, on=params["canc_col_name"], how="inner")
        data = data.merge(md_sc, on=params["drug_col_name"], how="inner")
        data = data.sample(frac=1.0).reset_index(drop=True) # shuffle

        print("Save data")
        data = data.drop(columns=["study"]) # to_parquet() throws error since "study" contain mixed values
        data.to_parquet(Path(params["ml_data_outdir"])/data_fname) # saves ML data file to parquet

        # Prepare the y dataframe for the current stage
        fea_list = ["ge", "mordred"]
        fea_cols = [c for c in data.columns if (c.split(fea_sep)[0]) in fea_list]
        meta_cols = [c for c in data.columns if (c.split(fea_sep)[0]) not in fea_list]
        ydf = data[meta_cols]

        # [Req] Save y dataframe for the current stage
        frm.save_stage_ydf(ydf, params, stage)

    return params["ml_data_outdir"]

    # [Req]
    def main(args):
        # [Req]
        additional_definitions = preprocess_params
        params = frm.initialize_parameters(
            filepath,
            default_model="lgbm_params.txt",
            additional_definitions=additional_definitions,
            required=None,
        )
        ml_data_outdir = run(params)
        print("\nFinished data preprocessing.")

    # [Req]
    if __name__ == "__main__":
        main(sys.argv[1:])

.. raw:: html

   </details>




As mentioned earlier, all the required code sections are designated with *[Req]*.
One of the requirements is to define two lists of directories: ``app_preproc_params`` and ``model_preproc_params``.
Each dictionary (dict) specifies keyword arguments.

| The params in ``app_preproc_params`` is a collection of application-specific parameters for the preprocessing step. The application in this case is monotherapy drug response prediction. This list should be copied to the script as is. There are two types of params in this list: *default* and *required*.
* *default*:   standard values to be used
* *required*:  model-specific values that must be included in the :ref:`parameter file <Parameter file>`

The params in ``model_preproc_params`` is a collection of model-specific parameters for the preprocessing step. 
All params in this list are optional. If no params are required by the model, then it should be an empty list.


Training
---------------------------------
The training script is used for executing model training as well as conducting :ref:`hyperparameter optimization (HPO) <Hyper Parameter Optimization (HPO)>`. The script generates a trained model, and model predictions and prediction performance scores calculated using the validation data. The naming convention for the training script is `MODELNAME_train_improve.py`. For example: `lgbm_train_improve.py <https://github.com/JDACS4C-IMPROVE/LGBM/blob/master/lgbm_train_improve.py>`_.

All the outputs from the training script are saved in ``params["model_outdir"]``.

| **Outputs from running the training script:**

1. **Trained model.**
    The training script loads the train and validation data that were generated during the :ref:`preprocessing <Preprocessing>` step.
    The train data and validation data are used for, respectively, model training and early stopping.
    When the model converges (i.e., prediction performance stops improving on validation data), the model is saved into a file.
    The model file name and file format are specified by, respectively, ``params["model_file_name"]`` and ``params["model_file_format"]``.
    For example:
        | LightGBM model: ``model.txt``
        | GraphDRP model: ``model.pt``

2. **Predictions on validation data.**
    Model predictions are calculated using the trained model on validation data.
    The predictions are saved as a DataFrame in ``val_y_data_predicted.csv``

3. **Prediction performance scores on validation data.**
    The performance scores are calculated using the model predictions and the true Y values for the performance metrics specified in the ``metrics_list``.
    The scores are saved in ``val_scores.json``.

Below is a training script that takes the generated data from the :ref:`preprocessing <Preprocessing>` step and trains a LightGBM model. This script is available in `this repo <https://github.com/JDACS4C-IMPROVE/LGBM/blob/master/lgbm_train_improve.py>`_. Another example for a training script can be found in a `repo <https://github.com/JDACS4C-IMPROVE/GraphDRP/blob/develop/graphdrp_train_improve.py>`_ for the GraphDRP model.

.. raw:: html

   <details>
   <summary><a>Training script (click to expand)</a></summary>

.. code-block:: python

    import sys
    from pathlib import Path
    from typing import Dict

    import pandas as pd
    import lightgbm as lgb

    # [Req] IMPROVE/CANDLE imports
    from improve import framework as frm

    # Model-specifc imports
    from model_utils.utils import extract_subset_fea

    # [Req] Imports from preprocess script
    from lgbm_preprocess_improve import preprocess_params

    filepath = Path(__file__).resolve().parent # [Req]

    # ---------------------
    # [Req] Parameter lists
    # ---------------------
    # Two parameter lists are required:
    # 1. app_train_params
    # 2. model_train_params
    # 
    # The values for the parameters in both lists should be specified in a
    # parameter file that is passed as default_model arg in
    # frm.initialize_parameters().

    # 1. App-specific params (App: monotherapy drug response prediction)
    # Currently, there are no app-specific params for this script.
    app_train_params = []

    # 2. Model-specific params (Model: LightGBM)
    # All params in model_train_params are optional.
    # If no params are required by the model, then it should be an empty list.
    model_train_params = [
        {"name": "learning_rate",
        "type": float,
        "default": 0.1,
        "help": "Learning rate for the optimizer."
        },
    ]

    # Combine the two lists (the combined parameter list will be passed to
    # frm.initialize_parameters() in the main().
    train_params = app_train_params + model_train_params
    # ---------------------

    # [Req] List of metrics names to compute prediction performance scores
    metrics_list = ["mse", "rmse", "pcc", "scc", "r2"]  


    # [Req]
    def run(params: Dict):
        """ Run model training.

        Args:
            params (dict): dict of CANDLE/IMPROVE parameters and parsed values.

        Returns:
            dict: prediction performance scores computed on validation data
                according to the metrics_list.
        """
        # ------------------------------------------------------
        # [Req] Create output dir and build model path
        # ------------------------------------------------------
        # Create output dir for trained model, val set predictions, val set
        # performance scores
        frm.create_outdir(outdir=params["model_outdir"])

        # Build model path
        modelpath = frm.build_model_path(params, model_dir=params["model_outdir"])

        # ------------------------------------------------------
        # [Req] Create data names for train and val sets
        # ------------------------------------------------------
        train_data_fname = frm.build_ml_data_name(params, stage="train")
        val_data_fname = frm.build_ml_data_name(params, stage="val")

        # ------------------------------------------------------
        # Load model input data (ML data)
        # ------------------------------------------------------
        tr_data = pd.read_parquet(Path(params["train_ml_data_dir"])/train_data_fname)
        vl_data = pd.read_parquet(Path(params["val_ml_data_dir"])/val_data_fname)

        fea_list = ["ge", "mordred"]
        fea_sep = "."

        # Train data
        xtr = extract_subset_fea(tr_data, fea_list=fea_list, fea_sep=fea_sep)
        ytr = tr_data[[params["y_col_name"]]]
        print("xtr:", xtr.shape)
        print("ytr:", ytr.shape)

        # Val data
        xvl = extract_subset_fea(vl_data, fea_list=fea_list, fea_sep=fea_sep)
        yvl = vl_data[[params["y_col_name"]]]
        print("xvl:", xvl.shape)
        print("yvl:", yvl.shape)

        # ------------------------------------------------------
        # Prepare, train, and save model
        # ------------------------------------------------------
        # Prepare model and train settings
        ml_init_args = {'n_estimators': 1000, 'max_depth': -1,
                        'learning_rate': params["learning_rate"],
                        'num_leaves': 31, 'n_jobs': 8, 'random_state': None}
        model = lgb.LGBMRegressor(objective='regression', **ml_init_args)

        # Train model
        ml_fit_args = {'verbose': False, 'early_stopping_rounds': 50}
        ml_fit_args['eval_set'] = (xvl, yvl)
        model.fit(xtr, ytr, **ml_fit_args)

        # Save model
        model.booster_.save_model(str(modelpath))
        del model

        # ------------------------------------------------------
        # Load best model and compute predictions
        # ------------------------------------------------------
        # Load the best saved model (as determined based on val data)
        model = lgb.Booster(model_file=str(modelpath))

        # Compute predictions
        val_pred = model.predict(xvl)
        val_true = yvl.values.squeeze()
    
        # ------------------------------------------------------
        # [Req] Save raw predictions in dataframe
        # ------------------------------------------------------
        frm.store_predictions_df(
            params,
            y_true=val_true, y_pred=val_pred, stage="val",
            outdir=params["model_outdir"]
        )

        # ------------------------------------------------------
        # [Req] Compute performance scores
        # ------------------------------------------------------
        val_scores = frm.compute_performace_scores(
            params,
            y_true=val_true, y_pred=val_pred, stage="val",
            outdir=params["model_outdir"], metrics=metrics_list
        )

        return val_scores

    # [Req]
    def main(args):
        # [Req]
        additional_definitions = preprocess_params + train_params
        params = frm.initialize_parameters(
            filepath,
            default_model="lgbm_params.txt",
            additional_definitions=additional_definitions,
            required=None,
        )
        val_scores = run(params)
        print("\nFinished model training.")

    # [Req]
    if __name__ == "__main__":
        main(sys.argv[1:])

.. raw:: html

   </details>



Similar to the :ref:`preprocessing <Preprocessing>` script, the training script requires defining two parameter lists: ``app_train_params`` and ``model_train_params``.




Inference
---------------------------------
The inference script is used to run the trained model in inference mode, allowing to compute predictions on an input data. The script generates model predictions and prediction performance scores for the test data. The naming convention for the inference script is `MODELNAME_infer_improve.py`. For example: `lgbm_infer_improve.py <https://github.com/JDACS4C-IMPROVE/LGBM/blob/master/lgbm_infer_improve.py>`_.

All the outputs from the training script are saved in ``params["infer_outdir"]``.

| **Outputs from executing the training script:**

1. **Predictions on test data.**
    Model predictions calculated using the trained model on test data.
    The predictions are saved as a DataFrame in ``test_y_data_predicted.csv``

2. **Prediction performance scores on test data.**
    The performance scores are calculated using the model predictions and the true Y values for the performance metrics specified in the ``metrics_list``.
    The scores are saved in ``test_scores.json``.

Below is an inference script that takes the generated test data from the :ref:`preprocessing <Preprocessing>` step and trained a LightGBM model from the :ref:`training <Training>` step. This script is available in `this repo <https://github.com/JDACS4C-IMPROVE/LGBM/blob/master/lgbm_infer_improve.py>`_. Another example for an inference script can be found in a `repo <https://github.com/JDACS4C-IMPROVE/GraphDRP/blob/develop/graphdrp_infer_improve.py>`_ for the GraphDRP model.

.. raw:: html

   <details>
   <summary><a>Inference script (click to expand)</a></summary>

.. code-block:: python

    import sys
    from pathlib import Path
    from typing import Dict

    import pandas as pd
    import lightgbm as lgb

    # [Req] IMPROVE/CANDLE imports
    from improve import framework as frm
    from improve.metrics import compute_metrics

    # Model-specifc imports
    from model_utils.utils import extract_subset_fea

    # [Req] Imports from preprocess and train scripts
    from lgbm_preprocess_improve import preprocess_params
    from lgbm_train_improve import metrics_list, train_params

    filepath = Path(__file__).resolve().parent # [Req]

    # ---------------------
    # [Req] Parameter lists
    # ---------------------
    # Two parameter lists are required:
    # 1. app_infer_params
    # 2. model_infer_params
    # 
    # The values for the parameters in both lists should be specified in a
    # parameter file that is passed as default_model arg in
    # frm.initialize_parameters().

    # 1. App-specific params (App: monotherapy drug response prediction)
    # Currently, there are no app-specific params in this script.
    app_infer_params = []

    # 2. Model-specific params (Model: LightGBM)
    # All params in model_infer_params are optional.
    # If no params are required by the model, then it should be an empty list.
    model_infer_params = []

    # [Req] Combine the two lists (the combined parameter list will be passed to
    # frm.initialize_parameters() in the main().
    infer_params = app_infer_params + model_infer_params
    # ---------------------

    # [Req]
    def run(params: Dict):
        """ Run model inference.

        Args:
            params (dict): dict of CANDLE/IMPROVE parameters and parsed values.

        Returns:
            dict: prediction performance scores computed on test data according
                to the metrics_list.
        """

        # ------------------------------------------------------
        # [Req] Create output dir
        # ------------------------------------------------------
        frm.create_outdir(outdir=params["infer_outdir"])

        # ------------------------------------------------------
        # [Req] Create data name for test set
        # ------------------------------------------------------
        test_data_fname = frm.build_ml_data_name(params, stage="test")

        # ------------------------------------------------------
        # Load model input data (ML data)
        # ------------------------------------------------------
        te_data = pd.read_parquet(Path(params["test_ml_data_dir"])/test_data_fname)

        fea_list = ["ge", "mordred"]
        fea_sep = "."

        # Test data
        xte = extract_subset_fea(te_data, fea_list=fea_list, fea_sep=fea_sep)
        yte = te_data[[params["y_col_name"]]]

        # ------------------------------------------------------
        # Load best model and compute predictions
        # ------------------------------------------------------
        # Build model path
        modelpath = frm.build_model_path(params, model_dir=params["model_dir"]) # [Req]

        # Load LightGBM
        model = lgb.Booster(model_file=str(modelpath))

        # Predict
        test_pred = model.predict(xte)
        test_true = yte.values.squeeze()

        # ------------------------------------------------------
        # [Req] Save raw predictions in dataframe
        # ------------------------------------------------------
        frm.store_predictions_df(
            params,
            y_true=test_true, y_pred=test_pred, stage="test",
            outdir=params["infer_outdir"]
        )

        # ------------------------------------------------------
        # [Req] Compute performance scores
        # ------------------------------------------------------
        test_scores = frm.compute_performace_scores(
            params,
            y_true=test_true, y_pred=test_pred, stage="test",
            outdir=params["infer_outdir"], metrics=metrics_list
        )

        return test_scores

    # [Req]
    def main(args):
        # [Req]
        additional_definitions = preprocess_params + train_params + infer_params
        params = frm.initialize_parameters(
            filepath,
            default_model="lgbm_params.txt",
            additional_definitions=additional_definitions,
            required=None,
        )
        test_scores = run(params)
        print("\nFinished model inference.")

    # [Req]
    if __name__ == "__main__":
        main(sys.argv[1:])

.. raw:: html

   </details>



Similar to the :ref:`training <Training>` script, the inference script requires defining two parameter lists: ``app_infer_params`` and ``model_infer_params``. In the case of LightGBM, both lists are empty.





Parameter file
---------------------------------
The parameter file is a `txt` file that contains default parameters for all three scripts.
The path to this file is passed to ``frm.initialize_parameters()`` as arg ``default_model``.
The functionality enabling ``frm.initialize_parameters()`` is provided by the `CANDLE library <https://candle-lib.readthedocs.io/en/latest/index.html#>`_.

Example of passing the parameter file to the ``frm.initialize_parameters()``.

.. code-block:: python

    filepath = Path(__file__).resolve().parent 

    params = frm.initialize_parameters(
        filepath,
        default_model="lgbm_params.txt",
        additional_definitions=additional_definitions,
        required=None,
    )

Example showing the content of the parameter file for LightGBM.

.. code-block:: text

    [Global_Params]
    model_name = "LGBM"

    [Preprocess]
    train_split_file = "CCLE_split_0_train.txt"
    val_split_file = "CCLE_split_0_val.txt"
    test_split_file = "CCLE_split_0_test.txt"
    ml_data_outdir = "./ml_data/CCLE-CCLE/split_0"
    data_format = ".parquet"
    y_data_files = [["response.tsv"]]
    x_data_canc_files = [["cancer_gene_expression.tsv", ["Gene_Symbol"]]]
    x_data_drug_files = [["drug_mordred.tsv"]]
    use_lincs = True
    scaling = "std"

    [Train]
    train_ml_data_dir = "./ml_data/CCLE-CCLE/split_0"
    val_ml_data_dir = "./ml_data/CCLE-CCLE/split_0"
    model_outdir = "./out_models/CCLE/split_0"
    model_file_name = "model"
    model_file_format = ".txt"

    [Infer]
    test_ml_data_dir = "./ml_data/CCLE-CCLE/split_0"
    model_dir = "./out_models/CCLE/split_0"
    infer_outdir = "./out_infer/CCLE-CCLE/split_0"




References
---------------------------------
`1. <https://www.frontiersin.org/articles/10.3389/fmed.2023.1086097/full>`_ A. Partin et al. "Deep learning methods for drug response prediction in cancer: Predominant and emerging trends", Frontiers in Medicine, Section Prediction Oncology, 2023
