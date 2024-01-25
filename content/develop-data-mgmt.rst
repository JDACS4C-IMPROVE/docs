IMPROVE Data Conventions
===============

This documentation on data management covers the IMPROVE techniques for handling input and output data for single model runs and for workflows via CANDLE/Supervisor. Models must include the arguments ``input_dir`` and ``output_dir``.
All inputs must be loaded from ``input_dir`` and outputs should be stored in a
flat format (e.g. .csv) under ``output_dir``.

File Location Parameters
--------

The user controls on data locations are listed here.

The minimal use case is to set none of these parameters.  In this case, all inputs and outputs will be stored under ``$PWD``.  The settings below modify this behavior.

Hyperparameter ``input_dir``
  The top-level directory for input.  In an IMPROVE model, all input data
  must be placed in this directory.  If unset, defaults to ``$PWD``.

Hyperparameter ``output_dir``
  The top-level directory for output.  In an IMPROVE model,
  all output data must be placed in this directory.
  If unset, defaults to ``input_dir``.

Environment variable ``$IMPROVE_DATA_DIR``
  This assigns to ``input_dir``.

Environment variable ``$IMPROVE_OUTPUT_DIR``
  This assigns to ``output_dir``.

Checkpointing
-------------

Checkpoints are written to ``output_dir/ckpts`` by default, see
the
`ckpt module docs <https://candle-lib.readthedocs.io/en/latest/api_ckpt_utils>`_ .

CANDLE/Supervisor workflows
--------------------

CANDLE/Supervisor expects ``$IMPROVE_DATA_DIR`` and ``$IMPROVE_OUTPUT_DIR``.
Models run within workflows should not set ``output_dir``,
as Supervisor will set this on a per-run basis so that different runs
have different output directories.

Different workflows set ``output_dir`` differently,
see the per-workflow documentation.

candle_lib is responsible for:

* Handling the translation from environment variables to hyperparameters
  specified above.
* Setting defaults as specified above.

This is done in ``candle.finalize_parameters()``.
