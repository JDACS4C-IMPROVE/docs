Curating Models
=================================
NATASHA: edit this
A central goal of the IMPROVE framework is the automated execution of community deep learning models so that they can be compared to each other under a wide range of conditions.

Three standards needed to automate execution across a collection of models address command line parameters, model hyperparameters, and the return value from a successful training process.

1.  Standard command line parameters are needed so that code that calls to multiple models can be simplified by only knowing one set of command line parameter keywords.

2.  Model hyperparameter keywords then map to the command line parameter keywords you can specify in a (model) file. Generally, each should contain at least a default model file containing the hyperparameter keywords and values from the original publication.

3.  The validation loss is generally the return value of the call to run() or main(). 

The IMPROVE library provides stable interfaces that standardize the interfaces of a set of otherwise heterogenous deep learning software.
We welcome members of the community to use the IMPROVE framework and benchmark data to standardize and compare their models. 


The following guides explain various aspects of the IMPROVE framework.


.. toctree::
   :titlesonly:

   Curating Steps <curating_steps>
   Step-by-Step Example <curating_tutorial>
   Contributing a Model <curating_contribute>

