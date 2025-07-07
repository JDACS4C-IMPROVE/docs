Synergy Prediction
========================


Modeling drug synergy
-------------------------
A drug synergy model can be represented by :math:`s = f(d1, d2, c)`, where :math:`f` is the analytical model designed to predict the synergy value :math:`s` of cancer :math:`c` to the treatment by two drugs :math:`d1` and :math:`d2`.
The function :math:`f` is implemented with a neural network (NN) architecture.
This formulation is for pan-cancer and pan-drug prediction model where both cancer and drug representations are needed to predict response.
 


Data
----

Synergy data (y data)
----------------------
Synergy screening experiments are typically performed with various pre-clinical cancer cell line models and ranges of two 
different drug compounds. From the viability data collected from these screenings, synergy metrics such as Loewe, Bliss, and others 
are calculated to create a single numerical representation of the synergy between two drugs for each cell line.


Feature representations (x data)
-----------------------------------
The cancer models (cell lines) are usually represented by omics data (transcriptomics, mutation data, copy number, etc). 
These features are publically available, typically preprocessed by standard bioinformatic algorithms (e.g. as TPM for transcriptomics).
The drugs are typically represented by SMILES strings, fingerprints, descriptors, or molecular graph structures. 
These representations can be calculated using open-source cheminformatics software packages such as RDKit and Mordred.


ML data (preprocessing)
---------------------------
The raw synergy data and feature representations outline above are further preprocessed by ML/DL models to create **ML data** 
which can be directly ingested by the model. This can include subsetting features, normalizing features, setting cutoffs for synergy 
(in the case of classification models). This also includes splitting the data into train/val/test splits and saving the data in a format 
appropriate for the model.

