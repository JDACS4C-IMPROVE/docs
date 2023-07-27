Installing Supervisor and Swift-t 
=================================

Requirements
------------

- `git <https://github.com>`_
- `conda <https://docs.conda.io/en/latest/>`_
- `singularity <https://apptainer.org>`_


Installing supervisor
_____________________

.. code-block:: bash

    conda create --name supervisor_env python=3.9.16
    conda activate supervisor_env
    git clone https://github.com/ECP-CANDLE/Supervisor.git
    git checkout develop
    cd Supervisor && PATH=$PATH:$(pwd)/bin



Installing swift-t
_____________________

For detailed instructions please refer to swift-t documenation at http://swift-lang.github.io/swift-t/guide.html

.. code-block:: bash

    # conda create --name supervisor_env python=3.9.16
    conda activate supervisor_env
    conda install --yes -c conda-forge -c swift-t swift-t
    pip install numpy deap
 