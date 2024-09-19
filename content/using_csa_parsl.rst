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
This Parsl workflow has been configured for use on lambda at Argonne National Laboratory. 
For other systems, we recommend using the :doc:`Brute Force method <using_csa_bruteforce>`.
We recommend running a test with two target datasets, one source dataset, and two splits with two GPUs before performing the full run.

If you are setting up CSA with Parsl for the first time with your model:

- Copy the scripts from `here <https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/develop/workflows/parsl_csa>`_ to your model repo.

- Configure the configuration file :code:`csa_params.ini`.

  - Change :code:`<MODEL_NAME>` to your model name (e.g. :code:`graphdrp`).

  - Change :code:`<NAME_OF_YOUR_MODEL_CONDA_ENVIRONMENT>` to your model environment name.

  - Change :code:`epochs` as necessary.

  - Change :code:`available_accelerators` to the available GPUs.

  - For testing purposes, change:
  
    - :code:`source_datasets = ["gCSI"]`

    - :code:`target_datasets = ["gCSI", "CCLE"]`

    - :code:`split = ["0", "1"]`

  - For complete runs, change:

    - :code:`source_datasets = ["gCSI", "CCLE", "GDSCv1", "GDSCv2", "CTRPv2"]`

    - :code:`target_datasets = ["gCSI", "CCLE", "GDSCv1", "GDSCv2", "CTRPv2"]`

    - :code:`split = ["0","1","2","3","4","5","6","7","8","9"]`

    - :code:`available_accelerators=["0","1","2","3","4","5","6","7"]`

- Add your model's hyperparameters to :code:`hyperparameters_default.json`.

- Commit changes to develop branch.

Running CSA with Parsl
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Clone your model repo:

.. code-block:: bash

  git clone https://github.com/JDACS4C-IMPROVE/<YOUR_MODEL>
  cd <YOUR_MODEL>
  git checkout develop

2. Create Parsl environment:

.. code-block:: bash

  conda create -n parsl parsl numpy pandas scikit-learn pyyaml -y
  conda activate parsl

3. Set up IMPROVE:

.. code-block:: bash

  source setup_improve.sh

4. Run preprocessing using Parsl (if using a config other than :code:`csa_params.ini` you can specific it with :code:`--config_file`):

.. code-block:: bash

  python workflow_csa.py

5. Run full cross study analysis using  (if using a config other than :code:`csa_params.ini` you can specific it with :code:`--config_file`):

.. code-block:: bash

  python workflow_preprocess.py

6. Analyze results:

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



References
------------
`1. <https://dl.acm.org/doi/10.1145/3307681.3325400>`_ Y. Babuji et al. "Parsl: Pervasive Parallel Programming in Python", 28th ACM International Symposium on High-Performance Parallel and Distributed Computing (HPDC), 2019

