=================
DeepTTC
=================
A transformer-based model for predicting cancer drug response

Model Architecture
--------------------
DeepTTA (DeepTTC on GitHub) model is a Deep Learning model that uses dual convergence approach, where separate networks are responsible for learning embeddings for cell lines and drug representations, and afterward Multi-Layer Perceptron (MLP) classifier is trained to predict drug response. Drug features are encoded via transformer architecture that uses an attention mechanism to find correlations between Explainable Substructure Partition Fingerprint (ESPF) encodings of drugs. Gene expressions are encoded by MLP with three hidden layers with the sizes of 1024, 256, and 64.

Feature Representation
--------------------

   * Response data: 

      * 

   * Cancer features: 

      * 

   * Drug features: 

       * 



URLs
--------------------
- `Original GitHub <https://github.com/jianglikun/DeepTTC>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/DeepTTC>`__

References
--------------------
`1. <https://academic.oup.com/bib/article/23/3/bbac100/6554594?login=true>`_ L. Jiang, et. al. "DeepTTA: a transformer-based model for predicting cancer drug response", Briefings in Bioinformatics, 2022
