import logging
from datetime import datetime
import os


HOUSING_LOG_DIR = "HousingLog"

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(HOUSING_LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(HOUSING_LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename= LOG_FILE_PATH,
                    filemode="w",
                    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
                    level = logging.INFO
                    )