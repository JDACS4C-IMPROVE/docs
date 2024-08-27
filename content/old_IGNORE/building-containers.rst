How to build a container
========================

Taken from:

https://github.com/JDACS4C-IMPROVE/Singularity/blob/master/README.building_container.md

Using bootstrap.sh
-----------------------------

.. code-block::

  Options:
    -n: Required. Name for the image
    -d: Path to Singularity definition file. Builds an image from specified definition
    -f: Build a base image for a framework. Acceptable values are: 'pytorch', 'tensorflow'.
        If -d option is specified, then -f is ignored.
    -t: Tag for Singularity definition file. Active only for -d option. Default value is 0.0.1
    -h: Help

Environmental variables are specified in a file ../config/improve.env

Runtime variables are specified in a file ../config/run.config


Building from definition file
-----------------------------

In order to build a container from a definition file, you have to write that definintion file. There are definition files in the definitions directory of the Singularity repository. Your definition file can start by using a pre-built improve image that has tensorflow or pytorch already installed along with candle_lib, or your definition file can start by using a deep learning docker image from dockerhub such as tensorflow/tensorflow:latest-gpu.

Definition files for images should be committed to the definitions directory of the Singularity repository.

Custom containers can be built using the bootstrap.sh command, for example:

.. code-block::

  ./bootstrap.sh -d ../definitions/GraphDRP.def -n GraphDRP


When bootstrap.sh is done running with no errors, you will be automatically logged into the sandbox. The following is an iterative process that likely requires rebuilding the container several times as the definition file is updated.

1.  Install dependencies and update definition file until the model is running.

2.  From within the container, demonstrate that the train.sh runs the community model. In this case, CANDLE_DATA_DIR can be any path within the container. See: https://github.com/JDACS4C-IMPROVE/Singularity/blob/master/src/templates/train.sh

.. code-block::

  CUDA_VISIBLE_DEVICES=0
  CANDLE_DATA_DIR=/candle_data_dir
  CANDLE_CONFIG=/usr/local/GraphDRP/graphdrp_default_model.txt
  
  train.sh $CUDA_VISIBLE_DEVICES $CANDLE_DATA_DIR $CANDLE_CONFIG


3.  Denonstrate that train.sh can be invoked from outside the container. These variables are set outside the container and passed in. NOTE: the path that is assigned to CANDLE_CONFIG is relative to CANDLE_DATA_DIR.

.. code-block::

  CUDA_VISIBLE_DEVICES=0
  CANDLE_DATA_DIR=/path/to/host/data_dir
  CANDLE_CONFIG=uno_default_model.txt
  
  singularity exec --nv --bind $CANDLE_DATA_DIR:/candle_data_dir <image or sandbox path/name> train.sh $CUDA_VISIBLE_DEVICES $CANDLE_DATA_DIR $CANDLE_CONFIG

In the above example, the model config file would exist in /path/to/host/data_dir/uno_default_model.txt on the host. Thus, the CANDLE_CONFIG is relative to CANDLE_DATA_DIR. You run train.sh from outside the container by invoking singularity:

4. Build a non-writable image from the sandbox and run train.sh

.. code-block::

  TODO: Document this

