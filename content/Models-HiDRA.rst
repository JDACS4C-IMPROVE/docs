=================
HiDRA
=================
Hierarchical Network for Drug Response Prediction with Attention

Model Architecture
--------------------
HiDRA starts with a dense two-layer drug encoding network. The gene expression data is then split up into pathways based on KEGG data, and each pathway has its own dense encoding network with gene-level and pathway-level attention modules that incorporate the drug encodings. Finally, a dense two-layer network takes concatenated drug and pathway outputs and generates an response prediction.

Feature Representation
--------------------

   * Cancer features: 

      * Gene Expression: converted to z-scores for each cell line, genes not present in the KEGG pathway data are removed

   * Drug features: 

       * Drug Fingerprints: 512-bit Morgan fingerprints generated from SMILES strings with rdkit



URLs
--------------------
- `Original GitHub <https://github.com/GIST-CSBL/HiDRA>`__
- `IMPROVE GitHub <https://github.com/JDACS4C-IMPROVE/HiDRA>`__

References
--------------------
`1. <https://pubs.acs.org/doi/full/10.1021/acs.jcim.1c00706>`_ I. Jin and H. Nam. "HiDRA: Hierarchical Network for Drug Response Prediction with Attention", J. Chem. Inf. Model., 2021
