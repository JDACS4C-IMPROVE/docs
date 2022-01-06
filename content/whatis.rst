What is the IMPROVE project?
============================

Background
----------

From 2015 to 2020, the joint DOE-NCI Pilot 1 project has developed a foundational set of machine learning models, related research, and infrastructure for prediction of tumor drug response to single and combination agents. These models have been benchmarked against models in the literature, compared to dozens of alternative formulations (ranging from classical machine learning methods to deep learning), and evaluated on a broad range of available training data. Some of these models have become benchmarks for the ECP-CANDLE project (https://github.com/ECP-Candle/Benchmarks).

There were many lessons learned during this work that led to the Innovative Methodologies and New Data for Predictive Oncology Model Evaluation (IMPROVE) project. For example, it became clear that while considerable progress has been made in the last decade by the cancer research community in the formulation and training of machine learning models for cancer, the community does not have a common set of well-documented and well-characterized approaches to constructing, training, and validating cancer drug response models.

It is difficult to compare new modelling results in the literature with those from previous studies due to different choices of normalization, encoding, filtering, etc. In addition, there is a lack of well-curated and standardized training and testing datasets, and lack of broadly accepted featurization for both tumors associated data and representations of drugs. Understanding and recognizing new innovations in drug response modeling are less clear due to ongoing challenges with data quality and data integration.

With the IMPROVE project, we address some of the challenges around model comparisons and dataset standardization and availability through the development and provision of a software framework to make it routine practice for the broader community (cancer research and other areas) to compare new machine learning modeling approaches to previous models in a rigorous and comprehensive fashion.

