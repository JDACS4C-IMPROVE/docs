=================
UNO
=================
Unified Drug Response Predictor

Model Architecture
--------------------
UNO consists of two fully connected neural network branches for separately embedding the drug and cell line features, then a third fully connected neural network to regress on the combined embedded features. UNO was one of the benchmark models in the CANDLE project for cancer drug response.

Feature Representation
--------------------

   * Cancer features: 

      * Gene Expression: as floats

   * Drug features: 

      * Drug Molecular Descriptors: mordred values as floats


URLs
--------------------
- `Original GitHub <https://github.com/JDACS4C-IMPROVE/Benchmarks/tree/preprocess_improve/Pilot1/Uno_IMPROVE>`__
