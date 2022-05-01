import logging
import os
from datetime import datetime
import uuid

EXPERIMENT_ID = str(uuid.uuid4())
CURRENT_TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')
FILENAME = f"log_{CURRENT_TIMESTAMP}.log"

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR, FILENAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format='[%(asctime)s] - %(name) - %(level) - %(message)',
                    level=logging.INFO)


def log_function_signature(func):
    def inner(*args, **kwargs):
        kw_args_text = ""
        for param_name, param_value in kwargs.items():
            kw_args_text = f"{kw_args_text},{param_name} = {param_value}"
        arg_text = list(args)
        arg_text = ",".join(map(str, arg_text))
        logging.info(f"Entering {func.__name__}({arg_text}{kw_args_text})")
        response = func(*args, **kwargs)
        logging.info(f"Exiting {func.__name__}({arg_text}{kw_args_text})")
        return response

    return inner


def print_text(text):
    print(text)


if __name__ == "__maim__":
    print_text(Diwanshu)
