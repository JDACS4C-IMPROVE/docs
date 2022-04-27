=================
IGTD  
=================
-------------------------
Converting Tabular Data into Images for Deep Learning With Convolutional Neural Networks
-------------------------

Structure
============
The IGTD package is composed of two components. The first component implements the IGTD approach to convert tabular data into images, which generates one heatmap for each sample. In the heatmaps, similar features are closely located, while dissimilar features are far apartr. The pixel intensity indicates the  value of the assoicated feature. The second component is a convolutional neural network (CNN). The CNN model has subnetworks for the input of multiple data modalities. Each subnetwork is composed of convolution layers processing the images of one data modality. Multiple kernels can be used simultaneously to encode the same image modality. After the concatenation of embedded features from multiple modalities, dense layers are used to further process the features to make predictions. Both regression and classification predictions are supported.

Data Sources
============
The Cancer Terapeutics Response Portal v2 (CTRP)
The Genomics of Drug Sensitivity in Cancer (GDSC)

Data and Preprocessing
============
Genes were filtered according to their variations across gene expression profiles. 2,500 genes with the largest variances were selected and the gene expression profiles were converted into 50 * 50 images using the default parameter setting of IGTD method.

Drug descriptors were filtered according to their variations across drugs. 2,500 descriptors with the largest variances were selected and the drug descriptor profiles were converted into 50 * 50 images using the default parameter setting of IGTD method.

Drug response was measured by the area under the dose response curve (AUC) for the dose range of [10\ :sup:`−10` M, 10\ :sup:`−4` M]. The AUC value was then normalized by the dose range. After normalization, the AUC value is between 0 and 1. 0 indicates complete response and 1 indicates no response.

Evaluation
============
The model was evaluated through cross-validations on the CTRP and GDSC drug screening datasets, in which the same cell line or drug can appear simultaneously in the training, validation, and testing sets.

URLs
============
- Original GitHub: https://github.com/zhuyitan/IGTD
- IMPROVE GitHub: 

Reference
---------
Zhu et al., Converting tabular data into images for deep learning with convolutional neural networks, Scientific Reports, vol. 11, article number: 11325 (2021)
