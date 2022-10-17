# Unified-Drug-Response-Predictor

### Description
The Unified Drug Response Predictor benchmark, also called Uno, is a deep neural network for modeling cell line response to treatments of single or paired drugs. The model takes cell line molecular features, drug properties, and dose information as input and predicts the response in percentage growth. The model uses a multi-tower structure for processing different feature types individually before concatenating them for the final layers. The model also unifies treatment input types of single drugs and drug pairs by allocating two slots for drugs and, in the case of drug pairs, dividing the concentration into the two slots. The authors of this model have integrated datasets from multiple public sources of drug response studies and provided options for training models with selections of subsets.

### User Community
Cancer biology data modeling; Machine Learning; Bioinformatics; Computational Biology

### Usability
To use the untrained model, users must be familiar with processing and feature extraction of molecular drug data, gene expression, and training of neural networks. The input to the model is preprocessed data. Users should have extended experience with preprocessing this data.

### Uniqueness
The community can use a neural network and multiple machine learning techniques to predict drug response. The general rule is that classical methods like random forests would perform better for small datasets, while neural network approaches like Uno would perform better for relatively larger datasets. The baseline for comparison can be: mean response, linear regression, or random forest regression.

### Components
The following components are in the Model and Data Clearinghouse (MoDaC):
* The [Unified Drug Response Predictor (Uno)](https://modac.cancer.gov/searchTab?dme_data_id=NCI-DME-MS01-7654821) asset contains the untrained model and trained model:
  * The model topology file is uno.model.json. 
  * The trained model is defined by combining the untrained model (uno.model.json) and model weights (uno.model.h5).
  * The trained model is used in inference.
* The [Pilot 1 Cancer Drug Response Prediction Dataset](https://modac.cancer.gov/searchTab?dme_data_id=NCI-DME-MS01-8088592) asset contains the processed training and test data. 


## Technical Section
### Setup
To set up the Python environment needed to train and run this model:
1. Install [conda](https://docs.conda.io/en/latest/) package manager.
2. Clone this repository.
3. Create the environment as shown below.

```bash
   conda env create -f environment.yml -n UNO
   conda activate UNO
   
 ### Training
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

Here is the example output from running the script with six sources. This example requires around 5 days to complete using a single V100:

```
python uno_baseline_keras2.py --train_sources CTRP GDSC NCI60 SCL SCLC ALMANAC --cache cache/all6 --use_landmark_genes True --preprocess_rnaseq source_scale --no_feature_source True --no_response_source True --cp True --batch_size 256 --timeout -1  
Using TensorFlow backend.
Params: {'train_sources': ['CTRP', 'GDSC', 'NCI60', 'SCL', 'SCLC', 'ALMANAC'], 'test_sources': ['train'], 'cell_types': None, 'cell_features': ['rnaseq'], 'drug_features': ['descriptors', 'fingerprints'], 'dense': [1000, 1000, 1000], 'dense_feature_layers': [1000, 1000, 1000], 'activation': 'relu', 'loss': 'mse', 'optimizer': 'adam', 'scaling': 'std', 'dropout': 0, 'epochs': 10, 'batch_size': 256, 'val_split': 0.2, 'cv': 1, 'max_val_loss': 1.0, 'learning_rate': None, 'base_lr': None, 'residual': False, 'reduce_lr': False, 'warmup_lr': False, 'batch_normalization': False, 'feature_subsample': 0, 'rng_seed': 2018, 'save_path': 'save/uno', 'no_gen': False, 'verbose': None, 'gpus': [0], 'timeout': -1, 'logfile': None, 'train_bool': True, 'experiment_id': 'EXP000', 'run_id': 'RUN000', 'shuffle': False, 'profiling': False, 'agg_dose': None, 'by_cell': None, 'by_drug': None, 'cell_subset_path': '', 'drug_subset_path': '', 'drug_median_response_min': -1, 'drug_median_response_max': 1, 'no_feature_source': True, 'no_response_source': True, 'dense_cell_feature_layers': None, 'dense_drug_feature_layers': None, 'use_landmark_genes': True, 'use_filtered_genes': False, 'feature_subset_path': '', 'cell_feature_subset_path': '', 'drug_feature_subset_path': '', 'preprocess_rnaseq': 'source_scale', 'es': False, 'cp': True, 'tb': False, 'tb_prefix': 'tb', 'partition_by': None, 'cache': 'cache/all6', 'single': False, 'export_csv': None, 'export_data': None, 'use_exported_data': None, 'growth_bins': 0, 'initial_weights': None, 'save_weights': None, 'data_type': <class 'numpy.float32'>, 'output_dir': '/gpfs/gsfs12/users/lup2/NCI-DOE-Collab-Pilot1-Tumor_Classifier/Benchmarks/Pilot1/Uno_5/Output/EXP000/RUN000'}
Cache parameter file does not exist: cache/all6.params.json
Loading data from scratch ...
Loaded 27769716 single drug dose response measurements
Loaded 3686475 drug pair dose response measurements
Combined dose response data contains sources: ['CCLE' 'CTRP' 'gCSI' 'GDSC' 'NCI60' 'SCL' 'SCLC' 'ALMANAC.FG'
 'ALMANAC.FF' 'ALMANAC.1A']
Summary of combined dose response by source:
              Growth  Sample  Drug1  Drug2
Source                                    
ALMANAC.1A    208605      60    102    102
ALMANAC.FF   2062098      60     92     71
ALMANAC.FG   1415772      60    100     29
CCLE           93251     504     24      0
CTRP         6171005     887    544      0
GDSC         1894212    1075    249      0
NCI60       18862308      59  52671      0
SCL           301336      65    445      0
SCLC          389510      70    526      0
gCSI           58094     409     16      0
Combined raw dose response data has 3070 unique samples and 53520 unique drugs
Limiting drugs to those with response min <= 1, max >= -1, span >= 0, median_min <= -1, median_max >= 1 ...
Selected 47005 drugs from 53520
Loaded combined RNAseq data: (15198, 943)
Loaded combined dragon7 drug descriptors: (53507, 5271)
Loaded combined dragon7 drug fingerprints: (53507, 2049)
Filtering drug response data...
  2375 molecular samples with feature and response data
  46837 selected drugs with feature and response data
Summary of filtered dose response by source:
              Growth  Sample  Drug1  Drug2
Source                                    
ALMANAC.1A    206580      60    101    101
ALMANAC.FF   2062098      60     92     71
ALMANAC.FG   1293465      60     98     27
CTRP         3397103     812    311      0
GDSC         1022204     672    213      0
NCI60       17190561      59  46272      0
Grouped response data by drug_pair: 51758 groups
Input features shapes:
  dose1: (1,)
  dose2: (1,)
  cell.rnaseq: (942,)
  drug1.descriptors: (5270,)
  drug1.fingerprints: (2048,)
  drug2.descriptors: (5270,)
  drug2.fingerprints: (2048,)
Total input dimensions: 15580
Saved data to cache: cache/all6.pkl
Combined model:
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input.cell.rnaseq (InputLayer)  (None, 942)          0                                            
__________________________________________________________________________________________________
input.drug1.descriptors (InputL (None, 5270)         0                                            
__________________________________________________________________________________________________
input.drug1.fingerprints (Input (None, 2048)         0                                            
__________________________________________________________________________________________________
input.drug2.descriptors (InputL (None, 5270)         0                                            
__________________________________________________________________________________________________
input.drug2.fingerprints (Input (None, 2048)         0                                            
__________________________________________________________________________________________________
input.dose1 (InputLayer)        (None, 1)            0                                            
__________________________________________________________________________________________________
input.dose2 (InputLayer)        (None, 1)            0                                            
__________________________________________________________________________________________________
cell.rnaseq (Model)             (None, 1000)         2945000     input.cell.rnaseq[0][0]          
__________________________________________________________________________________________________
drug.descriptors (Model)        (None, 1000)         7273000     input.drug1.descriptors[0][0]    
                                                                 input.drug2.descriptors[0][0]    
__________________________________________________________________________________________________
drug.fingerprints (Model)       (None, 1000)         4051000     input.drug1.fingerprints[0][0]   
                                                                 input.drug2.fingerprints[0][0]   
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 5002)         0           input.dose1[0][0]                
                                                                 input.dose2[0][0]                
                                                                 cell.rnaseq[1][0]                
                                                                 drug.descriptors[1][0]           
                                                                 drug.fingerprints[1][0]          
                                                                 drug.descriptors[2][0]           
                                                                 drug.fingerprints[2][0]          
__________________________________________________________________________________________________
dense_10 (Dense)                (None, 1000)         5003000     concatenate_1[0][0]              
__________________________________________________________________________________________________
dense_11 (Dense)                (None, 1000)         1001000     dense_10[0][0]                   
__________________________________________________________________________________________________
dense_12 (Dense)                (None, 1000)         1001000     dense_11[0][0]                   
__________________________________________________________________________________________________
dense_13 (Dense)                (None, 1)            1001        dense_12[0][0]                   
==================================================================================================
Total params: 21,275,001
Trainable params: 21,275,001
Non-trainable params: 0
__________________________________________________________________________________________________

Between random pairs in y_val:
  mse: 0.5962
  mae: 0.5373
  r2: -0.9995
  corr: 0.0002
Data points per epoch: train = 20164096, val = 5007616, test = 0
Steps per epoch: train = 78766, val = 19561, test = 0
Epoch 1/10
78766/78766 [==============================] - 18320s 233ms/step - loss: 0.1693 - mae: 0.2777 - r2: -0.3982 - val_loss: 0.0503 - val_mae: 0.2550 - val_r2: -0.0162
Current time ....18320.340
Epoch 2/10
78766/78766 [==============================] - 18498s 235ms/step - loss: 0.1320 - mae: 0.2390 - r2: -0.0522 - val_loss: 0.1105 - val_mae: 0.2778 - val_r2: -0.6922
Current time ....36819.388
Epoch 3/10
78766/78766 [==============================] - 17753s 225ms/step - loss: 0.1204 - mae: 0.2268 - r2: 0.0770 - val_loss: 0.0766 - val_mae: 0.2393 - val_r2: -0.0985
Current time ....54572.061
Epoch 4/10
78766/78766 [==============================] - 17641s 224ms/step - loss: 0.1146 - mae: 0.2199 - r2: 0.1513 - val_loss: 0.1868 - val_mae: 0.2423 - val_r2: -0.0380
Current time ....72213.299
Epoch 5/10
78766/78766 [==============================] - 17038s 216ms/step - loss: 0.1092 - mae: 0.2146 - r2: 0.2071 - val_loss: 0.0999 - val_mae: 0.2364 - val_r2: -0.0185
Current time ....89251.273
Epoch 6/10
78766/78766 [==============================] - 18038s 229ms/step - loss: 0.1055 - mae: 0.2106 - r2: 0.2477 - val_loss: 0.1094 - val_mae: 0.2458 - val_r2: -0.0791
Current time ....107289.135
Epoch 7/10
78766/78766 [==============================] - 18255s 232ms/step - loss: 0.1020 - mae: 0.2067 - r2: 0.2836 - val_loss: 0.0667 - val_mae: 0.2351 - val_r2: 0.0306
Current time ....125544.598
Epoch 8/10
78766/78766 [==============================] - 18157s 231ms/step - loss: 0.0997 - mae: 0.2042 - r2: 0.3070 - val_loss: 0.0734 - val_mae: 0.2332 - val_r2: 0.0991
Current time ....143701.607
Epoch 9/10
78766/78766 [==============================] - 17812s 226ms/step - loss: 0.0980 - mae: 0.2024 - r2: 0.3295 - val_loss: 0.3237 - val_mae: 0.2358 - val_r2: 0.0204
Current time ....161514.018
Epoch 10/10
78766/78766 [==============================] - 17555s 223ms/step - loss: 0.0961 - mae: 0.2005 - r2: 0.3463 - val_loss: 0.0531 - val_mae: 0.2325 - val_r2: 0.1053
Comparing y_true and y_pred:
  mse: 0.1430
  mae: 0.2325
  r2: 0.5205
  corr: 0.7292
```

### Inference
To test the trained model in inference, execute the script [uno_infer2.py](uno_infer2.py). This script does the following:
* Downloads the trained model.
* Downloads the processed test dataset with the corresponding labels.
* Performs inference on the test dataset.
* Reports the accuracy of the model on the test dataset.

```
python uno_infer2.py --train_sources CTRP GDSC NCI60 SCL SCLC ALMANAC  --use_landmark_genes True --preprocess_rnaseq source_scale --no_feature_source True --no_response_source True --test_sources gCSI  
...
Loaded model from disk
partition:test, rank:0, sharded index size:6304, batch_size:32, steps:197
Testing on data from gCSI (6304)
  mse: 0.2040
  mae: 0.2949
  r2: 0.2434
  corr: 0.5161
```

