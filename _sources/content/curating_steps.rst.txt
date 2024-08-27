Curating a Model
===========================
NATASHA: WRITE THIS

Split them up into the three, define, describe how to name the files

Model code should be in run().

Explain how to set up imports and main()

Explain how to set up inputs and output folders.

Explain how to load the data.

Note probably have to implement saving of model.

Automated training of a collection of models and using those models in inference mode under a wide range of conditions is made possible through standardization while maintainiing a best effort representation of the authors original architecture and huperparameters.

Curated community model are standardized using improvelib. 

1. Standard arguement parser will be used.


   
   b. All model arguements are passed to the model by way of the candle --config_file option. For example:
   
   ```
   cadre_candle.py --config_file some_file_name
   ```
   
   b. Non-standard keywords (meaning not represented in the candle keywords) shall be added to the additional_definitions so that they can be included in that they are properly passed to and parsed by the model.  If these keywords (arguments) are not in additional_definitions they can't be changed from the command line.



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
**TODO** all docs relevant to CANDLEizing models.

The next step is modify the repo to make the code CANDLE compliant.

3. Singularity
---------------------
**TODO** all docs relevant to Singularity.