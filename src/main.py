from logger import write_log
from detector import detect_event
from tracker import track_ip, track_port, is_suspicious, is_port_scan
from traffic_generator import generate_event


for i in range(10):

    level, message = generate_event()

    write_log(level, message)

    ip = message.split()[0]
    port = message.split()[-1]

    count = track_ip(ip)
    print(f"{ip} has sent {count} requests")
    port_count = track_port(ip, port)
    print(f"{ip} has tried {port_count} different ports")

    if is_suspicious(ip):
        write_log("WARNING", f"Suspicious IP activity detected from {ip}")
    if is_port_scan(ip):
        write_log("ALERT", f"Port scan behavior detected from {ip}")

    detection = detect_event(message)

    if detection:
        alert_level, alert_message = detection
        write_log(alert_level, alert_message)