CANDLE Checkpointing in Keras and PyTorch
=========================================

This document provides an overview of the CANDLE checkpointing feature in Keras and PyTorch. Checkpointing is a technique that allows saving and restoring the state of a model during training. This can be useful for resuming interrupted training sessions, performing fault tolerance, or transferring learned weights to other models.
The CANDLE library provides a unified interface for checkpointing in both Keras and PyTorch, as well as some utilities for managing checkpoints. The following examples demonstrate how to use the CANDLE checkpointing feature in Keras and PyTorch.

Examples
--------

Two examples of using CANDLE checkpointing in Keras and PyTorch are provided in the following repository:

https://github.com/ECP-CANDLE/candle_lib/tree/rajeeja/ckpt_examples/docs/examples/checkpointing

The directory structure of the examples is as follows:

.. code-block:: text

    checkpointing
    ├── README.md
    ├── mnist_keras
    │   ├── mnist.py
    │   ├── mnist_baseline_keras.py
    │   └── mnist_default_model.txt
    └── mnist_pytorch
        ├── mnist.py
        ├── mnist_baseline_pytorch.py
        └── mnist_default_model.txt

The README.md file contains a brief description of all the parameters that can be passed to the mnist_default_model.txt file.

The mnist_keras and mnist_pytorch directories contain the scripts and configuration files for training and evaluating a simple convolutional neural network on the MNIST dataset using Keras and PyTorch, respectively.

The mnist_baseline_keras.py and mnist_baseline_pytorch.py script are the main entry point for the example. It parses the command-line arguments, loads the data, creates the model, and calls the train and test functions.

The mnist_default_model.txt files contain the hyperparameters for the model and the training process.

The CANDLE checkpointing feature automatically handles the saving and loading of the model weights, the optimizer state, and the current epoch. It also supports saving multiple checkpoints with different names and deleting old checkpoints to save disk space.