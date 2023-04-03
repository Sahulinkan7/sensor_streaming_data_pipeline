import logging
from datetime import datetime


import os

LOG_DIR="kafka_logs"
log_file_name=f"log_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

os.makedirs(LOG_DIR,exist_ok=True)

log_file_path=os.path.join(LOG_DIR,log_file_name)

logging.basicConfig(filename=log_file_path,filemode="w",level=logging.INFO,
                    format="[%(asctime)s,%(lineno)s,%(levelname)s,%(filename)s,%(message)s]")