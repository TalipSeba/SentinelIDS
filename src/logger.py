from datetime import datetime

def write_log(level, message):
    log_message = f"[{datetime.now()}] [{level}] {message}"

    with open("logs/system.log", "a") as log_file:
        log_file.write(log_message + "\n")

    print(log_message)