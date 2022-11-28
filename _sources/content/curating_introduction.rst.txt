Introduction to Curating a Community Model
------------------------------------------

A central goal of the IMPROVE framework is the automated execution of community drug response models so that they can be compared to each other under a wide range of conditions.

Three standards needed to automate execution across a collection of models address command line parameters, model hyperparameters, and the return value from a successful training process.

1.  Standard command line parameters are needed so that code that calls to multiple models can be simplified by only knowing one set of command line parameter keywords.

2.  Model hyperparameter keywords then map to the command line parameter keywords you can specify in a (model) file. Generally, each should contain at least a default model file containing the hyperparameter keywords and values from the original publication.

3.  The validation loss is generally the return value of the call to run() or main(). The model weights through the candle library checkpointing. RETURN VALUE DOCUMENTATION.

CANDLE
------
.. toctree::
   :maxdepth: 1

    The CANDLE libraries provide stable interfaces that standardize the interfaces of a set of otherwise heterogenous drug response prediction software.

    How to write CANDLE-compliant deep learning code

    - https://ecp-candle.github.io/Candle/tutorials/writing_candle_code.html

    The candle_lib API documentation

    - https://ecp-candle.github.io/Candle/candle_lib

Examples
--------
.. toctree::
   :maxdepth: 1

    ADRP is a simple fully connected network that trains on drug descriptors using a binding score to a SARS-CoV-2 protein receptor as the label.

    -  https://ecp-candle.github.io/Candle/tutorials/index.html#examples
