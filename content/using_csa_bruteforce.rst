Brute Force Cross-Study Analysis
==================================

The concept behind Cross-Study Analysis (CSA) is detailed :doc:`here <using_csa>`. 
The brute force method uses a script to loop through the relevant datasets and splits to execute the Cross-Study Analysis.


Setting up CSA with the Brute Force Method
----------------------------------------------------------------------
The brute force method sequentially preprocesses, trains, and performs inference. 

1. Clone the model repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

  git clone <MODEL_REPO>
  cd <MODEL_REPO>
  git checkout <BRANCH>

.. important:: 

   1. Model scripts must be organized as:

      - <MODEL_NAME>_preprocess_improve.py

      - <MODEL_NAME>_train_improve.py

      - <MODEL_NAME>_infer_improve.py
   2. Make sure to follow the IMPROVE lib :doc:`documentation <curating>` to ensure the model is compliant with the IMPROVE framework.
   3. If the model uses supplemental data (i.e. author data), use the provided script in the repo to download this data (e.g. PathDSP/download_author_data.sh).



2. Set up model environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Follow the steps in the model repo to set up the environment for the model and activate the model.

.. code-block:: bash

  conda activate <MODEL_ENV>


3. Clone IMPROVE repo and set PYTHONPATH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Clone the `IMPROVE <https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/develop>`_ repository to a directory of your preference (outside your model directory).

.. code-block:: bash

  cd ..
  git clone https://github.com/JDACS4C-IMPROVE/IMPROVE
  cd IMPROVE
  git checkout develop
  source setup_improve.sh


4. Download benchmark data for cross study analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download benchmark data to the data destination directory using `this <https://github.com/JDACS4C-IMPROVE/IMPROVE/blob/develop/scripts/get-benchmarks>`_. For example:

.. code-block:: bash

  ./scripts/get-benchmarks ./workflows/bruteforce_csa


4. Configure the parameters for cross study analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These should be changed in :code:`csa_bruteforce_params.ini`:

- :code:`model_scripts_dir` set to the path to the model directory containing the model scripts (from step 1).

- :code:`model_name` set to your model name (this should have the same capitalization pattern as your model scripts, e.g. deepttc for deepttc_preprocess_improve.py, etc).

- :code:`epochs` set to max epochs appropriate for your model, or a low number for testing.

- :code:`uses_cuda_name` set to True if your model uses cuda_name as parameter, leave as False if it does not. Also set :code:`cuda_name` if your model uses this.

- :code:`input_supp_data_dir` add this if your model uses supplemental data. Set to the path to this folder, or the name of the folder if it is located in :code:`model_scripts_dir`.

These you may want to change in :code:`csa_bruteforce_params.ini`:

- :code:`csa_outdir` is './bruteforce_output' but you can change to whatever directory you like.

- :code:`source_datasets`, :code:`target_datasets`, and :code:`split_nums` can be modified for testing purposes or quicker runs.

5. Run brute force workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  We recommend running a test with two target datasets, one source dataset, and two splits with two GPUs before performing the full run.
  
  - For testing purposes, change:
  
    - :code:`source_datasets = ["gCSI"]`

    - :code:`target_datasets = ["gCSI", "CCLE"]`

    - :code:`split = ["0", "1"]`
    
  - For complete runs, change:

    - :code:`source_datasets = ["gCSI", "CCLE", "GDSCv1", "GDSCv2", "CTRPv2"]`

    - :code:`target_datasets = ["gCSI", "CCLE", "GDSCv1", "GDSCv2", "CTRPv2"]`

    - :code:`split = ["0","1","2","3","4","5","6","7","8","9"]`


To run with provided config file:

.. code-block:: bash

  python csa_bruteforce_wf.py


To run with an alternate config file:

.. code-block:: bash

  python csa_bruteforce_wf.py --config <YOUR_CONFIG_FILE>


If submitting a job:

.. code-block:: bash

  conda activate <MODEL_ENV>
  export PYTHONPATH=/YOUR/PATH/TO/IMPROVE
  python csa_bruteforce_wf.py --config <YOUR_CONFIG_FILE>

6. Analyze results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After executing the workflow, the inference results, including test data predictions and performance scores, will be available in the output directory specified by the user. 
These results will be organized into subfolders based on the source dataset, target dataset, and split.
To collate and summarize these results, see :doc:`using_csa_postprocess`.
























