=================
DualGCN
=================
A dual graph convolutional network model to predict cancer drug response


Model Architecture
--------------------
DualGCN is structured with two distinct GCN arms, termed drug-GCN and bio-GCN, which take input graphs of chemical structures and multi-omics features. Following multiple graph convolution layers, graph-level features are generated and pooled. Then, the features from two arms are concatenated and passed through an MLP block to generate IC50 predictions. For the chemical graph, the nodes are atoms, and edges are bonds. The atom features are generated using DeepChem default atom features. For the bio graph, the nodes are genes, and edges are protein-protein interactions (PPI). The input of genetic is flexible for multiomics input, and expression + CNV is reported to have the best performance. 

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
- `Original GitHub <https://github.com/horsedayday/DualGCN>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/DualGCN>`__

References
--------------------
`1. <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-022-04664-4>`_ T. Ma, et. al. "DualGCN: a dual graph convolutional network model to predict cancer drug response", BMC Bioinformatics, 2022
