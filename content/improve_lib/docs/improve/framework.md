Module improve.framework
========================
Basic definitions for IMPROVE framework.

Functions
---------

    
`build_ml_data_name(params: Dict, stage: str)`
:   Returns name of the ML/DL data file. E.g., train_data.pt
    TODO: params is not currently needed here. Consider removing this input arg.
    TODO: consider renaming build_ml_data_file_name()
    Used in *preprocess*.py*, *train*.py, and *infer*.py

    
`build_model_path(params: Dict, model_dir: Union[pathlib.Path, str])`
:   Returns path to store the trained model. Creates dir if needed.
    Used in *train*.py and *infer*.py

    
`build_paths(params)`
:   Build paths for raw_data, x_data, y_data, splits.
    These paths determine directories for benchmark datasets.
    TODO: consider renaming to build_benchmark_data_paths()

    
`check_path(path)`
:   

    
`check_path_and_files(folder_name: str, file_list: List, inpath: pathlib.Path) ‑> pathlib.Path`
:   Checks if a folder and its files are available in path.
    
    Returns a path to the folder if it exists or raises an exception if it does
    not exist, or if not all the listed files are present.
    
    :param string folder_name: Name of folder to look for in path.
    :param list file_list: List of files to look for in folder
    :param inpath: Path to look into for folder and files
    
    :return: Path to folder requested
    :rtype: Path

    
`compute_performace_scores(params: Dict, y_true: <built-in function array>, y_pred: <built-in function array>, stage: str, outdir: Union[pathlib.Path, str], metrics: List)`
:   Evaluate predictions according to specified metrics.
    
    Metrics are evaluated. Scores are stored in specified path and returned.
    
    :params array y_true: Array with ground truth values.
    :params array y_pred: Array with model predictions.
    :params listr metrics: List of strings with metrics to evaluate.
    :params Dict outdtd: Dictionary with path to store scores.
    :params str stage: String specified if evaluation is with respect to
            validation or testing set.
    
    :return: Python dictionary with metrics evaluated and corresponding scores.
    :rtype: dict

    
`create_outdir(outdir: Union[pathlib.Path, str])`
:   Create directory.

    
`get_file_format(file_format: Optional[str] = None)`
:   Clean file_format.
    Exmamples of (input, return) pairs:
    input, return: "", ""
    input, return: None, ""
    input, return: "pt", ".pt"
    input, return: ".pt", ".pt"

    
`initialize_parameters(filepath, default_model='frm_default_model.txt', additional_definitions=None, required=None)`
:   Parse execution parameters from file or command line.
    
    Parameters
    ----------
    default_model : string
        File containing the default parameter definition.
    additional_definitions : List
        List of additional definitions from calling script.
    required: Set
        Required arguments from calling script.
    
    Returns
    -------
    gParameters: python dictionary
        A dictionary of Candle keywords and parsed values.

    
`save_stage_ydf(ydf: pandas.core.frame.DataFrame, params: Dict, stage: str)`
:   Save a subset of y data samples (rows of the input dataframe).
    The "subset" refers to one of the three stages involved in developing ML
    models, including: "train", "val", or "test".
    
    ydf : dataframe with y data samples
    params : parameter dict
    stage (str) : "train", "val", or "test"

    
`store_predictions_df(params: Dict, y_true: <built-in function array>, y_pred: <built-in function array>, stage: str, outdir: Union[pathlib.Path, str], round_decimals: int = 4)`
:   Store predictions with accompanying data frame.
    
    This allows to trace original data evaluated (e.g. drug and cell
    combinations) if corresponding data frame is available, in which case
    the whole structure as well as the model predictions are stored. If
    the data frame is not available, only ground truth (read from the
    PyTorch processed data) and model predictions are stored. The ground
    truth available (from data frame or PyTorch data) is returned for
    further evaluations.
    
    ap: construct output file name as follows:
            
            [stage]_[params['y_data_suffix']]_
    
    :params Dict params: Dictionary of CANDLE/IMPROVE parameters read.
    :params Dict indtd: Dictionary specifying paths of input data.
    :params Dict outdtd: Dictionary specifying paths for ouput data.
    :params array y_true: Ground truth.
    :params array y_pred: Model predictions.
    
    :return: Arrays with ground truth. This may have been read from an
             input data frame or from a processed PyTorch data file.
    :rtype: np.array

Classes
-------

`ImproveBenchmark(filepath: str, defmodel: str, framework: str, prog: str = None, desc: str = None, parser=None, additional_definitions=None, required=None)`
:   Benchmark for Improve Models. 
    
    Initialize Benchmark object.
    
    :param string filepath: ./
        os.path.dirname where the benchmark is located. Necessary to locate utils and
        establish input/ouput paths
    :param string defmodel: 'p*b*_default_model.txt'
        string corresponding to the default model of the benchmark
    :param string framework : 'keras', 'neon', 'mxnet', 'pytorch'
        framework used to run the benchmark
    :param string prog: 'p*b*_baseline_*'
        string for program name (usually associated to benchmark and framework)
    :param string desc: ' '
        string describing benchmark (usually a description of the neural network model built)
    :param argparser parser: (default None)
        if 'neon' framework a NeonArgparser is passed. Otherwise an argparser is constructed.

    ### Ancestors (in MRO)

    * candle.benchmark_def.Benchmark

    ### Descendants

    * improve.csa.CSAImproveBenchmark

    ### Methods

    `set_locals(self)`
    :   Set parameters for the benchmark.
        
        Parameters
        ----------
        required: set of required parameters for the benchmark.
        additional_definitions: list of dictionaries describing the additional parameters for the
            benchmark.