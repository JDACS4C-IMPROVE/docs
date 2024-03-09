Drug Response Prediction Models
=================================
The IMPROVE project has curated a number of Drug Response Prediction (DRP) models.
Model curation involves selecting a subset of community models and then modifying their software scripts to conform to a unified code structure.

.. The primary focus is on pan-cancer pan-drug models. Descriptions of the curated models and links to the code can be found below.


Model Selection
-----------------
We previously compiled a compendium of papers that utilized DL methods for DRP [`1 <https://www.frontiersin.org/articles/10.3389/fmed.2023.1086097/full>`_]. As of December 2023, this collection comprised more than 90 models. Considering the size of this collection, we selected a subset of models to work on based on qualitative and hands-on selection criteria.

Qualitative selection criteria:

- Models providing open-source code with: 1) comprehensive installation instructions of the computational environment, 2) data preprocessing scripts that take feature and response data and transform them into model input data, 3) scripts which execute model training.
- Deep learning models implemented in TensorFlow/Keras or PyTorch.
- Focus on pan-cancer multi-drug models utilizing cancer and drug representations as input features.
- Preference for models utilizing conventional features and predicting continuous treatment response in cell lines (e.g., AUC, IC50).
- End-to-end learning models, excluding those requiring feature pre-training or utilizing transfer learning.
- Preference for recent peer-reviewed publications.

Hands-on selection criteria:

- Successful installation of the computational environment
- Execution of preprocessing scripts to generating model-input data
- Reproducibility of key results as reported in the respective papers


Model Standardization
-----------------------
Once the models met the selection criteria and were assessed for reproducibility, we proceeded with standardizing the
model code structure. The standardization process is executed as follows:

- Establishing reference prediction performance using the original model (e.g., r-square)
- Restructuring the code into distinct preprocessing, training, and inference scripts following the IMPROVE guidelines
- Verifying that the restructured code reproduces the reference performance
- Run small-scale cross-study analysis (a simple python script)
- Conducting a small-scale cross-study analysis (using a simple Python script)
- Running IMPROVE library test scripts

Further guidelines and details regarding code restructuring while leveraging the IMPROVE library are discussed in the :doc:`Tutorial <unified_interface>`.


Curated Models
-----------------------
Currently, we utilized 9 models for the cross-study analysis. We forked the original repositories and conducted the model selection and standardization procedures as discussed above.

.. toctree::
   :titlesonly:

   Models-GraphDRP
   Models-tCNNS
   Models-DeepTTC
   Models-IGTD
   Models-HiDRA
   Models-Paccman_MCA
   Models-DualGCN
   Models-DeepCDR
   Models-PathDSP


References
---------------------------------
`1. <https://www.frontiersin.org/articles/10.3389/fmed.2023.1086097/full>`_ A. Partin et al. "Deep learning methods for drug response prediction in cancer: Predominant and emerging trends", Frontiers in Medicine, Section Prediction Oncology, 2023
