Installing ECP-CANDLE/Supervisor and Swift/T
=================================
This quickstart guide is intended to help you install ECP-CANDLE/Supervisor and Swift/T within a conda environment. 

Requirements
______________

- `git <https://github.com>`_
- `conda <https://docs.conda.io/en/latest/>`_
- `singularity <https://apptainer.org>`_


Installation
_____________________

1. Create a conda environment to install all dependencies.

.. code-block:: bash

    conda create --name IMPROVE python=3.9.16
    conda activate IMPROVE

2. Install **Supervisor** from GitHub and add executables to your search path. 

.. code-block:: bash

    git clone https://github.com/ECP-CANDLE/Supervisor.git
    git checkout develop
    cd Supervisor && PATH=$PATH:$(pwd)/bin
   
3. Install **swift-t** conda package and python modules for *HPO*

.. code-block:: bash

    conda install --yes -c conda-forge -c swift-t swift-t
    pip install numpy deap


More Information
_____________________
- ECP-CANDLE/Supervisor: https://github.com/ECP-CANDLE/Supervisor
- Swift/T: http://swift-lang.github.io/swift-t/guide.html
