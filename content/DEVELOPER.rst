Developer Guide
====================

The improvelib and IMPROVE software stack has been designed with maximum flexibilty to allow for various applications and workflows.

Some key aspects of IMPROVE that allow for workflow integration are:
- Seperate conda environments for each model (reduces conflicts with workflow dependencies)
- Command-line parameter passing (e.g. to subprocess calls)
- Runtime logs (standardize output files for workflow definitions like Snakemake)


.. toctree::
   :titlesonly:

   Creating a Workflow <developer_workflow>
   Creating an Application <developer_application>