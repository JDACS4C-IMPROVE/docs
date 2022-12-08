Model Curation
==============

Community models refer to public cancer drug response prediction (DRP) models that have been published as peer-reviewed or preprint articles. Existing publications often provide code associated with the publications (usually a in GitHub repo). At this point, no agreed-upon standards or best practices exist for writing reproducible and/or usable code in this field. To address the challenge of working with different DRP models and alleviate model evaluation and comparison, each model is required to be modified using our **model curation** process.

Model curation generally involves three primary steps as described in this section.

1. Get the model running
---------------------
Once you a chose a model to work on, you need to ensure the code is in good state and usable for your analysis. In this step, you may find it useful to reach out to the authors of the repo for help and clarifications.

* Fork the model repo
* Create develop branch where you will modify the code
* Setup the Python computational environment
* Run the model with the original data provided with the repo
* Validate that the results make sense (e.g., reproducible)

2. CANDLE
------------------------
**TODO** all docs relevent to CANLDEizing models.

The next step is modify the repo to make the code CANDLE compliant.

3. Singulairy
---------------------
**TODO** all docs relevent to Singulairy.