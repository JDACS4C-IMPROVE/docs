Installing Ubuntu prerequisites
===============================

The IMPROVE framework relies on Singularity containers. To install singularity on Ubuntu 20.04.3, the following commands were used.

add the NeuroDebian repository to your native package management system, and you will be able to install neuroscience software the same way as any other package.

.. code-block:: bash
   wget -O- http://neuro.debian.net/lists/focal.us-tn.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
   sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9
   sudo apt-get update
   sudo apt-get install singularity-container

These instructions were obatined from http://neuro.debian.net/install_pkg.html?p=singularity-container
