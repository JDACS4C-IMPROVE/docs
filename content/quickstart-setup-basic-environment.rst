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

.. code-block:: bash

    conda create --name supervisor_env python=3.9.16
    conda activate supervisor_env
    git clone https://github.com/ECP-CANDLE/Supervisor.git
    cd Supervisor && PATH=$PATH:$(pwd)/bin
    git checkout develop
    conda install --yes -c conda-forge -c swift-t swift-t
    pip install numpy deap


More Information
_____________________
- ECP-CANDLE/Supervisor: https://github.com/ECP-CANDLE/Supervisor
- Swift/T: http://swift-lang.github.io/swift-t/guide.html
