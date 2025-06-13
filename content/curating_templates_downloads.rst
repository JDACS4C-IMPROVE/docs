Download Files Template
================================

All models should have :code:`setup_improve.sh` and :code:`download_csa.sh` present in the repository. If your model uses supplemental data, this 
should also be downloaded via shell script and included in :code:`setup_improve.sh` (see below).

Template for :code:`setup_improve.sh`
----------------------------------------

.. code-block:: bash

    #!/bin/bash --login
    # Navigate to the dir with the cloned model repo
    # Run it like this: source ./setup_improve.sh

    # set -e

    # Get current dir and model dir
    model_path=$PWD
    echo "Model path: $model_path"
    model_name=$(echo "$model_path" | awk -F '/' '{print $NF}')
    echo "Model name: $model_name"

    # Download data (if needed)
    data_dir="csa_data"
    if [ ! -d $PWD/$data_dir/ ]; then
        echo "Download CSA data"
        source download_csa.sh
    else
        echo "CSA data folder already exists"
    fi

    # # Download author data (if needed) - PathDSP specific
    # author_dir="author_data"
    # if [ ! -d $PWD/$author_dir/ ]; then
    #     echo "Download author data"
    #     mkdir author_data
    #     source download_author_data.sh author_data/
    # else
    #     echo "Author data folder already exists"
    # fi

    # Env var IMPROVE_DATA_DIR
    export IMPROVE_DATA_DIR="./$data_dir/"

    # Env var AUTHOR_DATA_DIR - PathDSP specific
    export AUTHOR_DATA_DIR="./$author_dir/"

    # Clone IMPROVE lib (if needed) and checkout the branch/tag
    cd ../
    improve_lib_path=$PWD/IMPROVE
    # improve_branch="develop"
    improve_branch="v0.1.0-2024-09-27"
    if [ -d $improve_lib_path ]; then
        echo "IMPROVE repo exists in ${improve_lib_path}"
    else
        git clone https://github.com/JDACS4C-IMPROVE/IMPROVE
    fi
    cd IMPROVE
    git checkout -f $improve_branch 
    cd ../$model_name

    # Env var PYTHOPATH
    export PYTHONPATH=$PYTHONPATH:$improve_lib_path

    echo
    echo "IMPROVE_DATA_DIR: $IMPROVE_DATA_DIR"
    echo "AUTHOR_DATA_DIR: $AUTHOR_DATA_DIR"
    echo "PYTHONPATH: $PYTHONPATH"



Template for :code:`download_csa.sh`
------------------------------------

This should not require any changes and can be used as is.

.. code-block:: bash

    wget --cut-dirs=8 -P ./ -nH -np -m https://web.cels.anl.gov/projects/IMPROVE_FTP/candle/public/improve/benchmarks/single_drug_drp/benchmark-data-pilot1/csa_data/


Template for supplemental data download
--------------------------------------------

This should be used only if required by your model. Modify as appropriate for your model.

.. code-block:: bash

    #!/bin/bash

    # arg 1: output directory to download model-specific data

    OUTPUT_DIR=$1

    # Check if the data is already downloaded
    if [ -f "$OUTPUT_DIR/.downloaded" ]; then 
    echo "Data present, skipping download"
    # Download data if no other download is in progress
    elif [ ! -f "$OUTPUT_DIR/.downloading_author_data" ]; then
    touch "$OUTPUT_DIR/.downloading_author_data"
    # Download files
    # Unzip files (if needed)
    wget -P $OUTPUT_DIR <path/to/the/file>
    unzip -d $OUTPUT_DIR $OUTPUT_DIR/<file>.zip 
    touch "$OUTPUT_DIR/.downloaded"
    rm "$OUTPUT_DIR/.downloading_author_data"
    else
    # Wait for other download to finish
    iteration=0
    echo "Waiting for external download"
    while [ -f "$OUTPUT_DIR/.downloading_author_data" ]; do
        iteration=$((iteration + 1))
        if [ "$iteration" -gt 10 ]; then
        # Download takes too long, exit and warn user
        echo "Check output directory, download still in progress after $iteration minutes."
        exit 1
        fi
        sleep 60
    done
    fi




Also uncomment and modify this section in :code:`setup_improve.sh`:

.. code-block:: bash

    # Download author data (if needed) - PathDSP specific
    author_dir="author_data"
    if [ ! -d $PWD/$author_dir/ ]; then
        echo "Download author data"
        mkdir author_data
        source download_author_data.sh author_data/
    else
        echo "Author data folder already exists"
    fi