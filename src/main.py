from logger import write_log
from detector import detect_event
from tracker import track_ip, is_suspicious

events = [

    ("INFO", "192.168.1.20 connected to port 80"),

    ("INFO", "192.168.1.20 connected to port 443"),

    ("WARNING", "192.168.1.20 tried multiple ports"),

    ("INFO", "192.168.1.30 connected to port 22"),

    ("INFO", "192.168.1.20 connected to port 21"),

    ("INFO", "192.168.1.30 connected to port 25")
]

for level, message in events:

    write_log(level, message)

    ip = message.split()[0]

    count = track_ip(ip)

    print(f"{ip} has sent {count} requests")
    
    if is_suspicious(ip):
     write_log("WARNING", f"Suspicious IP activity detected from {ip}")

    detection = detect_event(message)

    if detection:
        alert_level, alert_message = detection
        write_log(alert_level, alert_message)