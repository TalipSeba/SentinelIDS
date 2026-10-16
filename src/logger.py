from datetime import datetime
from config import LOG_FILE

def write_log(level, message):
    log_message = f"[{datetime.now()}] [{level}] {message}"

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_message + "\n")

    print(log_message)