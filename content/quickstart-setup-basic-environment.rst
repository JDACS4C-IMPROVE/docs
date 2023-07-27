Installing ECP-CANDLE/Supervisor and Swift/T
=================================

Requirements
______________

- `git <https://github.com>`_
- `conda <https://docs.conda.io/en/latest/>`_
- `singularity <https://apptainer.org>`_


Installing ECP-CANDLE/Supervisor
_____________________

.. code-block:: bash

    conda create --name supervisor_env python=3.9.16
    conda activate supervisor_env
    git clone https://github.com/ECP-CANDLE/Supervisor.git
    cd Supervisor && PATH=$PATH:$(pwd)/bin
    git checkout develop



Installing Swift/T
_____________________

.. code-block:: bash

    conda install --yes -c conda-forge -c swift-t swift-t
    pip install numpy deap

For more information about Swift/T, please see the guide at http://swift-lang.github.io/swift-t/guide.html
