What is the IMPROVE project?
============================
IMPROVE aims to establish methodology to systematically and rigorously compare supervised learning models. 
1) IMPROVE Framework: standardized scaffolding for machine learning models, written in Python
2) IMPROVE Benchmark Datasets: a collection of standardized data for each application to allow for benchmarking of models


In the realm of supervised learning models, three fundamental components exist: data preparation, model training and hyperparameter optimization (HPO), and performance evaluation [`1 <https://www.frontiersin.org/articles/10.3389/fmed.2023.1086097/full>`_].
Recognizing this norm, we propose to establish three distinct scripts, with each script dedicated to one of these essential components.
By establishing this convention and separating the components into separate scripts we aim to enhance code readability, provenance, and maintainability.
The first script handles **preprocessing** of input data, the second manages model **training**, and the third enables the utilization of the model in **inference** mode.
All these scripts should be organized in a modular and flexible manner to enable seamless combination, integration, and workflow generation.
This modular separation of components aims to facilitate an efficient and manageable workflow design and implemenation.


.. figure:: ../images/ML_pipeline_steps.png
    :width: 600
    :align: center

    General steps in developing and using prediction model.




For more information
----------------------

.. toctree::
   :titlesonly:

   Background
   Future Directions <FutureDirections>
   Acknowledgments <acknowledgment>


References
---------------------------------
`1. <https://www.frontiersin.org/articles/10.3389/fmed.2023.1086097/full>`_ A. Partin et al. "Deep learning methods for drug response prediction in cancer: Predominant and emerging trends", Frontiers in Medicine, Section Prediction Oncology, 2023
