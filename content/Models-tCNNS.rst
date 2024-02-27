=================
tCNNS
=================
Twin convolutional neural network for drugs in SMILES format.

Model Architecture
--------------------
tCNNS consists of two 1D convolutional neural network (CNN) branches for distilling the features for drugs and cell lines separately. For the cell-line branch, the input data are 1D feature vectors of 735 genetic features related to mutation state or copy number alteration. 
For the drug branch, the input data are one-hot matrices (28 unique symbols x 188 positions) for each drug where a value of 1 at row i and column j means that the ith symbol appears at jth position in the SMILES format for that drug. The structures for the two branches are the same. For each branch, there are three similar layers: each layer with convolution width 7, convolution stride 1, max pooling width 3, and pooling stride 3. The only difference between the layers is that their number of channels are 40, 80 and 60, respectively. After the two branches of the CNN, there is a fully connected network (FCN), which aims to do the regression analysis between the output of the two branches and the IC50 values. There are three hidden layers in the FCN, each with 1024 neurons. The dropout probability is set to be 0.5 for the FCN during the training phase.

Feature Representation
--------------------

   * Response data: IC50 values

      * normalized in the (0,1) interval

   * Cancer features: 735 binary features, including mutations and copy number alterations

      * not modified

   * Drug features: SMILES strings

       * converted into a 28 by 188 one-hot matrix where a value 1 at row i and column j means that the ith symbol appears at jth position in the SMILES string



URLs
--------------------
- `Original GitHub <https://github.com/Lowpassfilter/tCNNS-Project>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/tCNNS-Project/tree/develop>`__

References
--------------------
`1. <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2910-6>`_ P. Liu, et. al. "Improving prediction of phenotypic drug response on cancer cell lines using deep convolutional network", BMC Bioinformatics, 2019
