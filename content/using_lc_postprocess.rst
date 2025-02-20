Postprocessing of Learning Curve Analysis (LCA)
======================================================

This script produces aggregated LCA scores, run times, and plots LCA mean absolute error curves when given the output directory from any of the IMPROVE LCA workflows (bruteforce, swarm).

Requirements
---------------

* :doc:`IMPROVE general environment <INSTALLATION>`
* seaborn (for plotting only)
* matplotlib (for plotting only)
* a directory containing LCA output

Installation and Setup
-----------------------

Create the IMPROVE general environment:

.. code-block:: bash

    conda create -n IMPROVE python=3.6
    conda activate IMPROVE
    pip install improvelib


If you wish to use the included plotting functionality, install seaborn and matplotlib:

.. code-block:: bash

    conda install seaborn matplotlib


Parameter Configuration
------------------------

This workflow uses command line parameters. The first (positional) parameter (:code:`runtimes`, :code:`lca_scores`, :code:`plot_learning_curve`, or :code:`whole_analysis`) specifies the analysis to run. Other optional parameters are as follows:

* :code:`--input_dir`: Path to the LCA results (default: :code:`'./'`).
* :code:`--output_dir`: Path to the directory where the postprocessing will be saved (default: :code:`'./'`).
* :code:`--y_col_name`: The y_col_name in :code:`test_y_data_predicted.csv` (default: :code:`'auc'`).
* :code:`--metric_type`: Metric type to use (default: :code:`'regression'`).
* :code:`--model_name`: Name of the model, if you would like it saved in the file name / data / title of the plot (default: :code:`None`).
* :code:`--dataset`: Name of the dataset, if you would like it saved in the file name / data / title of the plot (default: :code:`None`).


Usage
---------

To generate run-time analysis:

.. code-block:: bash

    python lca_postprocess.py runtimes <arguments>

This will output a table :code:`runtimes.csv` in the specified :code:`output_dir`.

To generate aggregate scores:

.. code-block:: bash

    python lca_postprocess.py lca_scores <arguments>

This will output a table :code:`all_scores.csv` in the specified :code:`output_dir`.

To generate learning curve plot:

.. code-block:: bash

    python lca_postprocess.py plot_learning_curve <arguments>

This will use :code:`all_scores.csv` the specified :code:`output_dir` and output a plot :code:`fig.png` in the specified :code:`output_dir`.

To run all analyses:

.. code-block:: bash

    python lca_postprocess.py whole_analysis <arguments>

This will run the run-time analysis, aggregate scores, and plot the learning curve.


Output
---------

The processed results will be in :code:`output_dir` as follows:

.. code-block:: bash

    output_dir/
    ├── <model>_<dataset>_all_scores.csv
    ├── <model>_<dataset>_fig.png
    └── <model>_<dataset>_runtimes.csv


