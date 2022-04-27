=================
DeepCDR  
=================
-------------------------
DeepCDR: A Hybrid Graph Convolutional Network For Predicting Cancer Drug Response
-------------------------

Structure
============
The DeepCDR model has four subnetworks for processing drugs, transcripts, mutations, and DNA methylations. The subnetwork for drugs has three graph convolution layers. The subnetworks for transcripts and DNA methylations have two dense layers. The subnetwork for mutations has two 1D convolution layers and one dense layer. The concatenated features from four different modalities are then forwarded to 1D CNN layers for prediction.

Data Sources
============
- IC50 drug response data from the Genomics of Drug Sensitivity in Cancer (GDSC)
- Cell line transcript, mutation, and methylation data from the Cancer Cell Line Encyclopedia (CCLE)
- Patient transcript, mutation, and methylation data and associated drug responses from the Cancer Genome Atlas (TCGA).

Data and preprocessing
============
- The GDSC drug response data included 107,446 instances across 561 cancer cell lines and 238 drugs. Drug response was measured by IC50.
- For multi-omics profiles of cancer cell lines, data related to 697 genes included in the COSMIC Cancer Gene Census were considered. For genomic mutation data, 34,673 unique mutation positions including SNPs and Indels within the above genes were collected. The genomic mutations of each cancer cell line were represented as a binary feature vector in which ’1’ denoted a mutated position and ‘0’ denoted a non-mutated position. For gene expression data, the TPM value of gene expression was log2 transformed and quantile normalized. The gene expression of each cell line was represented by a 697-dimensional feature vector. The DNA methylation data was obtained for the promoter 1 kb upstream TSS region. A median value interpolation was applied on the data to impute missing values. The methylation of each cell line was represented by a 808-dimensional feature vector.
- TCGA patients with cervical squamous cell carcinoma and endocervical adenocarcinoma were selected with two criterions. (i) The gene mutation, gene expression and DNA methylation data were available. (ii) The clinic annotation of drug response was also available. A dataset including 54 records across 31 patients and 12 drugs was collected. The molecular data were processed in a similar way as the cell line data. 

Evaluation
============
- Cross-validation analysis on GDSC data without hard partitioning on cell lines and drugs.
- Cross-validation analysis on GDSC data with hard partitioning on cell lines.
- Cross-validation analysis on GDSC data with hard partitioning on drugs.
- Validation of generalizability to TCGA patient data.

URLs
============
- Original GitHub: https://github.com/kimmo1019/DeepCDR
- IMPROVE GitHub: 

Reference
---------
Liu et al., DeepCDR: a hybrid graph convolutional network for predicting cancer drug response, Bioinformatics, Volume 36, Issue Supplement_2, December 2020, Pages i911–i918,
