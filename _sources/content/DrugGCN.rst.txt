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

- GDSC: cell line and drug ids, treatment response, cell line omics data

- Library of Integrated Network-Based Cellular Signatures (LINCS) L1000 project: list of genes

- STRING: PPI network data

Raw data
--------
The raw data includes the following for the L1000 and Var1000 datasets:

#. EXP.csv: Gene expression data for 734 cell lines obtained from the authors' GitHub page, `GDSC_DATASET_S1-S12.zip <https://github.com/Jinyu2019/Suppl-data-BBpaper/blob/master/GDSC_DATASET_S1-S12.zip>`__, and found in the file,  Table_S1_GDSC_Gene_expression.csv.

#. PPI_INFO.txt: List of proteins including their display names and descriptions from the STRING database. This data can be downloaded from the STRING database `here <https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz>`__.

#. PPI_LINK.txt: Protein network data (full network, scored links between proteins) from the STRING database. This data can be downloaded from the STRING database `here <https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz>`__.

#. LIST.txt: 663 or 1000 genes for the L1000 and Var1000 datasets respectively.

The raw data is available in `this FTP location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/DrugGCN/druggcn_data.tar.gz>`__.

ML data
-------
The script `dataProcess.py <https://github.com/JDACS4C-IMPROVE/DrugGCN/blob/develop/dataProcess.py>`__ uses raw data to generate ML data that can be used to train and test with DrugGCN. The necessary raw data are automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()` and processed. 

The ML data files are available in `this FTP location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/DrugGCN/druggcn_data_processed.tar.gz>`__. These files can be automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()`.

The ML data files include the following:

- **Cancer features**. L1000 and Var1000 folders with gene expression and protein-protein interaction files: 
   - groupEXP.csv: Gene expression data of selected genes.
   - groupEXP_foldChange.csv: Fold change of gene expression data of selected genes.
   - groupPPI.csv: PPI data of selected genes where values are weights of the interactions that reflect the amount of available evidence of the interaction between two genes.
- **Response data**. IC50 or AUC values of 201 drugs and 734 cell lines.
   - Table_S6_GDSC_Drug_response_IC50.csv
   - Table_S7_GDSC_Drug_response_AUC.csv

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
- `Original GitHub <https://github.com/BML-cbnu/DrugGCN>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/DrugGCN/tree/develop>`__
- `Data <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/DrugGCN/>`__


----------
References
----------
Kim S, Bae S, Piao Y, Jo K. Graph Convolutional Network for Drug Response Prediction Using Gene Expression Data. *Mathematics*. 2021; 9(7):772. https://doi.org/10.3390/math9070772
