=================
GraphDRP
=================
Graph Convolutional Networks for Drug Response Prediction

---------
Structure
---------
GraphDRP consists of two subnetworks that learn from input features of cancer cell lines (CCLs) and drugs to predict IC50, a dose-independent treatment response. The encoded feature representations by the two subnetworks are concatenated and passed through dense layers for the prediction of IC50. Each CCL is represented by a vector of 735 binary features including variant conding and copy number alterations. Each drug is represented with a graph molecular structure where nodes and edges represent, respectively, the atoms and bonds of the a molecule (each atom is represented by 78 features). The CCL subnetwork consists of three 1-D CNNs followed by dense layers. For the drug subnetworks, four different configurations of graph neural network (GNN) modules have been explored, including GCN, GAT, and GIN.

----
Data
----

Data sources
------------
The primary data sources that have been used to construct ML datasets include:

- GDSC version 6.0 (cell line and drug ids, treatment response, cell line omics data)
- PubChem (drug SMILES)

Raw data
--------
The raw data is downloaded from GDSC website (version 6.0):

#. Dose-independent drug response values. `PANCANCER_IC.csv`: drug and cell ids, IC50 values and other metadata (223 drugs and 948 cell lines).
#. Cancer sample information. `PANCANCER_Genetic_feature.csv`: 735 binary features that include coding variants and copy number alterations.
#. Drug information. `drug_smiles.csv`: SMILES strings of drug molecules. The SMILES were retrieved from PubChem using CIDs (Druglist.csv). The script `preprocess.py` provides functions to generate this file.

All these data types were provided with the GraphDRP repo and are available in `this ftp location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/GraphDRP/data/>`__.

ML data
-------
The script `preprocess.py <https://github.com/JDACS4C-IMPROVE/GraphDRP/blob/develop/preprocess.py>`__ uses raw data to generate ML data that can be used to train and test with GraphDRP. The necessary raw data are automatically downloaded from the FTP server using a `candle_lib` utility function `get_file()` and processed:

- **Response data**. IC50 values (PANCANCER_IC.csv) are transformed using 1 / (1 + pow(math.exp(float(ic50)), -0.1)).
- **Cancer features**. 735 binary features, including mutations and copy number alterations, are not modified.
- **Drug features**. SMILES string of each drug is converted into graph structure where nodes represent atoms and edges represent the bonds (each atom is represented by 78 features).

The user can specify one of three data splitting strategies: 1) mixed set (random split), 2) cell-blind (hard partition on cell line samples), 3) drug-blind (hard partition on drugs).
In either case, the script generates three files, `train_data.pt`, `val_data.pt`, and `test_data.pt` with 0.8/0.1/0.1 ratio, and saves them in appropriate directories:

- ./data_processed/<split_strategy>/processed/train_data.pt
- ./data_processed/<split_strategy>/processed/val_data.pt
- ./data_processed/<split_strategy>/processed/test_data.pt

Bash script `preprocess_batch.sh <https://github.com/JDACS4C-IMPROVE/GraphDRP/blob/develop/preprocess_batch.sh>`__ generates the nine possible ML data configurations (i.e., 3 files for each splitting strategy). All the ML data files for the three splitting strategies are available in `this ftp location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/GraphDRP/data_processed/>`__.


----------
Evaluation
----------
Three evaluation schemes were used for the analysis of prediction performance.

- Mixed set: cell lines and drugs can appear in train, validation, and test sets.
- Cell-blind: no overlap on cell lines in train, validation, and test sets.
- Drug-blind: no overlap on drugs in train, validation, and test sets. 

----
URLs
----
- `Original GitHub <https://github.com/hauldhut/GraphDRP>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/develop>`__
- `Data <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/GraphDRP/>`__

----------
References
----------
Nguyen, T.-T. et al. Graph convolutional networks for drug response prediction. *IEEE/ACM Trans Comput Biol Bioinform*. Jan-Feb 2022;19(1):146-154.