Inference Template
======================

Below is a template in which you should place your model inference code.

All the outputs from this train script are saved in :code:`params["output_dir"]`.

- Predictions on test data: raw model predictions using the trained model on test data. The predictions are saved in :code:`test_y_data_predicted.csv`.

- Prediction performance scores on test data: calculated using the raw model predictions and the true values for performance metrics specified by :code:`metric_type`. The scores are saved as json in :code:`test_scores.json`.


.. code-block:: python

    import sys
    from pathlib import Path
    from typing import Dict
    # [Req] IMPROVE imports
    from improvelib.applications.drug_response_prediction.config import DRPInferConfig
    from improvelib.utils import str2bool
    import improvelib.utils as frm
    from model_params_def import infer_params
    # [MODEL] Model-specific imports, as needed

    # [Req]
    filepath = Path(__file__).resolve().parent 


    # [Req]
    def run(params):
        """ Run model inference.

        Args:
            params (dict): dict of IMPROVE parameters and parsed values.

        Returns:
            dict: prediction performance scores computed on test data.
        """
        # --------------------------------------------------------------------
        # [Req] Create data names for test set and build model path
        # --------------------------------------------------------------------
        test_data_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="test")
        modelpath = frm.build_model_path(
            model_file_name=params["model_file_name"], 
            model_file_format=params["model_file_format"], 
            model_dir=params["input_model_dir"])

        # --------------------------------------------------------------------
        # [MODEL] Load inference data (ML data)
        # --------------------------------------------------------------------

        # --------------------------------------------------------------------
        # [MODEL] CUDA/CPU device, as needed
        # --------------------------------------------------------------------

        # --------------------------------------------------------------------
        # [MODEL] Load best model and compute predictions
        # --------------------------------------------------------------------

        # ------------------------------------------------------
        # [Req] Save raw predictions in dataframe
        # ------------------------------------------------------
        frm.store_predictions_df(
            y_true=your_test_true, 
            y_pred=your_test_predicted, 
            stage="test",
            y_col_name=params["y_col_name"],
            output_dir=params["output_dir"]
        )

        # ------------------------------------------------------
        # [Req] Compute performance scores
        # ------------------------------------------------------
        if params["calc_infer_scores"]:
            test_scores = frm.compute_performance_scores(
                y_true=your_test_true, 
                y_pred=your_test_predicted, 
                stage="test",
                metric_type=params["metric_type"],
                output_dir=params["output_dir"]
            )

        return True


    # [Req]
    def main(args):
        cfg = DRPInferConfig()
        params = cfg.initialize_parameters(
            pathToModelDir=filepath,
            default_config="MODEL_params.txt",
            additional_definitions=infer_params,
        )
        status = run(params)
        print("\nFinished model inference.")


    # [Req]
    if __name__ == "__main__":
        main(sys.argv[1:])
