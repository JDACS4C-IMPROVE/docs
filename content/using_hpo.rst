Hyper Parameter Optimization (HPO)
==================================

Hyperparameters are pre-specified parameters in deep learning models that control the learning process. 
Examples of commonly fine-tuned hyperparameters include learning rate, batch size, dropout, or number of layers.
The values of these hyperparamers are fixed before training begins, but these hyperparameters can affect performance of the model.
Hyper Parameter Optimization (HPO) determines which hyperparameters produce the best model for a given dataset by minimizing validation loss. 
Common techniques for HPO include the more computationally intensive Grid Search and Random Search, as well as newer, more efficient methods such as Bayesian Optimization and Genetic Algorithms.
We have two workflows for HPO: :doc:`Supervisor HPO <using_hpo_supervisor>` (based on Genetic Algorithms) and :doc:`DeepHyper HPO <using_hpo_deephyper>` (based on Bayesian Optimization).

Workflow
------------


Metrics
------------
HPO workflows report the validation loss (usually MSE) for each set of hyperparameters tested.


.. toctree::
   :titlesonly:

   Supervisor HPO <using_hpo_supervisor>
   DeepHyper HPO <using_hpo_deephyper>
 