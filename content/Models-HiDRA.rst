=================
HiDRA
=================
Hierarchical Network for Drug Response Prediction with Attention

Model Architecture
--------------------
HiDRA consists of four smaller networks: a drug feature encoding network, which takes SMILES strings converted to Morgan fingerprints; a set of gene-level networks which encode expression data for genes in each pathway; a pathway-level network that takes in output of the individual gene-level networks; and a prediction network that uses drug encodings and pathway output to predict ln(IC50). Each sub-network consists of two dense layers and an attention module (tanh + softmax activation).

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
- `Original GitHub <https://github.com/GIST-CSBL/HiDRA>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/HiDRA>`__

References
--------------------
`1. <https://pubs.acs.org/doi/full/10.1021/acs.jcim.1c00706>`_ I. Jin and H. Nam. "HiDRA: Hierarchical Network for Drug Response Prediction with Attention", J. Chem. Inf. Model., 2021
