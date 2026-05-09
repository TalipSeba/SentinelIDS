from logger import write_log
from detector import detect_event

events = [
    ("INFO", "192.168.1.10 connected to port 80"),

    ("INFO", "192.168.1.15 connected to port 443"),

    ("WARNING", "192.168.1.20 tried multiple ports"),

    ("INFO", "192.168.1.30 connected to port 22")
]

for level, message in events:

    write_log(level, message)

    detection = detect_event(message)

    if detection:
        alert_level, alert_message = detection
        write_log(alert_level, alert_message)
