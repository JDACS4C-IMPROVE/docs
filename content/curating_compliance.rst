Ensuring the Curated Model is IMPROVE-compliant
==================================================

Following is a list of requirements for a curated model to be IMPROVE-compliant. Adhering to these requirements will allow
the model to function with IMPROVE :doc:`workflows <USING>`.

File naming conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^
<model>_preprocess_improve.py
<model>_train_improve.py
<model>_infer_improve.py
<model>_params.ini
model_params_def.py
<model>_environment.yml

All three (preprocess, train, infer) scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Use :code:`main()` which should:

    * Set params with appropriate stage/application config
    * Records the time to run :code:`run()` with :code:`from improvelib.utils import Timer`
    * Calls :code:`run()` which runs the code and returns:

        * preprocess: returns :code:`output_dir`
        * train: returns :code:`val_scores`
        * infer: returns :code:`True`


Preprocess
^^^^^^^^^^^^^^^^^^
* Uses the application-appropriate data loader
* Saves X data
* Saves Y data using :code:`save_stage_ydf()`

Train
^^^^^^^^^^^^^^^^^^
* Saves model with model path determined by :code:`build_model_path()`
* Saves val predictions with :code:`store_predictions_df()`
* Saves val scores using :code:`compute_performance_scores()`
* Early stopping using the param :code:`patience`
* The model should use GPU by default

Infer
^^^^^^^^^^^^^^^^^^
* Uses model loaded with model path determined by :code:`build_model_path()`
* Saves test predictions with :code:`store_predictions_df()`
* Has option to save test scores using :code:`compute_performance_scores()` if param :code:`calc_infer_scores` is true
* The model should use GPU by default

Parameters and Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Model-specific parameters must not include parameters defined in IMPROVE 
(see parameters for :doc:`preprocess <api_preprocess>`, :doc:`train <api_train>`, and :doc:`infer <api_infer>`).
* All IMPROVE-defined parameters that are used by the model should be used via the IMPROVE parameters

    * E.g. :code:`params['patience']` should be used instead of a model defined :code:`early_stop` or simply :code:`100` in train.
    * Model-specific parameters that users may want to change should also utilize IMPROVE parameter handling.
* IMPROVE-defined parameters that are not used by the model should be set to :code:`None` in the config file.

Model Repository
^^^^^^^^^^^^^^^^^^
* The readme should be updated and follow this :doc:`template <curating_templates_readme>`
* The repo should include :code:`setup_improve.sh` with this :doc:`template <curating_templates_downloads>`

    * :code:`download_csa.sh` should be present in the repo
    * If supplemental data not included in the benchmark data is needed by the model, it should be downloaded via a shell script present 
    in the repo and this script should be included in :code:`setup_improve.sh` 
    * The param :code:`input_supp_data_dir` should be used in preprocess to denote the default location of this data as downloaded by :code:`setup_improve.sh`


