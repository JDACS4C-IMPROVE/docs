Utility Functions
====================
NATASHA: fill this in

The following functions are part of improvelib and should be used to standardize aspects of the workflow.

.. topic:: build_ml_data_file_name

    Returns the name of the ML data file in the form of <stage>_data.<format>, e.g. train_data.pt.

    Used in *preprocess*, *train*, and *infer*.

    Inputs:
        data_format (str)
        
        stage (str)
    
    Returns:
        str: data file name

.. topic:: build_model_path

    Returns the path to save/load the trained model.

    Used in *train* and *infer*.

    Inputs:
        model_file_name (str): Name of model file.

        model_file_format (str): Type of file for model (e.g. '.pt').

        model dir (Path or str): Directory path to save the model.

    Returns:
        pathlib.Path: path to model.

save_stage_ydf

store_predictions_df

compute_performance_scores

