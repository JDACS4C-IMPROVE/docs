Workflow Overview
=================

IMPROVE workflows utilize a clear and consistent three-level script structure designed to integrate seamlessly with high-performance computing (HPC) environments. This structured approach allows IMPROVE to run models efficiently, maintain clear separation of dependencies, and ensure reproducibility.



Overview of the 3-Level Structure
---------------------------------

Every workflow in IMPROVE is organized into three distinct script types:

1. Launcher (Python)

   * Serves as the main entry point for initiating a workflow.
   * Directly interacts with the HPC management framework (e.g., Parsl, DeepHyper).
   * Coordinates high-level workflow tasks, distributing them across available resources.

    Example:

    .. code-block:: bash
        python workflow_csa.py


2. Runner (Bash)

   * Called by the **Launcher** script.
   * Activates the isolated computational environment (e.g., conda, container) specific to the predictive model.
   * Executes the **Stage Scripts** within this isolated environment.

    Example:

    .. code-block:: bash
        bash run_model.sh

3. Stage Script (Python)

   * Performs the actual computational work for the stage (e.g., preprocess, train, infer).
   * Runs within a model-specific isolated environment, free from HPC dependencies.

    Example:

    .. code-block:: bash
        python graphdrp_train_improve.py



Visual Representation
---------------------
The following schematic illustrates the interactions between these scripts:

.. code-block:: text
    Launcher (workflow_csa.py)
    │
    └─→ Runner (run_model.sh)
    │
    └─→ Stage Script (graphdrp_train_improve.py)



Why This Structure?
---------------------

The separation into these three levels ensures:

**Clarity**: Each script type has a clearly defined role.

**Isolation**: Dependencies for models and HPC tools are separated to avoid conflicts.

**Flexibility**: Easily adapts to various HPC environments and tools without modifying the underlying model scripts.



Next Steps
----------

Explore individual workflow guides:

* :doc:Cross-Study Analysis (CSA) <workflows/csa>
* :doc:Learning Curve Analysis (LCA) <workflows/lca>
* :doc:Hyperparameter Optimization (HPO) <workflows/hpo>