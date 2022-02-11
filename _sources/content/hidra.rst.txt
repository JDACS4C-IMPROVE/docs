=================
HiDRA
=================
-------------------------
Hierarchical Network for Drug Response Prediction with Attention
-------------------------

Structure
============

HiDRA consists of four smaller networks: a drug feature encoding network, which takes SMILES strings converted to Morgan fingerprints; a set of gene-level networks which encode expression data for genes in each pathway; a pathway-level network that takes in output of the individual gene-level networks; and a prediction network that uses drug encodings and pathway output to predict ln(IC50). Each sub-network consists of two dense layers and an attention module (tanh + softmax activation).

Input
============

HiDRA uses cell line expression data, drug SMILES, and drug/cell line IC50 pairs to predict ln(IC50) values for new pairs. Required files are:

- RMA normalized expression data for 968 cell lines from GDSC1000_.
- Metadata file for cell lines
- SMILES strings for 235 drugs in GDSC1000 data
- Drug/cell line IC50 pairs
- Pathway-to-gene file from KEGG


Reference
---------
Jin I, Nam H. HiDRA: Hierarchical Network for Drug Response Prediction with Attention. *Journal of Chemical Information and Modeling*. 2021 Aug 3;61(8):3858-67.


.. _GDSC1000: https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources//Data/preprocessed/Cell_line_RMA_proc_basalExp.txt.zip