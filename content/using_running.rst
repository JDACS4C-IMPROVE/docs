Running a Curated Model
=================================

For a step-by-step example of how run LGBM see: :doc:`quickstartguide`.

1. Clone the model and set up the environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* IMPROVE model repositories can be found here: `https://github.com/JDACS4C-IMPROVE <https://github.com/JDACS4C-IMPROVE>`_. Clone the model repo with:

 .. code-block::

  git clone <model_repo>
  cd <model_repo>

* Set up the environment according to the instructions. The IMPROVE library is installed with:

 .. code-block::

  pip install improvelib

2. Download the benchmark data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To download Drug Response Prediction benchmark data, run the following in the directory where you would like to store the data:

 .. code-block::

  wget --cut-dirs=8 -P ./ -nH -np -m https://web.cels.anl.gov/projects/IMPROVE_FTP/candle/public/improve/benchmarks/single_drug_drp/benchmark-data-pilot1/csa_data/

3. Run the model scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By default everything will be saved in the current working directory. This, and all other parameters can be changed by setting parameters on the command line. See :doc:`api_parameters` for more information about parameters.

 .. code-block::

  python <model>_preprocess_improve.py --input_dir /path/to/dir/csa_data/raw_data
  python <model>_train_improve.py
  python <model>_infer_improve.py


