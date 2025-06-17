Benchmark Data for Synergy 
=============================
The benchmark data for Synergy was created using this pipeline. 


.. list-table:: Number of cell lines, drugs, and experiments in the benchmark datasets.
   :header-rows: 1  

   * - Dataset
     - Number of cell lines
     - Number of drugs
     - Number of experiments
     - Number of unique experiments
   * - ALMANAC
     - 57
     - 103
     - 296,166
     - 294,152
   * - FRIEDMAN
     - 24
     - 108
     - 129,921
     - 129,921
   * - ONEIL
     - 35
     - 38
     - 82,712
     - 20,405
   * - ASTRAZENECA
     - 97
     - 116
     - 15,365
     - 15,233
   * - NCATS-1
     - 10
     - 1910
     - 9123
     - 7401
   * - FORCINA
     - 1
     - 1818
     - 1818
     - 1818
   * - FLOBAK
     - 8
     - 19
     - 9984
     - 1392
   * - SMALL
     - 6
     - 34
     - 264
     - 208
   
.. warning:: 
  
  The 'SMALL' dataset is a collection of smaller experiments and should be used with caution.

Data Location
----------------
- ADD FTP

Data File Description
-----------------------

* :code:`y_data` folder includes synergy measurements
    * synergy.tsv: file containing observations. Columns are as follows:
        * DepMapID: ID for cell line.
        * DrugID_row: ID for the first drug of the combination.
        * DrugID_col: ID for the second drug of the combination.
        * study: Study name identifying where the experiment originates from.
        * loewe: Loewe synergy value.
        * bliss: Bliss synergy value.
        * zip: ZIP synergy value.
        * hsa: HSA synergy value.
        * smean: Smean synergy value.
        * css: CSS synergy value.
* :code:`splits` folder includes sample indices corresponding to rows in :code:`synergy.tsv` in :code:`y_data` folder. Sample index starts with 0.
* :code:`x_data` folder includes multi-omics data of cancer cell lines and multi-modal data of drugs. The index of the files is the drug or cell ID and the columns are the features.
    * cell_cnv_continuous.tsv: copy number (CN), log2 transformed (log2(CN ratio + 1)) . Computed by a weighted average along the genomic coordinate.
    * cell_cnv_discretized.tsv: discretized gene copy numbers. -2, -1, 0, 1, 2 indicate deep deletion, heterozygous deletion, neutral, copy number gain, copy number amplification, respectively. 
    * cell_mutation_delet.tsv: gene-level mutation counts in cell lines of all deleterious mutations.
    * cell_mutation_nonsynon.tsv: gene-level mutation counts in cell lines of all non-synonymous mutations.
    * cell_transcriptomics.tsv: TPM (transcripts per million reads mapped), log2 tranformed (log2(TPM+1)) gene expression values.
    * drug_SMILES.tsv: SMILES strings of drugs.
    * drug_SMILES.tsv: SMILES strings of drugs, canonicalized with RDKit.
    * drug_ecfp2_nbits256.tsv: ecfp2 binary fingerprints of drugs with 256 bits.
    * drug_ecfp2_nbits1024.tsv: ecfp2 binary fingerprints of drugs with 1024 bits.
    * drug_ecfp4_nbits256.tsv: ecfp4 binary fingerprints of drugs with 256 bits.
    * drug_ecfp4_nbits1024.tsv: ecfp4 binary fingerprints of drugs with 1024 bits.
    * drug_ecfp6_nbits256.tsv: ecfp6 binary fingerprints of drugs with 256 bits.
    * drug_ecfp6_nbits1024.tsv: ecfp6 binary fingerprints of drugs with 1024 bits.
    * drug_infomax.tsv: Infomax fingerprints of durgs.
    * drug_mordred.tsv: Mordred descriptors of drugs.


Data Sources
-------------------

.. list-table:: Source of data in the synergy benchmark dataset.
   :header-rows: 1  

   * - Data type
     - Source
     - Version
     - Link
   * - Response
     - DrugComb
     - v1.5
     - https://drugcomb.org/download/
   * - Drug SMILES
     - DrugComb
     - v1.5
     - https://drugcomb.org/drugs/
   * - Cell line omics
     - DepMap
     - 22Q2
     - https://depmap.org/portal/download/all/

