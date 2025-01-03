Using Models with Workflows
=================================
With the recent explosion in the number and diversity of supervised learning models, there is a need for standardized evaluation schemes and datasets to benchmark models. 
We are creating both benchmark datasets and benchmark evaluation schemes as part of the IMPROVE framework, beginning with Drug Response Prediction.

Once a deep learning model has been :doc:`curated<curating>` with improvelib, the model can be used in :doc:`benchmark evaluation schemes<EVALUATION>` at scale. 

We currently have benchmark data for :doc:`Drug Response Prediction <CSA_Benchmark_Datasets>`.


The following guides walk through how to run various aspects of the IMPROVE workflows.

.. toctree::
   :titlesonly:
   :maxdepth: 2

   Running a Single Model <using_running>
   Building Containers <using_containers_build>
   CSA <using_csa>
   HPO <using_hpo>
