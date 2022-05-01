import logging
import os, sys
import yaml
from app_logger.logger import log_function_signature
from app_exception.exception import AppException

@log_function_signature
def read_yaml(yaml_file_path: str) -> dict:
    try:
        logging.info("Reading the config yaml file")
        with open(yaml_file_path, 'rb') as yml:
            config_dict = yaml.safe_load(yml)
            logging.info("Configuration yaml file read successfully")
            return config_dict
    except Exception as e:
        raise AppException(e, sys) from e




