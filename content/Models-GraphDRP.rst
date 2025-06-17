=================
GraphDRP
=================
Graph Convolutional Networks for Drug Response Prediction

Model Architecture
--------------------
GraphDRP consists of two subnetworks that learn from input features of cancer cell lines (CCLs) and drugs to predict drug response. The encoded feature representations by the two subnetworks are concatenated and passed through dense layers for the prediction. Each CCL is represented by a vector of binary features including variant coding and copy number alterations. Each drug is represented with a graph molecular structure where nodes and edges represent, respectively, the atoms and bonds of the a molecule. The CCL subnetwork consists of three 1-D CNNs followed by dense layers. 

Feature Representation
--------------------------

   * Cancer features:

      * Mutation: as binary
      * Copy Number Variation: as binary

   * Drug features: 

       * SMILES: converted into graph structure where nodes represent atoms and edges represent the bonds (each atom is represented by 78 features)


URLs
--------------------
- `Original GitHub <https://github.com/hauldhut/GraphDRP>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/develop>`__
- `Data <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/GraphDRP/>`__

References
--------------------
Nguyen, T.-T. et al. Graph convolutional networks for drug response prediction. *IEEE/ACM Trans Comput Biol Bioinform*. Jan-Feb 2022;19(1):146-154.
