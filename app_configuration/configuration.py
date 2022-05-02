import os, sys
from collections import namedtuple
from app_utils import read_yaml
from app_exception import AppException
from app_logger import log_function_signature
from app_entity.config_entity import DatasetConfig, DataValidationConfig, PreprocessingConfig,\
                                     ModelTrainingConfig, TrainingPipelineConfig

ROOT_DIR = os.getcwd()
CONFIG_FILENAME = "config.yaml"
CONFIG_FILEPATH = os.path.join(ROOT_DIR, CONFIG_FILENAME)

SCHEMA_FILENAME = "dataset_schema.yaml"
SCHEMA_FILEPATH = os.path.join(ROOT_DIR, SCHEMA_FILENAME)

DATASET_KEY = "data_set"
DATASET_NAME_KEY = "name"
SCHEMA_KEY = "schema"
BUFFER_SIZE_KEY = "buffer_size"
BATCH_SIZE_KEY = "batch_size"

