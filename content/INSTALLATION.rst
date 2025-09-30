Installation
=================================

Requirements
--------------

* Python >= 3.6
* pandas
* numpy >= 1.19.0
* requests
* tqdm
* typing_extensions
* pyyaml
* scikit-learn

Installing improvelib with pip
----------------------------------

.. code-block:: bash

    pip install improvelib


Installing improvelib with git
---------------------------------
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
We currently have benchmark data for :doc:`Drug Response Prediction <app_drp_benchmark>` and :doc:`Synergy <app_synergy_benchmark>`. 

* The DRP data can be downloaded from this `link <https://web.cels.anl.gov/projects/IMPROVE_FTP/candle/public/improve/benchmarks/drp_data_v0.2.0/>`_.

* The Synergy data can be downloaded from this `link <https://web.cels.anl.gov/projects/IMPROVE_FTP/candle/public/improve/benchmarks/synergy_data_v0.2.0/>`_.







Installing conda
_____________________________________

To check if you have conda, use ``conda --version``.

If you do not have conda installed, install with the following commands:

.. code-block:: bash

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh
    source ~/.bashrc

Now, using the ``conda --version`` command should give the version you've downloaded. If not, close the terminal session and open again, then try ``conda --version``.
