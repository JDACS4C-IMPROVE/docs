===========================
How to run a container
===========================


General Form:

 .. code-block::
 
  singularity exec –nv –bind $HOST_DATA_DIR:/candle_data_dir $IIL/$IMAGE $CMD $ARGS
 
Use case 1. A custom model  file is provided as an argument to train.sh.


Example:
 
 .. code-block::

  singularity exec --nv --bind /home/brettin/improve_data_dir:/candle_data_dir /software/improve/images/GraphDRP\:0.0.1-20221109.sif train.sh 2 /candle_data_dir GraphDRP/graphdrp_default_model.txt


.. csv-table:: Options
    :align: center
    :widths: auto
    :header-rows: 1

    Parameters, Description
    --nv, This option instructs Singularity to use the host NVidia drivers and cuda libraries.
    --bind, This option instructs Singularity to mount a host file system inside the container. The mount point inside the container will always be candle_data_dir.
    GraphDRP:0.0.1-20221109.sif, This is the Singularity image that contains the GraphDRP model code.
    train.sh, This is the command that runs inside the container. All containers will have this command. All arguments to follow are passed to train.sh.
    2, This is the host GPU device id to be used by code running inside the container. The value is used to set the CUDA_VISIBLE_DEVICES environment variable inside the container.
    candle_data_dir, The value of the CANDLE_DATA_DIR environment variable that is set inside the container. This enables candle_lib code running inside the container to rewrite input and output paths so that inputs and outputs will be saved on the host’s file system.
    GraphDRP/graphdrp_default_model.txt, This is a custom model file created and saved on the host’s filesystem. The location of the file is relative to CANDLE_DATA_DIR



Use Case 2: Train a model with the default model file.

  .. code-block::

    singularity exec --nv --bind /home/brettin/candle_data_dir:/candle_data_dir                   \ /home/brettin/Singularity/sandboxes/GraphDRP-GraphDRP:0.0.1-20221028.   \ train.sh 2 /candle_data_dir
 
Because the number of positional arguments to train.sh is 2, the default model file in the model directory inside the container is used. It still expects /candle_data_dir to be available inside the container as /candle_data_dir is prepended to input and output paths. The default model file would be the one used to closely reproduce the original authors results.
 
Use Case 3: Train a model using supported command line arguments.

In this case, the default model file in the model directory inside the container is read first, and then command line arguments passed to train.sh are used. In the event that both the default model file and the command line arguments contain the same parameter, the command line parameter’s value will take precedence. The first two positional arguments to train.sh must still always be the GPU device id and the mount point inside the container as specified by the –bind option.
 
In this use case, train.sh shifts the two positional arguments $1 and $2 and then simply pass the remaining args in $@ to the model python script.
 
