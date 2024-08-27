Curating a Model
===========================
NATASHA: WRITE THIS

IMPROVE members use the following criteria in selecting and reproducing a model: :doc:`curating_steps_choosing`.

Separating preprocess, train, and infer
----------------------------------------

Split them up into the three, define, describe how to name the files
Note probably have to implement saving of model.

Place model code in appropriate templates
-------------------------------------------
Templates available HERE
Model code should be in run(), but run() can call other functions as needed.
Any additional imports should be added as appropriate
Describe (and link to) implementation of model spec param
Parameters - IMPROVE provided parameters should be used as appropriate so that workflows function properly (e.g. HPO will use the provided --epochs parameter)
Other model-specific parameters not included as part of IMPROVE can be used by LINK TO THIS PAGE.

Explain how to set up inputs and output folders.

Implement IMPROVE benchmark data
-------------------------------------
At this step in the curation process, we recommend running the code with the original data to ensure everything is 
implemented correctly and the model runs.
Explain how to load the data. (for DRP at least)




