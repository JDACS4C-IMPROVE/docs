DeepDDS
=================
Deep Learning for Drug-Drug Synergy Prediction

Model Architecture
--------------------
DeepDDS extracts features for drugs with a GCN and cell features with an MLP and concatenates these features to an input vector to a multilayer fully connected network to predict binary classifications of synergy. 

Model Type
---------------
Classification

Feature Representation
-------------------------

   * Cancer features:

      * Transcriptomics: L1000

   * Drug features:

       * SMILES: converted to molecular graph


URLs
--------------------
- `Original GitHub <https://github.com/Sinwang404/DeepDDS/tree/master>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/DeepDDs>`__

References
--------------------
`1. <https://academic.oup.com/bib/article/23/1/bbab390/6375262>`_ J. Wang, et. al. "DeepDDS: deep graph neural network with attention mechanism to predict synergistic drug combinations", Briefings in Bioinformatics, 2022
