Quickstart
=================================
This quickstart guide is intended to help you install IMPROVE within a conda environment and preprocessing, train, and infer using a curated model and benchmark datasets.
Here we use LGBM as a example of a model in the IMPROVE framework to walk throught the necessary steps to predict drug response using curated IMPROVE Drug Response Datasets.


Requirements
--------------

- `git <https://github.com>`_
- `conda <https://docs.conda.io/en/latest/>`_


Clone a Model of Interest
---------------------------
Repositories for all curated models can be found on the `IMPROVE github <https://github.com/JDACS4C-IMPROVE/>`_. 
A list of Drug Response Prediction models can be found here: :doc:`app_drp_models`. 
Here we clone the LGBM model.

.. code-block:: bash

    git clone https://github.com/JDACS4C-IMPROVE/LGBM


Download Benchmark Dataset
-----------------------------
IMPROVE uses publicly available datasets that have been standardized and harmonized for use in assessing machine learning algorithms. 
Here we download the Drug Response Prediction Benchmark Dataset (CSA data). There are two options to download this data.

A. Directly with wget

.. code-block:: bash

    cd LGBM
    wget https://web.cels.anl.gov/projects/IMPROVE_FTP/candle/public/improve/benchmarks/single_drug_drp/benchmark-data-pilot1/csa_data/

B. By running the download_csa script

.. code-block:: bash

    cd LGBM
    sh ./download_csa.sh

Set up Environment
-------------------
Each model has specific requirements, details of which can be found in the readme of each model repository.
Here we create a conda environment for the required packages for LGBM and install the IMPROVE library.

.. code-block:: bash

    conda create -n LGBM python=3.7 pip lightgbm=3.1.1 --yes
    conda activate LGBM
    pip install pyarrow==12.0.1
    pip install improvelib


Run preprocessing script
-------------------------
Preprocessing takes the raw data standardized by the IMPROVE project (CSA data), and transforms it into a format appropriate for the model of choice. 
Data will be divided into input data and y data (e.g. drug response as AUC values) for training, validation, and testing sets to be used in the next two steps. 
Here we run preprocessing for LGBM.

.. code-block:: bash

    python lgbm_preprocess_improve.py --input_dir ./csa_data/raw_data --output_dir exp_result


Run training script
---------------------
The training script trains the model of interest, using the validation set for early stopping. 
This will generate the trained model, the predictions on the validation data, and the prediction performance scores on the validation data. 
Here we run training for LGBM.

.. code-block:: bash

    python lgbm_train_improve.py --input_dir exp_result --output_dir exp_result


Run inference script
---------------------
The inference script will use the model trained in the previous step to predict drug response for the test set and evaluate the performance of these predictions. 
Here we run inference for LGBM.

.. code-block:: bash

    python lgbm_infer_improve.py --input_data_dir exp_result --input_model_dir exp_result --output_dir exp_result --calc_infer_score true


Output
-------
By default the output from all scripts is saved in the current working directory. In this example, everything is saved in :code:`exp_result`.

- Preprocess: the ML data (model input data)

- Train:
  - the saved model (here :code:`model.txt`) <br>
  - the validation scores (:code:`val_scores.json`) <br>
  - the predicted response data on the validation split (:code:`val_y_data_predicted.csv`) <br>

- Infer:
  - the inference scores (:code:`test_score.json`) <br>
  - the predicted response data on the inference split (:code:`test_y_data_predicted.csv`) <br>