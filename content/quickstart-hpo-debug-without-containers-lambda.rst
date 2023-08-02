Supervisor without singularity container
==================================

Requirements
____________

Your model must be CANDLE compliant.

+ Conda environment with all the dependencies to run the model
+ Your model script should follow the format: MODEL_NAME_”baseline”_FRAMEWORK.py. This is different from when using a container where train.sh is executed.
+ Model code should contain initialize_parameters() and run(). The workflow will not execute any other functions. So if you have any other function that is needed for your model execution, you may need to put them within either of the two functions. 

Steps 
_____

0. Activate your conda environment.
1. Install deap : pip install deap (may not be necessary)
2. Clone your Model repo – example model directory name: Your_Model
3. Clone Supervisor repo : <https://github.com/ECP-CANDLE/Supervisor.git> Switch to develop branch: ``git checkout develop``. Supervisor directory is at the same level as Your_Model directory.
4. Use the appropriate python for executing Supervisor workflow: Within Supervisor, open: *workflows/common/sh/langs-app-lambda.sh*. Change PY (Python for executing the workflow) to your conda environment. Example content: 

   .. code-block:: bash
        # LANGS APP LAMBDA
        echo "langs-app-lambda ..."
        SFW=/home/woz/Public/sfw
        PY=/lambda_stor/homes/pvasanthakumari/miniconda/envs/paccmann_predictor/ #Path to your conda environment 
        PATH=$PY/bin:$PATH
        echo "langs-app-lambda done."

5. Clone test repo: <git clone https://github.com/ECP-CANDLE/Tests.git>. Switch to General branch: ``git checkout General``
6. Copy Tests/sv-tool/generic inside the Your_Model directory
7. Within Your_model/generic, change content of *cfg-1.sh*. 

   .. code-block:: bash
       source_cfg -v cfg-my-settings.sh
       export MODEL_NAME=your_model_name
       export PYTHONPATH=path to your code in your local directory
       export PARAM_SET_FILE=general_params.json
       export FRAMEWORK="pytorch" #or “keras”

8. Change content of *cfg-my-settings.sh*. Uncomment lines of code for lambda or Polaris (depending on which machine you are using). Specify path for CANDLE_DATA_DIR and CUDA devices.
9. Add Supervisor path

   .. code-block:: bash
         export PATH=~/Supervisor/bin:$PATH

10. When running Supervisor without container, the workflow will look for data within CANDLE_DATA_DIR. You may have to manually download and unzip data into CANDLE_DATA_DIR.
11. To execute the workflow, within Your_Model/generic: 

    .. code-block:: bash
        supervisor lambda GA cfg-1.sh 

12. Output is not written in the candle_data_dir unlike when using container. It is written within supervisor: /Supervisor/workflows/GA/experiments
13. You can also check the workflow output from /generic/turbine-output/out: Use cat out-* 





