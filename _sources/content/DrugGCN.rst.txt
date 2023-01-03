=================
DrugGCN
=================
DrugGCN is a framework for the prediction of **Drug** response using a Graph Convolutional Network (**GCN**).

---------
Structure
---------
DrugGCN uses a graph convolutional network model to learn genomic features of cell lines with a graph structure for drug response prediction. This framework integrates protein-protein interaction (PPI) network data and gene expression data utilizing genes with high predictive power to construct a model for each drug. The input of the GCN model is an undirected input graph G=(V,E,W) where V is a set of vertices, E is a set of edges, and W is a weighted adjacency matrix. Vertices and edges of the graph indicate genes and interactions between genes respectively. The use of localized filters in DrugGCN aids in the detection of local features in a biological network such as subnetworks of genes that can contribute together to drug response.

----
Data
----

Data sources
------------
The primary data sources that have been used to construct datasets for model training and testing (i.e., ML data) include:
- GDSC - cell line and drug ids, treatment response, cell line omics data
- Library of Integrated Network-Based Cellular Signatures (LINCS) L1000 project - list of genes
- STRING - PPI network data

Raw data
--------
The raw data is downloaded from GDSC website (version 6.0):

#. Dose-independent drug response values. `PANCANCER_IC.csv`: drug and cell ids, IC50 values and other metadata (223 drugs and 948 cell lines).
#. Cancer sample information. `PANCANCER_Genetic_feature.csv`: 735 binary features that include coding variants and copy number alterations.
#. Drug information. `drug_smiles.csv`: SMILES strings of drug molecules. The SMILES were retrieved from PubChem using CIDs (Druglist.csv). The script `preprocess.py` provides functions to generate this file.

All these data types were provided with the GraphDRP repo and are available in `this ftp location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/GraphDRP/data/>`__.

CCL omics data and treatment response data (IC50 and AUC) were downloaded from the authors' GitHub page, [GDSC_DATASET_S1-S12.zip](https://github.com/Jinyu2019/Suppl-data-BBpaper/blob/master/GDSC_DATASET_S1-S12.zip). The [protein links](https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz) and [protein info](https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz) files (version 11.5) for *Homo sapiens* can be obtained from the STRING website. Refer to [Data](Data.md) for more info regarding the raw data provided with the original DrugGCN model repo and preprocessing scripts allowing to generate ML data for model training and testing.

The raw data includes the following for the L1000 and Var1000 datasets:
1) Gene expression data. `EXP.csv`: Gene expression data for 734 cell lines obtained from the authors' GitHub page, [GDSC_DATASET_S1-S12.zip](https://github.com/Jinyu2019/Suppl-data-BBpaper/blob/master/GDSC_DATASET_S1-S12.zip), and found in the file,  `Table_S1_GDSC_Gene_expression.csv`.
2) Protein info. `PPI_INFO.txt`: List of proteins including their display names and descriptions from the STRING database. This data can be downloaded from the STRING database [here](https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz).
3) Protein links. `PPI_LINK.txt`: Protein network data (full network, scored links between proteins) from the STRING database. This data can be downloaded from the STRING database [here](https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz).
4) List of genes. `LIST.txt`: 663 or 1000 genes for the L1000 and Var1000 datasets respectively.

The raw data is available in: https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/DrugGCN/druggcn_data.tar.gz

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

The script `dataProcess.py` uses raw data to generate ML data that can be used to train and test with DrugGCN. The necessary raw data are automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()` and processed. 

The ML data files are available in FTP: https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/DrugGCN/druggcn_data_processed.tar.gz. These files can be automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()`.

The ML data files include the following:

- __Cancer features__. L1000 and Var1000 folders with gene expression and protein-protein interaction files: 
  - `groupEXP.csv`. Gene expression data of selected genes.
  - `groupEXP_foldChange.csv`. Fold change of gene expression data of selected genes.
  - `groupPPI.csv`. Protein-protein interaction data of selected genes where values are weights of the interactions that reflect the amount of available evidence of the interaction between two genes.
- __Response data__. IC50 or AUC values of 201 drugs and 734 cell lines.
  - `Table_S6_GDSC_Drug_response_IC50.csv`
  - `Table_S7_GDSC_Drug_response_AUC.csv`

The user can specify which dataset, L1000 or Var1000, and which response data, IC50 or AUC, to use when training and testing the model.


----------
Evaluation
----------
Four evaluation schemes were used for the analysis of prediction performance.

- L1000-IC50: Gene set of 663 genes using the list of landmark genes derived from LINCS L1000 project and IC50 drug response values.
- L1000-AUC: Gene set of 663 genes using the list of landmark genes derived from LINCS L1000 project and AUC drug response values.
- Var1000-IC50: Gene set of the top 1000 variable genes and IC50 drug response values.
- Var1000-AUC: Gene set of the top 1000 variable genes and AUC drug response values.

----
URLs
----
- `Original GitHub <https://github.com/hauldhut/GraphDRP>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/develop>`__
- `Data <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/GraphDRP/>`__

- [Original GitHub](https://github.com/BML-cbnu/DrugGCN)
- [IMPROVE GitHub](https://github.com/JDACS4C-IMPROVE/DrugGCN/tree/develop)
- [Data](https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/DrugGCN/)

----------
References
----------
Kim S, Bae S, Piao Y, Jo K. Graph Convolutional Network for Drug Response Prediction Using Gene Expression Data. *Mathematics*. 2021; 9(7):772. https://doi.org/10.3390/math9070772
