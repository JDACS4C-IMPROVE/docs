Using Non-Benchmark Data
========================

One of the strengths of IMPROVE is the use of benchmark datasets to compare models. However, the standardization provided
by IMPROVE also makes it an excellent system to perform experiments to better understand the models and the data. There
are cases where you may want to compare external data to the benchmark data and evaluate the performance. IMPROVE makes it easy to do so.

For example, say you are interested in :doc:`app_drp`. The :doc:`app_drp_benchmark` includes cancer_discretized_copy_number.tsv, in which  
-2, -1, 0, 1, 2 indicate deep deletion, heterozygous deletion, neutral, copy number gain, copy number amplification, respectively.
We might hypothesize that minor changes in copy number don't matter and that the model would perform better if we binarize 
deep deletions or amplifications (-2 or 2) vs minor changes in copy number (-1, 0, 1).

We can take the cancer_discretized_copy_number.tsv file, change -2 or 2 to 1 and -1, 0, or 1 to 0. We'll save this file in 
:code:`/home/my_data` as :code:`cancer_binary_cnv.tsv`.

.. warning::

    All data files should be tab-separated, with no index numbers. The first column in the text file will be read as the 
    index and *must* contain the IDs. The feature names (gene names in this example) should be the column headers.

We look through the :doc:`app_drp_models` and see that :doc:`Models-tCNNS` uses discretized copy number. We can run 
the model (see :doc:`using_running` for details) like normal except at the preprocessing step, we'll specify the 
location of the new CNV file we made like so:

.. code-block:: bash

    python tcnns_preprocess_improve.py --input_dir ./drp_v2 --cell_cnv_file /home/my_data/cancer_binary_cnv.tsv

That's it! You can run *train* and *infer* like normal, and compare your results.
