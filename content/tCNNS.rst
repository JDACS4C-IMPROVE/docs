=================
tCNNS
=================
Twin convolutional neural network for drugs in SMILES format.


---------
Structure
---------
tCNNS consists of two 1D convolutional neural network (CNN) branches for distilling the features for drugs and cell lines separately. For the cell-line branch, the input data are 1D feature vectors of 735 genetic features related to mutation state or copy number alteration. 
For the drug branch, the input data are one-hot matrices (28 unique symbols x 188 positions) for each drug where a value of 1 at row i and column j means that the ith symbol appears at jth position in the SMILES format for that drug. The structures for the two branches are the same. For each branch, there are three similar layers: each layer with convolution width 7, convolution stride 1, max pooling width 3, and pooling stride 3. The only difference between the layers is that their number of channels are 40, 80 and 60, respectively. After the two branches of the CNN, there is a fully connected network (FCN), which aims to do the regression analysis between the output of the two branches and the IC50 values. There are three hidden layers in the FCN, each with 1024 neurons. The dropout probability is set to be 0.5 for the FCN during the training phase.


----
Data
----

Data sources
------------
The primary data sources that have been used to construct datasets for model training and testing (i.e., ML data) include:
- GDSC version 6.0 - cell line and drug IDs, treatment response, cell line omics data
- PubChem - drug SMILES
- Library of the Integrated Network-based Cellular Signatures (LINCS) - drug SMILES

Raw data
--------
The raw data is downloaded from GDSC website (version 6.0) and refers here to three types of data:

#.  Dose-independent drug response values. `PANCANCER_IC.csv`: drug and cell IDs, IC50 values and other metadata (223 drugs and 948 cell lines).

#.  Cancer sample information. `PANCANCER_Genetic_feature.csv`: 735 binary features that include mutations and copy number alterations.

#.  Drug information. `drug_smiles.csv`: SMILES strings of drug molecules. The canonical SMILES were retrieved from PubChem using CIDs (`Druglist.csv`) or from LINCS if not available in PubChem. The script `preprocess.py` provides functions to generate this file.

The raw data is available in `this FTP location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/tCNNS/tcnns_data.tar.gz>`__.

ML data
-------
The script `preprocess.py <https://github.com/JDACS4C-IMPROVE/tCNNS/blob/develop/preprocess.py>`__ uses raw data to generate ML data that can be used to train and test with tCNNS. The necessary raw data are automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()` and processed. 

The ML data files are available in `this FTP location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/tCNNS/tcnns_data_processed.tar.gz>`__. These files can be automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()`.

- **Response data**. IC50 values (`PANCANCER_IC.csv`) are normalized in the (0,1) interval.
- **Cancer features**. 735 binary features, including mutations and copy number alterations, are not modified.
- **Drug features**. SMILES string of each drug is converted into a 28 by 188 one-hot matrix where a value 1 at row i and column j means that the ith symbol appears at jth position in the SMILES string.


----------
Evaluation
----------
Several evaluation schemes were used for the analysis of prediction performance.

- Mixed set: Cell lines and drugs can appear in train, validation, and test sets.
- Cell-blind: No overlap on cell lines in train, validation, and test sets.
- Drug-blind: No overlap on drugs in train, validation, and test sets. 
- Exclusion of extrapolated activity data: The model is trained and tested on a subset of GDSC data referred to as max_conc data. This subset of data only includes IC50 values below the maximum screening concentration (max_conc), which is the maximum IC50 value verified by biological experiments for each drug in GDSC.
- Number of cell line features: The performance of the model is tested with different numbers of cell line features.
- Modification of SMILES format:  The one-hot representation of the SMILES format was modified in three ways for assessing whether the model captures the biological meaning in the data versus the statistical pattern of the data.


----
URLs
----
- `Original GitHub <https://github.com/Lowpassfilter/tCNNS-Project>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/tCNNS-Project/tree/develop>`__
- `Data <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/tCNNS/>`__


----------
References
----------
Liu, P., Li, H., Li, S., & Leung, K. S. (2019). Improving prediction of phenotypic drug response on cancer cell lines using deep convolutional network. BMC bioinformatics, 20(1), 408. https://doi.org/10.1186/s12859-019-2910-6

