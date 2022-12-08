========================
Drug Response Prediction
========================

----
Modeling drug response
----
.. DRP Formulation
A drug response prediction (DRP) model can be represented by :math:`r = f(d, c)`, where :math:`f` is the analytical model designed to predict the response :math:`r` of cancer :math:`c` to the treatment by drug :math:`d`.
The function :math:`f` is implemented with a neural network (NN) architecture.
This formulation is for pan-cancer and multi-drug prediction model where both cancer and drug representations are needed to predict response.
A special case is drug-specific models designed to make predictions for a drug or drug family (e.g., drugs with the same mechanism of action (MoA)). These models learn from cancer features only and can be formulated as :math:`r=f_D(c)`. 

.. https://labs.bilimedtech.com/workshops/rst/writing-rst-6.html
.. figure:: ../images/NN_architecture.png
    :width: 350
    :align: center

    A neural network architecture for cancer drug response prediction (DRP). The model is pan-cancer and multi-drug where both cancer and drug representations are used to predict the response.

----
Data
----
.. Screening data
Screening data
==============
Drug screening experiments can be performed with various pre-clinical cancer models such as cell lines, organoids, and xenografts, where cancer samples are screened against a library of drug compounds. Regardless of specific cancer models, the screening space can be characterized by the involved drugs and cancers. The 2-D matrix illustrates such a space composed of a finite number of known cancer cases and drugs, where the marked coordinates symbolize that treatment responses are available for these combinations. 
Results of the screening experiments can be organized in a table format, represting the **response data** .

.. figure:: ../images/Screening_data.png
    :width: 500
    :align: center

    Several drug and cancer feature representations that are used as input features for a DRP model.

.. Feature representations
Feature representations
=======================
The different cancers and drugs in a screening experiment can be numerically described using various representations that can serve as features in a DL model.
In most DRP models, cancer is represented using various omics data types which are often provided with public drug screening studies (e.g., CCLE, GDSC). In certain, however, additional bioinformatics processing methods are applied to further preprocess the omics for the downstream ML analysis. 
The drugs are generallity represtend with SMILES strings, fingerprints (binary vectors), descriptors, and molecular graph structures. These representations can be calculated using open-source cheminformatics software packages such as RDKit and Mordred.

.. figure:: ../images/Feature_representations.png
    :width: 500
    :align: center

    Drug and cancer feature representaions.

.. Raw data
Raw DRP data
============
The data required to develop (train and validate) a DRP model, consists of three primary components:
1) response data
2) cancer representations
3) drug representations
These data are generally stored in tabular structures.
In the context of the DRP problem, we define these data structures as **raw DRP data**.


.. ML data
ML data
=======

Deep learning (DL) models built using popular DL frameworks can take various types of data from simple CSV to more complex structures such as TFRecords.
Constructing datasets for DRP models generally requires combining heterogeneous data such as cancer and drug information and treatment response values (see the definition of **raw DRP data**.
In this context, we distinguish between two types of data, **raw DRP data** (described above) and **ML data**.
ML data refers to data files that can be directly supplied to models for training and testing (e.g., TFRecords with TensorFlow, **.pt** with PyTorch).

Preprocessing scripts are often required to generate ML data from raw data. However, not all public repositories provide the necessary scripts.