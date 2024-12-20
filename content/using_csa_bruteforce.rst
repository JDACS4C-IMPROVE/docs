Brute Force Cross-Study Analysis
==================================
NATASHA: in progress, updating as scripts are updated.

The concept behind Cross-Study Analysis (CSA) is detailed :doc:`here <using_csa>`. 
The brute force method uses a script to loop through the relevant datasets and splits to execute the Cross-Study Analysis.

Setting up CSA with the Brute Force method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are setting up CSA with the Brute Force method for the first time with your model:

- Copy the scripts from `here <>`_ to your model repo.

- Change :code:`<MODEL_NAME>` to your model name (e.g. :code:`graphdrp`).

- ADD OTHER CONFIG

- Commit changes to develop branch.

Running CSA with the Brute Force method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Clone your model repo:

.. code-block:: bash

  git clone https://github.com/JDACS4C-IMPROVE/<YOUR_MODEL>
  cd <YOUR_MODEL>
  git checkout develop

2. Set up and activate your model environment.

3. Set up IMPROVE:

.. code-block:: bash

  source setup_improve.sh

4. Run CSA

.. code-block:: bash

    python csa_bruteforce_wf.py

5. Script for scores
