Prerequisites HPO
=================

- `git <https://github.com>`_
- `conda <https://docs.conda.io/en/latest/>`_
- `singularity <https://apptainer.org>`_
- `swift-t <https://github.com/swift-lang/swift-t>`_
- `Supervisor <https://github.com/ECP-CANDLE/Supervisor>`_


Installing git and singularity
_____________________________________

Please refer to the documentation of the tools for install instructions.

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


Installing supervisor
_____________________

.. code-block:: bash

    conda create --name IMPROVE python=3.9.16
    conda activate IMPROVE
    git clone https://github.com/ECP-CANDLE/Supervisor.git
    cd Supervisor && export PATH=$PATH:$(pwd)/bin
    git checkout develop
    pip install numpy deap
    



Installing swift-t
_____________________

You need to be in conda environment to proceed. If you aren’t sure: ::
 
    # Same conda env than above
    # conda create --name IMPROVE python=3.9.16
    conda activate IMPROVE

Install swift-t via conda. For detailed instructions please refer to the `swift-t documentation <http://swift-lang.github.io/swift-t/guide.html>`_:

.. code-block:: bash

    conda install --yes -c conda-forge -c swift-t swift-t
    
 
