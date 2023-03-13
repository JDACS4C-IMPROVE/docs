=================
NIHGCN
=================
NIHGCN is a framework for predicting drug response using a graph neural network approach to learn cell and drug embeddings. 

---------
Paper
---------
Peng, W., Liu, H., Dai, W., Yu, N., & Wang, J. (2022). Predicting cancer drug response using parallel heterogeneous graph convolutional networks with neighborhood interactions. Bioinformatics, 38(19), 4546-4553.
https://doi.org/10.1093/bioinformatics/btac574

---------
Structure
---------
NIHGCN is a graph neural network model that builds on a bipartite heterogeneous network based on the known drug responses in cell lines, i.e. sensitive or resistant. This bipartite graph is then used to learn the feature representation for both drugs and cell lines by transforming and aggregating the neighborhood feature information on the graph architecture using an interaction module. The interaction module consists of a Parallel Graph Convolution Network (PGCN) layer and a Neighbor Interaction (NI) layer, aggregating features from neighbors at the node and element level. Initial embeddings for cell and drug nodes are given by a vector of the normalized gene expression in a given cell line and the linear transform of the drug molecular fingerprints, respectively. The PGCN then consists of a summation of features from a cell node and all connected drug nodes multiplied by a learned weight matrix, and vice-versa for drug nodes. The NI layer takes the element-wise dot product of the PGCN summation and the node, with the goal of emphasizing similarities between vectors. Finally the aggregation layer passes a weighted sum of the PGCN and NI representations through a ReLu. Linear correlation between the aggregated drug and cell representations are used for training drug response prediction with BCE loss.

----
Data
----

Data sources
------------
The primary data sources that have been used to construct datasets for model training and testing include:

* GDSC

  * The GDSC database provides two tables to help us infer drug sensitivity and resistance states, mainly a logarithmic matrix of half-maximal inhibitory concentration (IC50) values for all screened cell line/drug combinations, containing 990 cancer cell lines and 265 tested drugs, and sensitivity thresholds for the 265 drugs.

    * https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources//Data/suppData/TableS4A.xlsx
    * https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources//Data/suppData/TableS5C.xlsx 

  *	The tables are binarized into the following tables. Files provided by the github repo for reproducibility:

    * cell_drug.csv records the log IC50 association matrix of cell line-drug
    * cell_drug_binary.csv records the binary cell line-drug association matrix
    * cell_exprs.csv records cell line gene expression features
    * drug_feature.csv records the fingerprint features of drugs
    * null_mask.csv records the null values in the cell line-drug association matrix
    * threshold.csv records the drug sensitivity threshold

* CCLE

  * The CCLE database provides 11 670 records of cell line-drug trials. Each record reports experimental information such as drug target, dose, log(IC50) and effective area.
  * These are binarized into the following:

    * cell_drug.csv records the log IC50 association matrix of cell line-drug
    * cell_drug_binary.csv records the binary cell line-drug association matrix
    * cell_exprs.csv records cell line gene expression features
    * drug_feature.csv records the fingerprint features of drugs

#. PDX
#.. From the PDX Encyclopedia dataset (PDX), dataset is available in Supplementary File of Gao et al. (2015), containing gene expression profiles and drug responses values.
#.. Binarized files:
#... pdx_response.csv records the binary patient-drug association matrix.
#... pdx_exprs.csv records patient gene expression features.
#... pdx_null_mask.csv records the null values in the patient-drug association matrix.
#... drug_feature.csv records the fingerprint features of drugs.
#. TCGA
#.. The corresponding gene expression of the TCGA samples was from FirehoseBroadGDAC. TCGA drug responses were divided into two groups, responses (‘Complete Response’ and ‘Partial Response’) and non-response (‘Stable Disease’ and ‘Progressive Disease’). 
#.. Binarized files:
#... patient_drug_binary.csv records the binary patient-drug association matrix.
#... tcga_exprs.csv records patient gene expression features.
#... tcga_null_mask.csv records the null values in the patient-drug association matrix.
#... drug_feature.csv records the fingerprint features of drugs.

