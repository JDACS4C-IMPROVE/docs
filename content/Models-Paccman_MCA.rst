=================
PaccMann-MCA
=================
Prediction of AntiCancer Compound sensitivity with Multi-modal Attention-based Neural Networks

Model Architecture
--------------------
The PaccMann-MCA model is composed of a network propagation layer, an attention-based gene expression encoder, a SMILES embedding layer and a SMILES encoder. The gene expression encoder generates attention weights to encode the cell-line gene expression. The model uses multiscale convolutional attention (MCA) mechanism for the SMILES encoders. The MCA mechanism enables to incorporate both positional information and long-range dependencies using a combination of convolutional layers and contextual attention mechanisms. Finally the encoded drug and cell-line features are concatenated and inputted to fully connected dense layers to predict the drug response.

Feature Representation
--------------------------

   * Cancer features: 

      * Gene Expression: RMA-normalized

   * Drug features: 

      * SMILES
      * Morgan fingerprints



URLs
--------------------
- `Original GitHub <https://github.com/PaccMann/paccmann_predictor>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/Paccmann_MCA>`__

References
--------------------
`1. <https://pubs.acs.org/doi/10.1021/acs.molpharmaceut.9b00520>`_ M. Manica, et. al. "Toward Explainable Anticancer Compound Sensitivity Prediction via Multimodal Attention-Based Convolutional Encoders", Mol. Pharmaceutics, 2019
