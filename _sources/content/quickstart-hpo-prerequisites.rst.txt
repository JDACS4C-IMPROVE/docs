Prerequisites HPO
=================

- `git <https://github.com>`_
- `conda <https://docs.conda.io/en/latest/>`_
- `singularity <https://apptainer.org>`_
- `swift-t <https://github.com/swift-lang/swift-t>`_
- `Supervisor <https://github.com/ECP-CANDLE/Supervisor>`_


Installing git, conda and singularity
_____________________________________

Please refer to the documentation of the tools for install instructions.

Installing supervisor
_____________________

.. code-block:: bash

    conda create --name supervisor_env python=3.9.16
    conda activate supervisor_env
    git clone https://github.com/ECP-CANDLE/Supervisor.git
    git checkout develop
    pip install numpy deap
    cd Supervisor && PATH=$PATH:$(pwd)/bin



Installing swift-t
_____________________

You need to be in conda environment to proceed. If you aren’t sure: ::
 
    # Same conda env than above
    # conda create --name supervisor_env python=3.9.16
    conda activate supervisor_env

Install swift-t via conda. For detailed instructions please refer to the `swift-t documentation <http://swift-lang.github.io/swift-t/guide.html>`_:

.. code-block:: bash

    conda install --yes -c conda-forge -c swift-t swift-t
    
 