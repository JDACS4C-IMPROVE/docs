=================
NIHGCN
=================
NIHGCN is a framework for predicting drug response using a graph neural network approach to learn cell and drug embeddings. 

---------
Paper
---------
Peng, W., Liu, H., Dai, W., Yu, N., & Wang, J. (2022). Predicting cancer drug response using parallel heterogeneous graph convolutional networks with neighborhood interactions. Bioinformatics, 38(19), 4546-4553.
https://doi.org/10.1093/bioinformatics/btac574

---------
Structure
---------
NIHGCN is a graph neural network model that builds on a bipartite heterogeneous network based on the known drug responses in cell lines, i.e. sensitive or resistant. This bipartite graph is then used to learn the feature representation for both drugs and cell lines by transforming and aggregating the neighborhood feature information on the graph architecture using an interaction module. The interaction module consists of a Parallel Graph Convolution Network (PGCN) layer and a Neighbor Interaction (NI) layer, aggregating features from neighbors at the node and element level. Initial embeddings for cell and drug nodes are given by a vector of the normalized gene expression in a given cell line and the linear transform of the drug molecular fingerprints, respectively. The PGCN then consists of a summation of features from a cell node and all connected drug nodes multiplied by a learned weight matrix, and vice-versa for drug nodes. The NI layer takes the element-wise dot product of the PGCN summation and the node, with the goal of emphasizing similarities between vectors. Finally the aggregation layer passes a weighted sum of the PGCN and NI representations through a ReLu. Linear correlation between the aggregated drug and cell representations are used for training drug response prediction with BCE loss.

----
Data
----

Data sources
------------
