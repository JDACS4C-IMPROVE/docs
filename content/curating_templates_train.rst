Training Template
====================

Below is a template in which you should place your model training code.
All the outputs from this train script are saved in :code:`params["output_dir"]`.

- Trained model: trained with train data and validated with val data. The model file name and file format are specified, respectively by :code:`params["model_file_name"]` and :code:`params["model_file_format"]`.

- Predictions on val data: raw model predictions using the trained model on val data. The predictions are saved in :code:`val_y_data_predicted.csv`.

- Prediction performance scores on val data: calculated using the raw model predictions and the true values for performance metrics specified by :code:`metric_type`. The scores are saved as json in :code:`val_scores.json`.

.. code-block:: python

    import sys
    from pathlib import Path
    from typing import Dict
    # [Req] IMPROVE imports
    from improvelib.applications.drug_response_prediction.config import DRPTrainConfig
    from improvelib.utils import str2bool
    import improvelib.utils as frm
    from improvelib.metrics import compute_metrics
    from model_params_def import train_params
    # [MODEL] Model-specific imports, as needed

    # [Req]
    filepath = Path(__file__).resolve().parent 

    # [Req]
    def run(params: Dict):
        """ Run model training.

        Args:
            params (dict): dict of IMPROVE parameters and parsed values.

        Returns:
            dict: performance scores computed on val data.
        """
        # --------------------------------------------------------------------
        # [Req] Create data names for train/val sets and build model path
        # --------------------------------------------------------------------
        train_data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="train") 
        val_data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="val")

        modelpath = frm.build_model_path(
            model_file_name=params["model_file_name"], 
            model_file_format=params["model_file_format"], 
            model_dir=params["output_dir"])

        # --------------------------------------------------------------------
        # [MODEL] Load model input data (ML data) for train and val
        # --------------------------------------------------------------------

        # --------------------------------------------------------------------
        # [MODEL] CUDA/CPU device, as needed
        # --------------------------------------------------------------------

        # --------------------------------------------------------------------
        # [MODEL] Prepare model
        # --------------------------------------------------------------------

        # --------------------------------------------------------------------
        # [MODEL] Train. Iterate over epochs.
        # --------------------------------------------------------------------

        # --------------------------------------------------------------------
        # [MODEL] Load best model and compute predictions
        # --------------------------------------------------------------------

        # --------------------------------------------------------------------
        # [Req] Save raw predictions in dataframe
        # --------------------------------------------------------------------
        frm.store_predictions_df(
            y_true=your_val_true, 
            y_pred=your_val_predicted, 
            stage="val",
            y_col_name=params["y_col_name"],
            output_dir=params["output_dir"]
        )

        # --------------------------------------------------------------------
        # [Req] Compute performance scores
        # --------------------------------------------------------------------
        val_scores = frm.compute_performance_scores(
            y_true=your_val_true, 
            y_pred=your_val_predicted, 
            stage="val",
            metric_type=params["metric_type"],
            output_dir=params["output_dir"]
        )

        return val_scores


    # [Req]
    def main(args):
        cfg = DRPTrainConfig()
        params = cfg.initialize_parameters(
            pathToModelDir=filepath,
            default_config="MODEL_params.txt",
            additional_definitions=train_params)
        val_scores = run(params)
        print("\nFinished training model.")


    # [Req]
    if __name__ == "__main__":
        main(sys.argv[1:])