Build and deploy containerized models
=====================================

Requirements
____________

- git
- singularity
- `IMPROVE Singularity repository <https://github.com/JDACS4C-IMPROVE/Singularity>`_
- Path to a directory on a local file system (not shared filesystem, e.g. your home directory is usually on a shared filesystem)
- Build permissions with singularity, e.g. fakeroot  


Installation
____

Build singularity images for IMPROVE models and deploy them to a shared location.

1. Clone the repository into a location of your choice: ::

    git clone https://github.com/JDACS4C-IMPROVE/Singularity.git
    
2. Create your config file: ::

    cd Singularity
    ./setup

3. To customize your setup modify the config in config/improve.env to change the workspace and data directory.

4. Build and deploy:

    a)  deploy image files to default location ./images: ::

            make configure && make deploy
    
    b) If you want to deploy the images at a different location invoke the make command and set PREFIX to a path of your choosing, default is the current directory. The deploy process will create an image directory at the specified location and copy the image files into it. ::

            make configure && make deploy PREFIX=/my/deploy/path/

5. Every container has a standardized script for training a model called *train.sh* and a standard location (*/candle_data_dir*) for model input and output. To train a model you have to make your data directory available inside the container as */candle_data_dir*. ::

            export IMPROVE_DATA_DIR=$HOME/improve_data_dir
            export GPUID=0
            export CONTAINER=images/GraphDRP.sif

            singularity exec --nv --bind ${IMPROVE_DATA_DIR}:/candle_data_dir ${CONTAINER} train.sh ${GPUID} /candle_data_dir
  
With:

    - **IMPROVE_DATA_DIR** path to data directory
    - **CONTAINER** *path/and/name.sif* of image file
    - **GPUID** ID of GPU to use
