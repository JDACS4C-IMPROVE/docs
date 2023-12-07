Unified Interface
===========================

The IMPROVE comparison workflows require that prediction models conform a unitified code interface.

Supervised learning models generally consist of three primary components, including data preparation, model development training and hyperparameter optimisation, and performance evaluation [ref paper].
We propose to separate the model code into three distinct interfaces to facilitate code readability, provenance and maintainability.
The first interface handles **preprocessing** of input data, the second is responsible for model **training**, and the third handles model **inference**.
All these should be structured in a modular and flexible way to allow for tractable combination and workflow generation.

| Model repositories should provide a python script for each of the three steps:
| 1. **Preprocessing.** Preprocessing transforms general input data related to the prediction problem (e.g., drug response prediction) into model specific input data. It transforms the input format into a model specific format, e.g. csv into hdf5 or pt (if using PyTorch data loaders).
| 2. **Training.** Training and optimization of the model. This often includes hyperparameter optimization and early stopping with validation data to mitigate overfitting [link to workflow].
| 3. **Inference.** Using the preprocessed data and the trained model to prediction and evaluate model prediction performance.

.. This step invloves transforming __raw__ data into data formats that [conform ML/DL frameworks APIs] can supplied to ML models.
[Add schematic]

..
    In the following [TODO]:
    * Example templates of the three scripts (the use case is drug response prediction)
    * Inputs and outputs (defaults and methods to set the arguments, required and optional)
    * Example with LightGBM
    * Structure of the benchmark dataset

| In the template scripts below, we designate required and optional code sections.
* Required sections refer to functionality that models must intergrate in their scripts and specifically use the provided framework functionality (designated with *[Req]*). For example:
.. code-block:: python

    filepath = Path(__file__).resolve().parent # [Req]
* Optional sections refer to common steps involved in ML model development that are either optional or implementation depends on the model itself. Optional sections are designated with "[Optional]".

The design of code, including keyword arguments and functionality, can be grouped on three levels: framework, scientific problem (e.g., drug response prediction), model (e.g., LightGBM).

Find below specifications for each of the three scripts, including examples for utilizing LightGBM for drug response prediction (DRP).

There are several components to the model repo:

1. Python scripts for [modelname]_preprocess_improve.py, [modelname]_train_improve.py, [modelname]_inference_improve.py
2. Benchmark data (e.g., CSA data)
3. Parameter file

Preprocessing
---------------------------------
.. TODO] consider create a table
This is a preprocessing script that takes benchmark data (e.g., CSA data [link]) and generates datasets for the prediction model.

The preprocessing script name should follow the following naming convention: `MODELNAME_preprocess_improve.py`. For example: `lgbm_preprocess_imporve.py`

| **Required outputs**: 
All the outputs from the preprocessing script are saved in ``params["ml_data_outdir"]``.

1. Model input data files.
    Data files that are used as inputs to the ML/DL model. The file format is specified by ``params["data_format"]``. The script creates three files corresponding to train, validation, and test data.
2. Y data files.
    Dataframes with true y values and additional metadata. The script creates ``train_y_data.csv``, ``val_y_data.csv``, and ``test_y_data.csv``.



Import the `imporve` library and the python module `drug_resp_pred`. The `improve` lib contains common arguments

.. code-block:: python

    from improve import framework as frm
    from improve import drug_resp_pred as drp
* Create two lists of directories. Each dict specifies an keyword arguments.

Both lists must be defined in the script.

The list app_preproc_params must be copied here as is.
The [Req] indicates the args that must be specified by each model.

.. code-block:: python

    # [Req] App-specific params (App: monotherapy drug response prediction)
    # TODO: consider moving this list to drug_resp_pred.py module
    # The list app_preproc_params must be copied here as is.
    # The [Req] indicates that the args must be specified for the model.
    
    app_preproc_params = [
        # These arg should be specified in the [modelname]_default_model.txt:
        # y_data_files, x_data_canc_files, x_data_drug_files
        {"name": "y_data_files", # default
        "type": str,
        "help": "List of files that contain the y (prediction variable) data. \
                Example: [['response.tsv']]",
        },
        {"name": "x_data_canc_files", # [Req]
        "type": str,
        "help": "List of feature files including gene_system_identifer. Examples: \n\
                1) [['cancer_gene_expression.tsv', ['Gene_Symbol']]] \n\
                2) [['cancer_copy_number.tsv', ['Ensembl', 'Entrez']]].",
        },
        {"name": "x_data_drug_files", # [Req]
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

All args in model_preproc_params are optional. If no args are required by the model, then it should be an empty list.
# [Optional] Model-specific params (Model: LightGBM)
# All args in model_preproc_params are optional. If no args are required by the model, then it should be an empty list.

.. code-block:: python

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


Training
---------------------------------
* Script name: `MODELNAME_train_improve.py`. For example: `lgbm_train_imporve.py`
* Import the `imporve` library and the python module `drug_resp_pred`


Inference
---------------------------------
* Script name: `MODELNAME_infer_improve.py`. For example: `lgbm_infer_imporve.py`
* Import the `imporve` library and the python module `drug_resp_pred`



We saw in the previous example how to create a candle benchmark. Now we will use
the ``candle.file_utils`` methods to set up our input and output directories. Building
on the previous example, we will extend our Example model to load data. The general
functionality is that if the data exists in the data directory, use it, otherwise download
it and then use it.

----


.. code-block:: python

    from improve import framework as frm
    from improve import drug_resp_pred as drp

    # Set up input and output directory paths. These will always be
    # relative to os.environ['CANDLE_DATA_DIR'].
    data_dir = gParameters["data_dir"]
    output_dir = gParameters["output_dir"]
    # the following is incorrect and appends extra subdirectories to the path
    # data_dir, output_dir = directory_tree_from_parameters(gParameters)
    print('data_dir: {}\noutput_dir: {}'.format(data_dir, output_dir))

    # prints:
    # data_dir:   /tmp/improve_data_dir/Example/Data
    # putput_dir: /tmp/improve_data_dir/Example/Output/EXP000/RUN000

    # Get machine learning data
    download_filepath = candle.get_file(
        gParameters['train_data'],
        gParameters['data_url'] + "/" + gParameters['train_data']
        datadir = data_dir  # This puts the files in correct path
        cache_subdir = None  # This prevents get_file from creating another subdirectory
    )
    print('download_path: {}'.format(download_filepath))

    # prints:
    # download_path: /tmp/improve_data_dir/Example/Data/example.csv


----

The code above uses the environment variable CANDLE_DATA_DIR as the root to all input
and output paths.

Two new keyword = value pairs are needed in the default model file - ``example_default_model.txt``. These are
``data_url`` and ``train_data``. Additionally, I had to upload ``example.csv`` to
https://ftp.mcs.anl.gov/pub/candle/public/improve/examples


.. code-block:: text
    
    # set location and name of training data
    data_url="https://ftp.mcs.anl.gov/pub/candle/public/improve/examples"
    train_data="example.csv"

----

Putting this together into a running example looks like this:

.. code-block:: python

    import os
    import candle
    # from candle.file_utils import directory_tree_from_parameters
    # from candle.file_utils import get_file
    # from candle import Benchmark
    # from candle import finalize_parameters

    # set CANDLE_DATA_DIR env var. This is normally set externally.
    os.environ['CANDLE_DATA_DIR'] = '/tmp/improve_data_dir'

    # get the directory of this script, so that the default_model.txt
    # file can be found when the benchmark is instanciated.
    filepath = os.path.dirname(os.path.abspath(__file__))

    imp_bmk=candle.Benchmark(
        filepath=filepath,
        defmodel="example_default_model.txt",
        framework="tensorflow"
    )

    # Initialize parameters
    gParameters = candle.finalize_parameters(imp_bmk)

    # Set up input and output directory paths. These will always be
    # relative to os.environ['CANDLE_DATA_DIR'].
    # data_dir, output_dir = directory_tree_from_parameters(gParameters)
    print('data_dir: {}\noutput_dir: {}'.format(gParameters{"data_dir"], gParameters{"output_dir"]))

    # data_dir:   /tmp/improve_data_dir/Example/Data
    # putput_dir: /tmp/improve_data_dir/Example/Output/EXP000/RUN000

    # Get machine learning data
    download_filepath = candle.get_file(
        gParameters['train_data'],
        gParameters['data_url'] + "/" + gParameters['train_data']
        datadir = data_dir  # This puts the files in correct path
        cache_subdir = None  # This prevents get_file from creating another subdirectory
    )
    print('download_path: {}'.format(download_filepath))

This code produces the following output. The first output, model_name and Params come
from the call to finalize_parameters. The rest is print statements in the code above.

.. code-block:: text
    
 $ python ./example.py
 
 model name:  "Example"

 Params:
 {'ckpt_checksum': False,
 'ckpt_directory': './save',
 'ckpt_keep_limit': 1000000,
 'ckpt_keep_mode': 'linear',
 'ckpt_restart_mode': 'auto',
 'ckpt_save_best': True,
 'ckpt_save_best_metric': 'val_loss',
 'ckpt_save_interval': 0,
 'ckpt_save_weights_only': False,
 'ckpt_skip_epochs': 0,
 'data_dir': '/tmp/improve_data_dir/Example/Data',
 'data_type': <class 'numpy.float32'>,
 'data_url': 'https://ftp.mcs.anl.gov/pub/candle/public/improve/examples',
 'experiment_id': 'EXP000',
 'logfile': None,
 'model_name': 'Example',
 'output_dir': '/tmp/improve_data_dir/Example/Output/EXP000/RUN000',
 'profiling': False,
 'rng_seed': 7102,
 'run_id': 'RUN000',
 'shuffle': False,
 'timeout': -1,
 'train_bool': True,
 'train_data': 'example.csv',
 'verbose': False}

 data_dir: /tmp/improve_data_dir/Example/Data
 output_dir: /tmp/improve_data_dir/Example/Output/EXP000/RUN000
 download_path: /tmp/improve_data_dir/Example/Data/example.csv

The code for this example can be found at https://github.com/JDACS4C-IMPROVE/docs/tree/main/example_code
in the example.py and example_default_model.txt files.
