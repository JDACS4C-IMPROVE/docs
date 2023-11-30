Module improve.csa
==================
Functionality for Cross-Study Analysis (CSA) in IMPROVE.

Functions
---------

    
`directory_tree_from_parameters(params: Dict, raw_data_check: Callable = None, step: str = 'preprocess') ‑> Tuple[Deque, Optional[improve.framework.DataPathDict]]`
:   Check input data and construct output directory trees from parameters for cross-study analysis (CSA).
    
    Input and output structure depends on step.
    For preprocess step, input structure is represented by DataPathDict.
    In other steps, raw input is None and the output queue contains input and output paths.
    
    :param Dict params: Dictionary of parameters read
    :param Callable raw_data_check: Function that checks raw data input and returns paths to x-data/y-data/splits.
    :param string step: String to specify if this is applied during preprocess, train or test.
    
    :return: Paths and info about processed data output directories and raw data input.
    :rtype: (Deque, (Path, Path, Path))

    
`initialize_parameters(filepath, default_model='csa_default_model.txt', additional_definitions=None, required=None, topop=None)`
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

Classes
-------

`CSAImproveBenchmark(filepath: str, defmodel: str, framework: str, prog: str = None, desc: str = None, parser=None, additional_definitions=None, required=None)`
:   Benchmark for Cross-Study Analysis (CSA) Improve Models. 
    
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

    * improve.framework.ImproveBenchmark
    * candle.benchmark_def.Benchmark

    ### Methods

    `read_config_file(self, file: str)`
    :   Functionality to read the configue file specific for each
        benchmark.
        
        :param string file: path to the configuration file
        
        :return: parameters read from configuration file
        :rtype: ConfigDict

`DataSplit(dsource: str, dtarget: str, sindex: int, tindex: int)`
:   Define structure of information for split.