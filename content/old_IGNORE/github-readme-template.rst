=================
UNO
=================
-------------------------
Unified-Drug-Response-Predictor
-------------------------

Description
============
The Unified Drug Response Predictor benchmark, also called Uno, is a deep neural network for modeling cell line response to treatments of single or paired drugs. The model takes cell line molecular features, drug properties, and dose information as input and predicts the response in percentage growth. The model uses a multi-tower structure for processing different feature types individually before concatenating them for the final layers. The model also unifies treatment input types of single drugs and drug pairs by allocating two slots for drugs and, in the case of drug pairs, dividing the concentration into the two slots. The authors of this model have integrated datasets from multiple public sources of drug response studies and provided options for training models with selections of subsets.

User Community
============
Cancer biology data modeling; Machine Learning; Bioinformatics; Computational Biology

Usability
============
To use the untrained model, users must be familiar with processing and feature extraction of molecular drug data, gene expression, and training of neural networks. The input to the model is preprocessed data. Users should have extended experience with preprocessing this data.

Uniqueness
============
The community can use a neural network and multiple machine learning techniques to predict drug response. The general rule is that classical methods like random forests would perform better for small datasets, while neural network approaches like Uno would perform better for relatively larger datasets. The baseline for comparison can be: mean response, linear regression, or random forest regression.

Components
============
The following components are in the Model and Data Clearinghouse (MoDaC):
* The [Unified Drug Response Predictor (Uno)](https://modac.cancer.gov/searchTab?dme_data_id=NCI-DME-MS01-7654821) asset contains the untrained model and trained model:
  * The model topology file is uno.model.json. 
  * The trained model is defined by combining the untrained model (uno.model.json) and model weights (uno.model.h5).
  * The trained model is used in inference.
* The [Pilot 1 Cancer Drug Response Prediction Dataset](https://modac.cancer.gov/searchTab?dme_data_id=NCI-DME-MS01-8088592) asset contains the processed training and test data. 

Technical Section
============
Setup
============
To set up the Python environment needed to train and run this model:
1. Install [conda](https://docs.conda.io/en/latest/) package manager.
2. Clone this repository.
3. Create the environment as shown below.

```bash conda env create -f environment.yml -n UNO
```

```conda activate UNO
```
   
Training
============
To train the model from scratch, execute the script [uno_baseline_keras2.py](uno_baseline_keras2.py). This script does the following:
* Reads the model configuration parameters from [uno_default_model.txt](uno_default_model.txt).
* Downloads the training data and splits it to training/validation sets.
* Creates and trains the Keras model.
* Saves the best-trained model based on the validation accuracy.

Training Uno on all data sources is slow. The `--train_sources` parameter can be used to test the code with a smaller set of training data. An example command line is the following.

```
python uno_baseline_keras2.py --train_sources gCSI --cache cache/gCSI --use_landmark_genes True --preprocess_rnaseq source_scale --no_feature_source True --no_response_source True
```

A faster example is given in the `uno_by_drug_example.txt` configuration file. This example focuses on a single drug (paclitaxel) and trains at 15s/epoch on a single P100.

```
python uno_baseline_keras2.py --config_file uno_by_drug_example.txt
```

Inference
============
To test the trained model in inference, execute the script [uno_infer2.py](uno_infer2.py). This script does the following:
* Downloads the trained model.
* Downloads the processed test dataset with the corresponding labels.
* Performs inference on the test dataset.
* Reports the accuracy of the model on the test dataset.

```
python uno_infer2.py --train_sources CTRP GDSC NCI60 SCL SCLC ALMANAC  --use_landmark_genes True --preprocess_rnaseq source_scale --no_feature_source True --no_response_source True --test_sources gCSI  
```

