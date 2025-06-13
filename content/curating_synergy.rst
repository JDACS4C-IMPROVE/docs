Curating a Synergy Model
===========================

Curating a synergy model is similar to curating a Drug Response Prediction model with a few key differences:

Interface changes
^^^^^^^^^^^^^^^^^^^^^

- Data loading doesn't require the creation of data loading objects, instead functions can be called to load the appropriate dataset
- Response dataframes can be loaded in two ways: 1) by loading the individual train/val/test response dataframes, or 2) by loading a single response dataframe with a column indicating which split the row belongs to
- Split files can be a single file name, or a list of files.
- Commonly use preprocessing selections and transformation can be indicated using a parameter and will be automatically performed with the data loading functions

Application-specific differences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Uses the synergy benchmark dataset (details can be found :doc:`here <app_synergy_benchmark>`).
- Two drug IDs and one cell ID
- :code:`y_col_name` should be one of :code:`loewe`, :code:`bliss`, :code:`zip`, :code:`hsa`, :code:`smean`, or :code:`css`.


Core improvelib imports
import improvelib.utils as frm

Synergy imports
from improvelib.applications.synergy.config import SynergyPreprocessConfig
import improvelib.applications.synergy.synergy_utils as syn



Create a config file
<model>_params.ini



