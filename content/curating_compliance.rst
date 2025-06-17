Ensuring the Curated Model is IMPROVE-compliant
==================================================

Following is a list of requirements for a curated model to be IMPROVE-compliant. Adhering to these requirements will allow
the model to function with IMPROVE :doc:`workflows <USING>`.


Required files and their naming conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A list of files required for compliance, along with their standardized naming patterns:

* ``<model>_preprocess_improve.py``
* ``<model>_train_improve.py``
* ``<model>_infer_improve.py``
* ``<model>_params.ini``
* ``model_params_def.py``
* ``<model>_environment.yml``


All three stage scripts (preprocess, train, infer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each of the three stage scripts uses a :code:`main()` function that:

* Sets params with the appropriate stage/application config
* Records execution time of :code:`run()` using :code:`from improvelib.utils import Timer`.
* Calls :code:`run()`, which executes the stage-specific code and returns:

  - **Preprocessing**: :code:`output_dir`
  - **Training**: :code:`val_scores`
  - **Inference**: :code:`True`


Preprocessing
^^^^^^^^^^^^^^^^^^^

* **Use the appropriate data loader** for your application.
* **Save the X data** (features).
* **Save the Y data** using :code:`save_stage_ydf()`.


Training
^^^^^^^^^^^^^^

* **Save the model** using a path determined by :code:`build_model_path()`.
* **Save validation predictions** with :code:`store_predictions_df()`.
* **Save validation scores** using :code:`compute_performance_scores()`.
* **Implement early stopping** and use the :code:`patience` parameter.
* **Use a GPU by default**, if available.


Inference
^^^^^^^^^^^^^^^

* **Load the model** using a path determined by :code:`build_model_path()`.
* **Save test predictions** with :code:`store_predictions_df()`.
* **Optionally save test scores** using :code:`compute_performance_scores()` if :code:`calc_infer_scores` is set to ``True``.
* **Use a GPU by default**, if available.


Parameters and configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Avoid duplicating IMPROVE-defined parameters**
  While you can define model-specific parameters, do not redefine those already established by IMPROVE. Refer to the IMPROVE-defined parameters for :doc:`preprocess <api_preprocess>`, :doc:`train <api_train>`, and :doc:`infer <api_infer>` as needed.

* **Use IMPROVE-defined parameters for consistent handling**
  If your model relies on an IMPROVE-defined parameter, access it via the IMPROVE :code:`params` rather than creating a separate variable or using a hard-coded value. For example, use :code:`params['patience']` instead of introducing a new model-specific parameter (e.g., :code:`early_stop`) or typing a value directly (e.g., :code:`100`). Additionally, any model-specific parameter that users may need to adjust should integrate with the IMPROVE parameter handling system.

* **Set unused IMPROVE-defined parameters to :code:`None`**
  If your model does not require a particular IMPROVE-defined parameter, set it to :code:`None` in the config file. This ensures clarity about which parameters are actually used.


Model repository
^^^^^^^^^^^^^^^^^^

* **README**

  - Follow the :doc:`template <curating_templates_readme>` to ensure a unified structure.

* **Include a :code:`setup_improve.sh` script**

  - Base it on this :doc:`template <curating_templates_downloads>`.
  - Ensure :code:`download_csa.sh` is present in the repo.
  - If the model requires supplemental data (not included in the benchmark data), it should be downloaded via a shell script present in the repo, and this script should be integrated in :code:`setup_improve.sh`
  - In the preprocessing stage, use the :code:`input_supp_data_dir` parameter to specify the default location where :code:`setup_improve.sh` places any supplemental data.
