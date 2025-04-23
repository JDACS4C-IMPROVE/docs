What is the IMPROVE project?
============================
IMPROVE aims to establish methodology to systematically and rigorously compare supervised learning models. To this end, IMPROVE has four components:

1) IMPROVE Python Package (improvelib): Python tools and protocols for standardizing model code structure, facilitating modular code allowing to design complex workflows

2) IMPROVE Workflows :doc:`Evaluation Schemes <BenchmarkEvaluationSchemes>`: distributed and modular workflows for large-scale model evaluation and downstream model comparison

3) Benchmark Datasets: standardized datasets (for each scientific application), enabling consistent and rigorous model benchmarking

4) Community Curated Models: A diverse collection of models from the scientific community (a collocation per application), curated within the IMPROVE framework and organized by application, providing a baseline for comparison


IMPROVE can be applied to a variety of supervised learning models. We have begun with the :doc:`Drug Response Prediction <app_drp_intro>` problem, standardizing pan-cancer, pan-drug :doc:`community models <Models>` that predict monotherapy drug response with a standardized :doc:`benchmark dataset <CSA_Benchmark_Datasets>`.




For more information
----------------------

.. toctree::
   :titlesonly:

   Background <whatis_background>
   Future Directions <whatis_future>
   Acknowledgments <whatis_acknowledgment>


Access the code base https://github.com/JDACS4C-IMPROVE/

References
---------------------------------
`1. <https://www.frontiersin.org/articles/10.3389/fmed.2023.1086097/full>`_ A. Partin et al. "Deep learning methods for drug response prediction in cancer: Predominant and emerging trends", Frontiers in Medicine, Section Prediction Oncology, 2023

`2. <https://arxiv.org/abs/2409.12215>`_ JC. Overbeek and A. Partin et al. "Assessing Reusability of Deep Learning-Based Monotherapy Drug Response Prediction Models Trained with Omics Data", arXiv, 2024

`3. <https://arxiv.org/abs/2503.14356>`_ A. Partin and P. Vasanthakumari et al. "Benchmarking community drug response prediction models: datasets, models, tools, and metrics for cross-dataset generalization analysis", arXiv, 2025