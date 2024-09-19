IMPROVE API
=================================
.. Deep learning models are divided into three distinct steps in the IMPROVE framework, each with their own set of parameters.

To comply with the IMPROVE model structure, prediction models must include three distinct scripts responsible for preprocessing, training, and inference. Each script has its own set of parameters, promoting better organization, readability, and preventing potential conflicts between the different stages of the model's workflow.

| 1. Preprocess
| Takes raw benchmark data (feature representations, the predicted variable, and splits) and transforms the data into ML data (i.e., model input data) and splits the data into training, validation, and inference splits.

| 2. Train
| Trains the model using the ML data for training and validation splits and saves the model and validation metrics.

| 3. Infer
| Uses the saved model to perform inference with the inference split of the ML data.

Additionally, general IMPROVE parameters are used for every model, as well as application-specific parameters (e.g. DRP). Model curators can create model-specific parameters, and these can be found HERE. `TODO` define HERE



.. toctree::
   :titlesonly:

   Preprocess <api_preprocess>
   Train <api_train>
   Infer <api_infer>
   Utility Functions <api_util>
   Creating Model-Specific Parameters <api_model>
   Configuration Files <api_config>

