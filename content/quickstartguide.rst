Quickstart
=================================
This quickstart guide is intended to help you install IMPROVE within a conda environment and run preprocessing, train, and infer using a curated model and benchmark datasets.
Here, we demonstrate how to use LGBM, a standardized IMPROVE model built with the LightGBM package, to predict drug response using curated a Drug Response Dataset. This walkthrough will guide you through the essential steps involved in utilizing IMPROVE for drug response prediction.

Requirements
-----------------------------

- `git <https://github.com>`_
- `conda <https://docs.conda.io/en/latest/>`_


Clone Model
-----------------------------
Repositories for all curated models can be found on the `IMPROVE GitGub <https://github.com/JDACS4C-IMPROVE/>`_. 
A list of drug response prediction models can be found here: :doc:`app_drp_models`. 
Here we clone the LGBM model.

.. code-block:: bash

    git clone https://github.com/JDACS4C-IMPROVE/LGBM
    cd LGBM
    git checkout v0.1.0



Download Benchmark Dataset
-----------------------------
IMPROVE uses publicly available datasets that have been standardized and harmonized for use in assessing machine learning algorithms. 
Here we download the Drug Response Prediction Benchmark Dataset (CSA data). There are two options to download this data.

A. Using :code:`wget`

.. code-block:: bash

    cd LGBM
    wget https://web.cels.anl.gov/projects/IMPROVE_FTP/candle/public/improve/benchmarks/single_drug_drp/benchmark-data-pilot1/csa_data/

B. Using `download_csa` script

.. code-block:: bash

    cd LGBM
    sh ./download_csa.sh


Set up Environment
-----------------------------
Each model has specific package requirements, which are detailed in the README file of their respective repositories.
Here we create a conda environment to install the necessary packages for LGBM and the IMPROVE library.

.. code-block:: bash

    conda create -n LGBM python=3.7 pip lightgbm=3.1.1 --yes
    conda activate LGBM
    pip install pyarrow==12.0.1
    pip install improvelib==0.1.0


Run preprocessing script
-----------------------------
The preprocessing script takes the raw benchmark data, standardized by the IMPROVE project (CSA data), and transforms it into a model-compatible format. This process generates train, validation, and test data files, which will be utilized in the subsequent training and inference steps.
Here we run preprocessing for LGBM.

.. code-block:: bash

    python lgbm_preprocess_improve.py --input_dir ./csa_data/raw_data --output_dir exp_result


Run training script
-----------------------------
The training script uses the training data to train the model and the validation data for early stopping. Upon completion, this process generates the trained model, predictions on the validation data, and corresponding performance scores.
Here we run training for LGBM.

.. code-block:: bash

    python lgbm_train_improve.py --input_dir exp_result --output_dir exp_result


Run inference script
-----------------------------
The inference script uses the previously trained model to generate drug response predictions for the test set, subsequently computing prediction performance scores (e.g., r-squared).
Here we run inference for LGBM.

.. code-block:: bash

    python lgbm_infer_improve.py --input_data_dir exp_result --input_model_dir exp_result --output_dir exp_result --calc_infer_score true


Output
-----------------------------
By default the output from all scripts is saved in the current working directory. In this example, everything is saved in :code:`exp_result`.

- **Preprocess**: the ML data (model input data)

- **Train**
  
  - the saved model (here :code:`model.txt`)
  - the validation data performance scores (:code:`val_scores.json`)
  - the predicted response data on the validation set (:code:`val_y_data_predicted.csv`)

- **Infer**
  
  - the test data performance scores (:code:`test_score.json`)
  - the predicted response data on the test data (:code:`test_y_data_predicted.csv`)