=================
PathDSP
=================
Explainable Drug Sensitivity Prediction through Cancer Pathway Enrichment Scores

Model Architecture
--------------------
PathDSP first converts the cancer and drug features into pathway-level enrichment scores using a network-based approach, then feeds those into a fully connected neural network (FNN) with four hidden layers.

Feature Representation
---------------------------

   * Cancer features: 

      * Gene Expression: converted into pathway-level activity using ssGSEA algorithm
      * CNV: converted into pathway-level activity using NetPEA algorithm
      * Mutation: converted into pathway-level activity using NetPEA algorithm

   * Drug features: 

      * SMILES: converted into morgan fingerprints
      * Drug target: converted into pathway-level activity using NetPEA algorithm



URLs
--------------------
- `Original GitHub <https://github.com/TangYiChing/PathDSP>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/PathDSP>`__

References
--------------------
`1. <https://www.nature.com/articles/s41598-021-82612-7>`_ Y. Tang and A. Gottlieb. "Explainable drug sensitivity prediction through cancer pathway enrichment", Scientific Reports, 2021.
