=================
GraphDRP
=================
-------------------------
Graph Convolutional Networks for Drug Response Prediction
-------------------------

Structure
============
GraphDRP consists of two subnetworks that learn from input features of cancer cell lines (CCLs) and drugs to predict drug response. The encoded representations by the subnetworks are concatenated and passed through dense layers for the prediction of IC50. The CCLs are represented with 735 binary features including variant and copy number alterations. The drugs are represented with graph structures where nodes represent the atoms of drug molecules and edges represent the bonds. Each atom is represented by 78 features. The CCL subnetwork consists of three 1-D CNNs followed by dense layers. For the drug subnetworks, four different configurations of graph neural networks (GNN) have been explored, including GCN, GAT, and GIN.

Data Sources
============

- GDSC version 6.0 (also called GDSC1000)
- PubChem

Data and preprocessing
============
CCL features and response data were downloaded from the GDSC website.  

- Cell lines features. 735 binary features that include mutations and copy number alterations were downloaded for GDSC1_ (PANCANCER_Genetic_feature.csv).
- Drug features. Drug SMILES (drug_smiles.csv) were retrieved from the PubChem using CIDs (Druglist.csv).
- Response values. The raw IC50 values (PANCANCER_IC.csv) were transformed with 1 / (1 + pow(math.exp(float(ic50)), -0.1)) (see preprocess.py).
- Data structures that can be used with PyTorch Geometric were created containing cell and drug features, and response values. 

Evaluation
============
Three evaluation schemes were used for performance evaluation.

- Mixed: cell lines and drugs can appear in train, validation, and test sets.
- Cell blind: no overlap on cell lines in train, validation, and test sets.
- Drug blind: no overlap on drugs in train, validation, and test sets. 

URLs
============
- Original GitHub: https://github.com/hauldhut/GraphDRP
- IMPROVE GitHub: https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/improve

Reference
---------
Nguyen, T.-T. et al. Graph convolutional networks for drug response prediction. *IEEE/ACM Trans Comput Biol Bioinform*. Jan-Feb 2022;19(1):146-154.

.. _GDSC1: https://www.cancerrxgene.org/downloads/genetic_features?mutation=both&screening_set=GDSC1

