=================
DualGCN
=================
A dual graph convolutional network model to predict cancer drug response


Model Architecture
--------------------
DualGCN consists of two Graph Convolutional Networks (GCN) branches, one for protein-protein interaction information (which includes Copy Number Variation and Gene Expression), and one for the chemical structure of the applied drug. Each branch has built-in dropout and batch normalization, where the dropout rate is one of the considered hyperparameters. At the end of the branches, the obtained features are concatenated and fed into a fully connected network (FCN) with three hidden layers, aiming to do the regression analysis between the output of the two branches and the drug response values. 

Feature Representation
-------------------------

   * Cancer features: 

      * Copy Number Variation
      * Gene Expression

   * Drug features: 

       * SMILES: converted into a graph using RDKit and DeepChem

   * Other features:

      * Protein-Protein Interaction



URLs
--------------------
- `Original GitHub <https://github.com/horsedayday/DualGCN>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/DualGCN>`__

References
--------------------
`1. <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-022-04664-4>`_ T. Ma, et. al. "DualGCN: a dual graph convolutional network model to predict cancer drug response", BMC Bioinformatics, 2022
