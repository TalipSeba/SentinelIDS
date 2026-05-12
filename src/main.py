from logger import write_log
from detector import detect_event
from tracker import track_ip, track_port, is_suspicious, is_port_scan, track_failed_login, is_bruteforce
from traffic_generator import generate_event, generate_login_event
import time


while True:

    level, message = generate_login_event()

    write_log(level, message)

    ip = message.split()[0]
    port = message.split()[-1]

    count = track_ip(ip)
    print(f"{ip} has sent {count} requests")
    port_count = track_port(ip, port)
    failed_count = track_failed_login(ip)

    print(f"{ip} has {failed_count} failed logins")
    print(f"{ip} has tried {port_count} different ports")

    if is_suspicious(ip):
        write_log("WARNING", f"Suspicious IP activity detected from {ip}")
    if is_port_scan(ip):
        write_log("ALERT", f"Port scan behavior detected from {ip}")
    if is_bruteforce(ip):
        write_log("ALERT", f"Brute force attack detected from {ip}")

    detection = detect_event(message)

    if detection:
        alert_level, alert_message = detection
        write_log(alert_level, alert_message)
    time.sleep(1)