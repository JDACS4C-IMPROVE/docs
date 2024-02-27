=================
GraphDRP
=================
Graph Convolutional Networks for Drug Response Prediction

Model Architecture
--------------------
GraphDRP consists of two subnetworks that learn from input features of cancer cell lines (CCLs) and drugs to predict IC50, a dose-independent treatment response. The encoded feature representations by the two subnetworks are concatenated and passed through dense layers for the prediction of IC50. Each CCL is represented by a vector of 735 binary features including variant conding and copy number alterations. Each drug is represented with a graph molecular structure where nodes and edges represent, respectively, the atoms and bonds of the a molecule (each atom is represented by 78 features). The CCL subnetwork consists of three 1-D CNNs followed by dense layers. For the drug subnetworks, four different configurations of graph neural network (GNN) modules have been explored, including GCN, GAT, and GIN.

Feature Representation
--------------------
The script preprocess.py uses raw data to generate ML data that can be used to train and test with GraphDRP. The necessary raw data are automatically downloaded from the FTP server using a candle_lib utility function get_file() and processed:

   * Response data: IC50 values

      * (PANCANCER_IC.csv) are transformed using 1 / (1 + pow(math.exp(float(ic50)), -0.1)).

   * Cancer features: 735 binary features, including mutations and copy number alterations

      * not modified

   * Drug features: SMILES strings

       * converted into graph structure where nodes represent atoms and edges represent the bonds (each atom is represented by 78 features).

The user can specify one of three data splitting strategies: 1) mixed set (random split), 2) cell-blind (hard partition on cell line samples), 3) drug-blind (hard partition on drugs). In either case, the script generates three files, train_data.pt, val_data.pt, and test_data.pt with 0.8/0.1/0.1 ratio, and saves them in appropriate directories:
./data_processed/<split_strategy>/processed/train_data.pt
./data_processed/<split_strategy>/processed/val_data.pt
./data_processed/<split_strategy>/processed/test_data.pt
Bash script preprocess_batch.sh generates the nine possible ML data configurations (i.e., 3 files for each splitting strategy).

URLs
--------------------
- `Original GitHub <https://github.com/hauldhut/GraphDRP>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/GraphDRP/tree/develop>`__
- `Data <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/GraphDRP/>`__

References
--------------------
Nguyen, T.-T. et al. Graph convolutional networks for drug response prediction. *IEEE/ACM Trans Comput Biol Bioinform*. Jan-Feb 2022;19(1):146-154.
