from datetime import datetime
import os

def write_log(level, message):
    log_message = f"[{datetime.now()}] [{level}] {message}"

    os.makedirs("logs", exist_ok=True)

    with open("logs/system.log", "a") as log_file:
        log_file.write(log_message + "\n")

    print(log_message)