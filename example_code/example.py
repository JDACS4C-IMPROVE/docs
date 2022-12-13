import os
import candle
# from candle.file_utils import directory_tree_from_parameters
# from candle.file_utils import get_file
# from candle import Benchmark
# from candle import finalize_parameters

# set CANDLE_DATA_DIR env var. This is normally set externally.
os.environ['CANDLE_DATA_DIR'] = '/tmp/improve_data_dir'

# get the directory of this script, so that the default_model.txt
# file can be found when the benchmark is instanciated.
filepath = os.path.dirname(os.path.abspath(__file__))

imp_bmk = candle.Benchmark(
    filepath=filepath,
    defmodel="example_default_model.txt",
    framework="tensorflow"
)

# Initialize parameters
gParameters = candle.finalize_parameters(imp_bmk)

# Set up input and output directory paths. These will always be
# relative to os.environ['CANDLE_DATA_DIR'].
# data_dir, output_dir = directory_tree_from_parameters(gParameters)
data_dir = gParameters["data_dir"]
output_dir = gParameters["output_dir"]

print('data_dir: {}\noutput_dir: {}'.format(data_dir, output_dir))

# data_dir:   /tmp/improve_data_dir/Example/Data
# putput_dir: /tmp/improve_data_dir/Example/Output/EXP000/RUN000

# Get machine learning data
download_filepath = candle.get_file(
    gParameters['train_data'],
    gParameters['data_url'] + "/" + gParameters['train_data'],
    datadir=data_dir,
    cache_subdir=None
)
print('download_path: {}'.format(download_filepath))
