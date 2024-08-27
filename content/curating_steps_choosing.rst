Internal Standards for Model Curation
======================================================

IMPROVE members use the following criteria in selecting and reproducing a model.

1. Choosing a model
---------------------
Look for the following attributes when choosing a community model to curate.

* Deep learning methods in Python using PyTorch or Keras/TensorFlow
* Data features and response data that match data features currently available in the benchmark dataset
* Publically available publication (preference for peer-reviewed)
* Code available on GitHub
* Preference for models with unique architecture or data preprocessing, elements of interpretability, or quantification of uncertainty of predictions.

2. Getting the model running
------------------------------
Once you a chose a model to work on, you need to ensure the code is in good state and usable for your analysis. 
In this step, you may find it useful to reach out to the authors of the repo for help and clarifications.

* Fork the model repo
* Create develop branch where you will modify the code
* Setup the Python computational environment
* Run the model with the original data provided with the repo
* Validate that the results make sense (e.g., reproducible)

3. Curating the model
------------------------
* Follow the steps on the previous page to curate the model
* Ensure that the performance is in line with original results with a similar dataset and features from the benchmark dataset.


