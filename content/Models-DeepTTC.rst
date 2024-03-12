=================
DeepTTC
=================
A transformer-based model for predicting cancer drug response

Model Architecture
--------------------
DeepTTC (or DeepTTA) is a deep learning-based drug response prediction method with state-of-the-art performance. This model is composed of two separate subnetworks that learn representations of the cell line gene expression data and drug SMILES encoding. Gene expression representations are obtained with the help of a multi-layer perceptron with three hidden layers of sizes 1024, 256, and 64. 

Feature Representation
--------------------

   * Cancer features: 

      * Gene expression: as continuous values

   * Drug features: 

       * Drug SMILES: split into Explainable Substructure Partition Fingertips from the pre-defined dictionary & compact embedding via a transformer-based encoder with the attention mechanism and 128-dim output



URLs
--------------------
- `Original GitHub <https://github.com/jianglikun/DeepTTC>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/DeepTTC>`__

References
--------------------
`1. <https://academic.oup.com/bib/article/23/3/bbac100/6554594?login=true>`_ L. Jiang, et. al. "DeepTTA: a transformer-based model for predicting cancer drug response", Briefings in Bioinformatics, 2022
