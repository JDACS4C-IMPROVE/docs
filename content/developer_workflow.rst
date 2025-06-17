Creating a Workflow
=====================

Identify an appropriate workflow
---------------------------------

Some key aspects of IMPROVE that allow for workflow integration are:

* Seperate conda environments for each model (reduces conflicts with workflow dependencies)
* Command-line parameter passing (e.g. to subprocess calls)
* Runtime logs (standardize output files for workflow definitions like Snakemake)

The modular design of IMPROVE allows for a variety of workflows. To create your own workflow consider:

* Does the workflow require changes to model scripts? These would not be appropriate for an IMPROVE workflow.
* Does the workflow function by altering input benchmark data and/or splits? These types of workflows are great options.
* Does the workflow function by changing any parameters/hyperparameters used by the model? These types of workflows are great options.


Choose an appropriate package, if required
--------------------------------------------
Workflows are kept seperate from the core improvelib to allow the use of packages other than the core improvelib dependencies.

Workflows can be written as a a pure python script (like CSA bruteforce), or use other available tools (like CSA Parsl). 
You may want to consider if another package can provide advantages, such as speed or computational performance.
However, some packages are not easily adaptable to different computational environments, particularly those that interface with MPI, etc.
In this case, we suggest providing multiple implementations, including one in pure python, so that users have options based on their compuational environment.


Creating a new application within improvelib
-----------------------------------------------
Within `improvelib/workflows <https://github.com/JDACS4C-IMPROVE/IMPROVE/tree/develop/workflows>`_, you should create a directory 
for your workflow type (<WORKFLOW>) and a subdirectory for your workflow implementation (<TOOL>). If your workflow requires pre or 
postprocessing scripts that are common for all implementations of the workflow, we recommend they are in an appropriately named directory under <WORKFLOW>.

.. note::

    By convention, we call workflows 'bruteforce' when they are written in pure python with no additional dependencies (other than improvelib dependencies).



Creating a workflow configuration
-----------------------------------------------
To create workflow configuration, you will need to create two files: :code:`<WORKFLOW>_<TOOL>_params_def.py` and :code:`<WORKFLOW>_<TOOL>_params.ini`.

For :code:`<WORKFLOW>_<TOOL>_params_def.py` you can use the template here and see an example here. You will need to:

* Fill in the dictionary with the 'name', 'type', 'default' and 'help' for each parameter.
* We recommend calling this list :code:`additional_definitions`.

.. warning::

    Use :code:`str2bool` as the type for boolean parameters or they will be interpreted as a string. Your file will need to include :code:`from improvelib.utils import str2bool`.

Ensure that the import statement in your workflow script matches the location of the parameter definition file for your workflow and that the name of the parameter definition list matches.

For :code:`<WORKFLOW>_<TOOL>_params.ini` you can use the template here and see an example here. Unlike :doc:`api_config`, all parameters are set under :code:`[<APPLICATION>]` for workflows.
This ini file will serve as a template for users when setting up a workflow.

Creating a workflow script
-----------------------------
Two imports are required for parameter handing with workflows:

* :code:`import <WORKFLOW>_<TOOL>_params_def` with the name you used when setting up the configuration (see above).
* :code:`from improvelib.initializer.config import Config`

To access the parameters, your code should include the following (usually in :code:`main()` or the top of the file):

.. code-block::

    filepath = Path(__file__).resolve().parent
    cfg = Config()
    params = cfg.initialize_parameters(
        section="<APPLICATION>",
        pathToModelDir=filepath,
        default_config="<WORKFLOW>_<TOOL>_params.ini",
        additional_definitions=<WORKFLOW>_<TOOL>_params_def.additional_definitions
        )

Note that if you named your parameter definition list anything other than :code:`additional_definitions`, you will need to change it in :code:`additional_definitions=<WORKFLOW>_<TOOL>_params_def.additional_definitions`.

The parameters can now be accessed by the key in the dictionary like :code:`params['<MY_PARAM>']`.

Document the workflow
----------------------
Workflow readme should contain the following sections:

* Overview 
* Requirements
* Installation and Setup
* Parameter Configuration
* Usage
* Output
