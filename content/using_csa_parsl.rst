Scaling Cross-Study Analysis with Parsl
=========================================

The concept behind Cross-Study Analysis (CSA) is detailed :doc:`here <eval_csa>`. 
To enable parallel execution, Parsl parallel processing library [1] is used to implement the cross-study analysis workflow. 
The figure below illustrates the cross-study workflow with Parsl. The main components of the workflow - preprocess, train and infer - are implemented as Parsl apps, each returning ‘futures’ that monitor progress of the execution. 
For example, once preprocessing for CCLE split 1 is complete, the corresponding ‘preprocess_futures’ will trigger training for CCLE split 1. Inference begins after training, as indicated by ‘train_futures’. 
Parsl also allow parallel execution using multiple GPUs, as specified by the user. 
The cross-study analysis workflow using Parsl has been successfully implemented on the GraphDRP model using multiple GPUs on the Lambda machine managed by CELS at Argonne National Laboratory.


.. figure:: ../images/using_csa_parsl_diagram.png
   :class: with-border

Cross-study analysis workflow using Parsl parallel processing library

Setting up CSA with Parsl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are setting up CSA with Parsl for the first time with your model:

- Copy the scripts from `here <https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/develop/workflows/parsl_csa>`_ to your model repo.

- Change :code:`<MODEL_NAME>` to your model name (e.g. :code:`graphdrp`).

- Commit changes to develop branch.

Running CSA with Parsl
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Clone your model repo (example here for GraphDRP):

.. code-block:: bash

  git clone https://github.com/JDACS4C-IMPROVE/GraphDRP.git
  cd GraphDRP
  git checkout develop
  cd ..

2. Create environment and install dependencies (example here for GraphDRP):

   a. Create conda env using :code:`env_gdrp_37_improve.yml` and activate the environment

   .. code-block:: bash

     conda env create -f env_gdrp_37_improve.yml
     conda activate graphdrp_py37_improve

   b. (TODO: PIP INSTALL) 

   c. Install Parsl (2023.6.19):

   .. code-block:: bash

     pip install parsl 

   If you see an error during execution you may have to do this:

   .. code-block:: bash

     export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7


3. (TODO: change to download_csa.sh after pip install and stable branches/release.) TEMP FOR CURATORS: Set PYTHONPATH per usual to the correct (currently develop) branch of improvelib. Make sure csa_data is in the model repo.

4. Run cross study analysis using PARSL (see below for how to change CSA parameters):

.. code-block:: bash

  python workflow_csa.py

5. Analyze results:

After executing the workflow, the inference results, including test data predictions and performance scores, will be available in the output directory specified by the user. 
These results will be organized into subfolders based on the source dataset, target dataset, and split.

Changing CSA Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**csa_params.ini** contains parameters necessary for the workflow. The user can change the parameters inside this configuration file.

- :code:`input_dir`: Location of raw data for cross study analysis. 

- :code:`output_dir`: Location of the output. The subdirectories in the output_dir are organized as:

  - ml_data: Contains pre-processed data

  - models: Contains trained models

  - infer: Contains inference results

- :code:`source_datasets`: List of source_datasets for cross study analysis. With the current benchmark datasets this can be a subset of CCLE, gCSI, GDSCv1, GDSCv2 and CTRPv2

- :code:`target_datasets`: List of source_datasets for cross study analysis. With the current benchmark datasets this can be a subset of CCLE, gCSI, GDSCv1, GDSCv2 and CTRPv2

- :code:`split`: Splits of the source datasets for cross study analysis

- :code:`hyperparameters_file`: Name of the json file containing hyperparameters per dataset. In this template two hyperparameter files are given:

  - hyperparameters_hpo.json: Contains hyperparameters optimized separately on all source datasets

  - hyperparameters_default.json : Contains default values of the hyperparameters for the model

- :code:`model_name`: Name of the model for cross study analysis

- :code:`epochs`: Number of epochs for the model

- :code:`y_col_name`: Response variable used in the model eg: auc

- :code:`use_singularity`: True, if the model files are available in a singularity container

- :code:`singularity_image`: Singularity image file (.sif) of the model scripts (optional)

- :code:`only_cross_study`: True, if only cross study analysis is needed without within study inferences

**hyperparameters.json** contains a dictionary of optimized hyperparameters for the models. The key to the dictionary is the model name, which contains another dictionary with source dataset names as keys. The two hyperparameters considered for this analysis are: batch_size and learning_rate. 
The hyperparameters are optimized using [Supervisor](https://github.com/JDACS4C-IMPROVE/HPO).


To run cross study analysis with a different configuration file:

.. code-block:: bash
  
  python workflow_csa.py --config_file <CONFIG_FILE>



References
------------
`1. <https://dl.acm.org/doi/10.1145/3307681.3325400>`_ Y. Babuji et al. "Parsl: Pervasive Parallel Programming in Python", 28th ACM International Symposium on High-Performance Parallel and Distributed Computing (HPDC), 2019

