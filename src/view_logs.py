import sqlite3

connection = sqlite3.connect("sentinelids.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM attack_logs")

rows = cursor.fetchall()

print("\n=== SentinelIDS Attack Logs ===\n")

for row in rows:
    log_id = row[0]
    timestamp = row[1]
    ip = row[2]
    event_type = row[3]
    threat_score = row[4]

    print(f"ID: {log_id}")
    print(f"Time: {timestamp}")
    print(f"IP Address: {ip}")
    print(f"Event Type: {event_type}")
    print(f"Threat Score: {threat_score}")
    print("-" * 40)

connection.close()