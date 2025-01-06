Installation
=================================

Installing improvelib with pip
------------
Coming soon


Installing improvelib with git
----------
Clone the IMPROVE repository to a directory of your preference (outside of your drug response prediction (DRP) model's directory).

.. code-block:: bash

    git clone https://github.com/JDACS4C-IMPROVE/IMPROVE
    cd IMPROVE
    git checkout develop


.. note::

    You can :code:`git checkout` older versions of IMPROVE if needed. See :doc:`here <ReleaseNotes>` for details on older versions.

To use improvelib, specify the full path to the IMPROVE library with $PYTHONPATH.

.. code-block:: bash

    export PYTHONPATH=$PYTHONPATH:/your/path/to/IMPROVE



Downloading IMPROVE benchmark datasets
-------------------------------------------
We currently have benchmark data for Drug Response Prediction. This data can be downloaded from this `link <https://web.cels.anl.gov/projects/IMPROVE_FTP/candle/public/improve/benchmarks/single_drug_drp/benchmark-data-pilot1/>`_ 
or to a specified definition with the following:

.. code-block:: bash

    ./scripts/get-benchmarks $DESTINATION/csa_data/raw_data

