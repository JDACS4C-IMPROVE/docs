Hyper Parameter Optimization (HPO)
==================================

Requirements
____________

- Supervisor code
- Model 
    - containerized
    - candle interface
    - improve interface 


*swift-t and Supervisor*

> 1. ``git clone https://github.com/ECP-CANDLE/Supervisor.git``
2. ``conda install``
3. Add path to supervisor to your environment: ``cd Supervisor && PATH = $PATH:$(pwd)/bin``

*IMPROVE Models*

Your model is packaged in a singularity image. You can identify the image file by the ``*.sif*`` suffix. The container exposes following interface scripts:
+ preprocess.sh
+ train.sh
+ infer.sh

Steps
_____

. Create config files
. ``supervisor *location* *workflow* *config*``

Running an HPO experiment on lambda. The model image is in /software/improve/images/.

- location = lambda
- workflow = GA


