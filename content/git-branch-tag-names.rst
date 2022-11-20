===========================
GitHub branch and tag names and definitions
===========================

Github Branch and Tag Definitions

Branches:

main, master - The branch representing the original forked code.

improve - This is the improve release branch. Only the release engineer(s) will have write permissions on this branch.

develop - This is the branch that improve developers work on.

Tags

Release tags will be used to mark releases, which will be on the improve branch. Releases tags follow the v0.0.0 nomenclature.

An optional annotated tag can be added to the model on the develop branch when the code is determined to be reproducing the original results (within reasonable limits). For consistency sake, we are recommending that the tag name be "validated". Hence a command to tag the develop branch when it is believed that we have reproduced the results is

.. code-block::
 
  git tag -a valiated
  
The -a will cause git to prompt you for annotation, which would be something like "The author reported an MSE of 1.141 and we obtrained an MSE of 1.145". Of course the specific message (annotation) will be model specific, and the tag name will be "validated".
