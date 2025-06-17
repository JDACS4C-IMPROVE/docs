Matchmaker
=================
Deep Learning Framework for Drug Synergy Prediction

Model Architecture
--------------------
MatchMaker takes chemical features and gene expression and predicts a synergy score by training two parallel drug subnetworks of three FC layers for drug specific representation on each cell line. 
Both subnetworks are input for the third subnetwork (also of three FC layers), which predicts the drug pair synergy. 

Feature Representation
-------------------------

   * Cancer features:

      * Transcriptomics: L1000

   * Drug features:

       * Mordred


URLs
--------------------
- `Original GitHub <https://github.com/tastanlab/matchmaker>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/matchmaker>`__

References
--------------------
`1. <https://ieeexplore.ieee.org/document/9447196>`_ H. Kuru, et. al. "MatchMaker: A Deep Learning Framework for Drug Synergy Prediction", IEEE/ACM Transactions on Computational Biology and Bioinformatics, 2022
