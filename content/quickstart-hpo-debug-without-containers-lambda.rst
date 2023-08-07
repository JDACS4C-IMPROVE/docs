Running a single Model with the Supervisor
==========================================

Packaging the model code in a container image is benefical for ease of deployment  and running multiple models in parallel but it adds an additional layer for debugging the code directly.
Here we describe how to run a single model directly with the supervisor without the need to build a container image first.

Requirements
____________


1. `Install swift-t and Supervisor <quickstart-setup-basic-environment.html>`_
2. Your model must be CANDLE compliant:

    + Add all the dependencies to run your model
    + Your main model script should follow the following naming convention: 
    
        `MODELNAME\_baseline\_FRAMEWORK.py` 


    + Model code should contain **initialize_parameters()** and **run()**. The workflow will not execute any other functions. So if you have any other function that is needed for your model execution, you may need to put them within either of the two functions. 

3. Credentials and access to lambda
4. Model and dependencies will be installed in your home directory.


Steps 
_____

1. Login into your account on lambda
#. Activate your conda environment, e.g. ``conda activate IMPROVE``
#. Clone your Model repo, e.g.  ``git clone ORGANIZATION/MY_MODEL``
#. Set the appropriate python for executing Supervisor workflow. Within Supervisor directory, open:
    
     *workflows/common/sh/langs-app-lambda.sh*. 
     
    Change the value for **PY** (Python for executing the workflow) to the Python version in your conda environment. Example content: 

   .. code-block:: bash

        # LANGS APP LAMBDA
        echo "langs-app-lambda ..."
        SFW=/home/woz/Public/sfw
        PY=`which \`python3\``
        #Path to your conda environment e.g. /lambda_stor/homes/pvasanthakumari/miniconda/envs/paccmann_predictor/  
        PATH=$PY/bin:$PATH
        echo "langs-app-lambda done."

#.  Clone test repo: 

    ``git clone https://github.com/ECP-CANDLE/Tests.git`` 
    
    and switch to **General** branch: 
    
    ``git checkout General``

#.  Copy the generic subdirectory from the Test repository into your model directory, e.g:
    
    ``cp -r Tests/sv-tool/generic MY_MODEL/``
    
#. Within **MY_MODEL**/generic, change the content of *cfg-1.sh* :

   .. code-block:: bash

       source_cfg -v cfg-my-settings.sh
       export MODEL_NAME=MY_MODEL                   
       export PYTHONPATH=$HOME/MY_MODEL             # path to your model code in your local directory
       export PARAM_SET_FILE=general_params.json
       export FRAMEWORK="pytorch"                   # or “keras” see FRAMEWORK part of your file name

#. Change content of *cfg-my-settings.sh*. Uncomment lines of code for lambda or Polaris (depending on which machine you are using). Specify path for **CANDLE_DATA_DIR** and CUDA devices.
#. Make sure the Supervisor scripts are in your `search path <quickstart-setup-basic-environment.html>`_. 
#. When running Supervisor without container, the workflow will look for data within **CANDLE_DATA_DIR**. You may have to manually download and unzip data into **CANDLE_DATA_DIR**.
#. To execute the workflow, within Your_Model/generic: 

    .. code-block:: bash

        supervisor lambda GA cfg-1.sh 

#. You can find outputs in *$HOME/Supervisor/workflows/GA/experiments*
#. You can also check the workflow output from $HOME/MY_MODEL/generic/turbine-output/out:

     ``cat $HOME/MY_MODEL/generic/turbine-output/out-*`` 





