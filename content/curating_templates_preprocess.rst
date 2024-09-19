Preprocessing Template
========================

Below is a template in which you should place your preprocessing code that takes benchmark data (e.g., CSA data) and generates datasets for your prediction model.
All the outputs from this preprocessing script are saved in :code:`params["output_dir"]`.

- Data files corresponding to train, validation, and test data. These data files are used as inputs to the ML/DL model in the train and infer scripts. The file format is specified by :code:`params["data_format"]`.

- Dataframes with true y values and additional metadata.

The file should be named :code:`mymodel_preprocess_improve.py` where 'mymodel' is the name of your model.

.. code-block:: python

    import sys
    from pathlib import Path
    from typing import Dict
    # [Req] Core improvelib imports
    from improvelib.applications.drug_response_prediction.config import DRPPreprocessConfig
    from improvelib.utils import str2bool
    import improvelib.utils as frm
    # [Req] Application-specific (DRP) imports
    import improvelib.applications.drug_response_prediction.drug_utils as drugs_utils
    import improvelib.applications.drug_response_prediction.omics_utils as omics_utils
    import improvelib.applications.drug_response_prediction.drp_utils as drp
    from model_params_def import preprocess_params 
    # [MODEL] Model-specific imports, as needed

    # [Req]
    filepath = Path(__file__).resolve().parent 

    # [Req]
    def run(params: Dict):
        """ Run data preprocessing.

        Args:
            params (dict): dict of IMPROVE parameters and parsed values.

        Returns:
            str: directory name that was used to save the ML data files.
        """
        # --------------------------------------------------------------------
        # [Req] Create data names for train/val/test sets
        # --------------------------------------------------------------------
        data_train_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="train")
        data_val_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="val")
        data_test_fname = frm.build_ml_data_file_name(data_format=params["data_format"], stage="test")

        # --------------------------------------------------------------------
        # [Req] Create dataloaders and get response data - DRP specific
        # --------------------------------------------------------------------
        omics_obj = omics_utils.OmicsLoader(params)
        drugs_obj = drugs_utils.DrugsLoader(params)
        response_train = drp.DrugResponseLoader(params,
                                        split_file=params["train_split_file"],
                                        verbose=False).dfs["response.tsv"]
        response_val = drp.DrugResponseLoader(params,
                                        split_file=params["val_split_file"],
                                        verbose=False).dfs["response.tsv"]
        response_test = drp.DrugResponseLoader(params,
                                        split_file=params["test_split_file"],
                                        verbose=False).dfs["response.tsv"]
        # --------------------------------------------------------------------
        # [Req] Load X data (feature representations) - DRP specific
        # --------------------------------------------------------------------
        # Use the provided data loaders to load data required by the model.
        # Drug features: 
        # 'drug_ecfp4_nbits512.tsv', 'drug_mordred.tsv', 'drug_SMILES.tsv'
        # Omics features: 
        # 'cancer_DNA_methylation.tsv', 'cancer_discretized_copy_number.tsv', 
        # 'cancer_copy_number.tsv', 'cancer_mutation_count.tsv', 'cancer_RPPA.tsv'
        # 'cancer_miRNA_expression.tsv', 'cancer_gene_expression.tsv', 
        # Example:
        # ge = omics_obj.dfs['cancer_gene_expression.tsv'] # return gene expression
        # Example:
        # smi = drugs_obj.dfs['drug_SMILES.tsv']  # return SMILES data

        # --------------------------------------------------------------------
        # [MODEL] Preprocess X data
        # --------------------------------------------------------------------
        # Ensure that you match and retain the correct features with responses

        # --------------------------------------------------------------------
        # [MODEL] Save X data 
        # --------------------------------------------------------------------
        # The implementation of this depends on the model.
        # Data must be saved in params["output_dir"].

        # --------------------------------------------------------------------
        # [Req] Save response data (Y data)
        # --------------------------------------------------------------------
        frm.save_stage_ydf(ydf=your_ml_response_train, stage="train", output_dir=params["output_dir"])
        frm.save_stage_ydf(ydf=your_ml_response_val, stage="val", output_dir=params["output_dir"])
        frm.save_stage_ydf(ydf=your_ml_response_test, stage="test", output_dir=params["output_dir"])

        '''
        Alternatively, you can use a loop like so:
        stages = {"train": params["train_split_file"],
                "val": params["val_split_file"],
                "test": params["test_split_file"]}

        for stage, split_file in stages.items():
            rsp = drp.DrugResponseLoader(params,
                                        split_file=split_file,
                                        verbose=False).dfs["response.tsv"]
            rsp = rsp.merge( ge[params["canc_col_name"]], on=params["canc_col_name"], how="inner")
            rsp = rsp.merge(smi[params["drug_col_name"]], on=params["drug_col_name"], how="inner")
            # Preprocessing steps here for this stage
            data.to_parquet(Path(params["output_dir"]) / data_fname) # saves ML data file to parquet
            frm.save_stage_ydf(ydf, params, stage)
        '''

        return params["output_dir"]


    # [Req]
    def main(args):
        cfg = DRPPreprocessConfig()
        params = cfg.initialize_parameters(
            pathToModelDir=filepath,
            default_config="MODEL_params.txt",
            additional_definitions=preprocess_params)
        ml_data_outdir = run(params)
        print("\nFinished data preprocessing.")

    # [Req]
    if __name__ == "__main__":
        main(sys.argv[1:])