from logger import write_log
from detector import parse_event
from tracker import track_ip, track_port, is_suspicious, is_port_scan, track_failed_login, is_bruteforce
from traffic_generator import generate_event, generate_login_event
from threat_score import increase_score, get_score, mark_high_risk
from database import save_attack
from datetime import datetime
import random
import time


while True:

    # Mix normal connection traffic with brute force login attempts
    if random.randint(1, 100) <= 70:
        level, message = generate_event()
    else:
        level, message = generate_login_event()

    timestamp = str(datetime.now())

    write_log(level, message)

    event_kind, ip, port = parse_event(level, message)

    count = track_ip(ip)
    print(f"{ip} has sent {count} requests")

    if event_kind == "CONNECTION":
        port_count = track_port(ip, port)
        print(f"{ip} has tried {port_count} different ports")

    if event_kind == "LOGIN_FAILED":
        failed_count = track_failed_login(ip)
        print(f"{ip} has {failed_count} failed logins")

    if is_suspicious(ip):
        write_log("WARNING", f"Suspicious IP activity detected from {ip}")
        score = increase_score(ip, 5)
        print(f"{ip} threat score = {score}")

    if event_kind == "CONNECTION" and is_port_scan(ip):
        write_log("ALERT", f"Port scan behavior detected from {ip}")
        score = increase_score(ip, 10)
        save_attack(timestamp, ip, "PORT_SCAN", score)
        print(f"{ip} threat score = {score}")

    if event_kind == "LOGIN_FAILED" and is_bruteforce(ip):
        write_log("ALERT", f"Brute force attack detected from {ip}")
        score = increase_score(ip, 20)
        save_attack(timestamp, ip, "BRUTE_FORCE", score)
        print(f"{ip} threat score = {score}")

    if mark_high_risk(ip):
        write_log("CRITICAL", f"High risk attacker detected from {ip}")
        save_attack(timestamp, ip, "HIGH_RISK", get_score(ip))

    time.sleep(1)
