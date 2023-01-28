=================
PathDSP
=================
PathDSP is a framework for "Explainable drug sensitivity prediction through cancer pathway enrichment" (title of paper).

---------
Structure
---------
From Abstract: PathDSP: a pathway-based model for drug sensitivity prediction that integrates chemical structure information with enrichment of cancer signaling pathways across drug-associated genes, gene expression, mutation and copy number variation data to predict drug response on the Genomics of Drug Sensitivity in Cancer dataset. Using a deep neural network, we outperform state-of-the-art deep learning models, while demonstrating good generalizability a separate dataset of the Cancer Cell Line Encyclopedia as well as provide explainable results, demonstrated through case studies that are in line with current knowledge. Additionally, our pathway-based model achieved a good performance when predicting unseen drugs and cells, with potential utility for drug development and for guiding individualized medicine.

----
Data
----

Data sources
------------
The primary data sources that have been used to construct datasets for model training and testing (i.e., ML data) include:

"Drug sensitivity data, cell-line gene expression, somatic mutation and copy number variation data for 319 cancer cell lines and 153 drugs was downloaded from Genomics of Drug Sensitivity in Cancer (GDSC downloaded from https://www.cancerrxgene.org/downloads/bulk_download.) Drug sensitivity data of 24 drugs and 478 cancer cell lines from the Cancer Cell Line Encyclopedia (CCLE) were downloaded through the DepMap portal (https://depmap.org/portal/download/, release version: public 20Q1), which also include gene expression, mutation and copy number variation data for those cancer cell lines. Primary target data was downloaded from GDSC, and PID pathways were downloaded from MSigDB. Protein–protein network was downloaded from STRING database, including protein interactions, co-expression and text-mined interactions."


Raw data
--------
The raw data includes the following:

#. `GDSCv2.Gao2015.Powell2020.Lee2021.GeoSearch.Ding2016.CHEM.256.MBits.txt`: Looks like drug response from GDSC.

#. `GDSCv2.Gao2015.Powell2020.Lee2021.GeoSearch.Ding2016.DGNet.NetPEA.txt`: "We collected all mutations for each cell line to perform network-based pathway enrichment analysis by the NetPEA algorithm, which calculates an enrichment score by measuring the closeness of pathway genes to a given gene set within a protein–protein interaction (PPI) network." 

#. `GDSCv2.Powell2020.EXP.ssGSEA.txt`: "Gene expression data were measured by transcripts per million (TPM) and log-transformed. We imputed with mean for the rest of missing values. Enrichment score (ES) of each PID pathway in each cell line was calculated using the single-sample Gene Set Enrichment (ssGSEA) algorithm52 through GSEApy (https://gseapy.readthedocs.io/en/master/gseapy_example.html). We ran permutation test for 1000 times and normalized ES scores by the size of gene set to obtain normalized ES (i.e., NES). We used the resulting pathway enrichment matrix with size of 319 cancer cell lines by 196 pathways as the gene expression feature (EXP)."

#. `GDSCv2.resp_PowellAUC.Alias.txt`: Set of aliases [Therapy | Sample | Response | Cancer types | Datasets | Alias]

The raw data is available in `this highly suspicious location <http://chia.team/IMPROVE_data/data>`__.

ML data
-------
The script `dataProcess.py <https://github.com/JDACS4C-IMPROVE/DrugGCN/blob/develop/dataProcess.py>`__ uses raw data to generate ML data that can be used to train and test with DrugGCN. The necessary raw data are automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()` and processed. 

The ML data files are available in `this FTP location <https://ftp.mcs.anl.gov/pub/candle/public/improve/model_curation_data/DrugGCN/druggcn_data_processed.tar.gz>`__. These files can be automatically downloaded from the FTP server using the `candle_lib` utility function `get_file()`.

The ML data files include the following:

- **Cancer features**.  L1000 and Var1000 folders with gene expression and protein-protein interaction files: 

  - `groupEXP.csv`: Gene expression data of selected genes.
  - `groupEXP_foldChange.csv`: Fold change of gene expression data of selected genes.
  - `groupPPI.csv`: PPI data of selected genes where values are weights of the interactions that reflect the amount of available evidence of the interaction between two genes.
   
- **Response data**.  IC50 or AUC values of 201 drugs and 734 cell lines.

  - `Table_S6_GDSC_Drug_response_IC50.csv`
  - `Table_S7_GDSC_Drug_response_AUC.csv`

The user can specify which dataset, L1000 or Var1000, and which response data, IC50 or AUC, to use when training and testing the model.


----------
Evaluation
----------
Four evaluation schemes were used for the analysis of prediction performance.

- L1000-IC50: Gene set of 663 genes using the list of landmark genes derived from LINCS L1000 project and IC50 drug response values.
- L1000-AUC: Gene set of 663 genes using the list of landmark genes derived from LINCS L1000 project and AUC drug response values.
- Var1000-IC50: Gene set of the top 1000 variable genes and IC50 drug response values.
- Var1000-AUC: Gene set of the top 1000 variable genes and AUC drug response values.


----
URLs
----
- `Original Developer's GitHub <https://github.com/TangYiChing/PathDSP>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/PathDSP/tree/develop>`__
- `Data <http://chia.team/IMPROVE_data/data>`__


----------
References
----------
Tang, Yi-Ching, and Assaf Gottlieb. "Explainable drug sensitivity prediction through cancer pathway enrichment." Scientific reports 11, no. 1 (2021): 1-10. https://www.nature.com/articles/s41598-021-82612-7
