=================
DeepCDR
=================
Cancer Drug Response Prediction via a Hybrid Graph Convolutional Network

Model Architecture
--------------------
DeepCDR is a hybrid graph convolutional network (GCN) that consists of a uniform graph convolutional network (UGCN) to represent the chemical features of cancer drugs and several subnetworks for processing different multi-omic profiles. The UGCN takes the adjacency information of atoms in the drug molecules by aggregating the features of the neighboring atoms into consideration, and the subnetworks extract features for the cancer omic profiles from cell line information. Both these features are later concatenated and passed through a 1D convolutional neural network (CNN) to predict the cancer drug response (CDR). DeepCDR is one of the first models to use GCNs and multi-omic profiles to predict CDR.

Model Type
---------------
Regression

Feature Representation
------------------------

   * Cancer features: 

      * Gene Expression: extracted by subnetwork
      * DNA Methylation: extracted by subnetwork
      * Mutation: extracted by subnetwork

   * Drug features: 

       * SMILES: neighboring and feature information of the drug molecules are processed using a UGCN



URLs
--------------------
- `Original GitHub <https://github.com/kimmo1019/DeepCDR>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/DeepCDR>`__

References
--------------------
`1. <https://academic.oup.com/bioinformatics/article/36/Supplement_2/i911/6055929>`_ Q. Liu, et. al. "DeepCDR: a hybrid graph convolutional network for predicting cancer drug response", Bioinformatics, 2020
