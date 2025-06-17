=================
tCNNS
=================
Twin convolutional neural network for drugs in SMILES format.

Model Architecture
--------------------
tCNNS consists of two 1D convolutional neural network (CNN) branches for distilling the features for drugs and cell lines separately, each with three layers. After the two branches of the CNN, there is a fully connected network (FCN) with three hidden layers, which aims to do the regression analysis between the output of the two branches and the drug response values. tCNNS was one of the first models to apply CNNs to the problem of drug prediction.

Feature Representation
--------------------------

   * Cancer features:

      * Mutation: as binary
      * CNV: as binary

   * Drug features:

       * SMILES: converted into a 28 by 188 one-hot matrix where a value 1 at row i and column j means that the ith symbol appears at jth position in the SMILES string



URLs
--------------------
- `Original GitHub <https://github.com/Lowpassfilter/tCNNS-Project>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/tCNNS-Project/tree/develop>`__

References
--------------------
`1. <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2910-6>`_ P. Liu, et. al. "Improving prediction of phenotypic drug response on cancer cell lines using deep convolutional network", BMC Bioinformatics, 2019
