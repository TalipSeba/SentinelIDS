import sqlite3

connection = sqlite3.connect("sentinelids.db")

cursor = connection.cursor()

cursor.execute("""
SELECT ip, MAX(threat_score)
FROM attack_logs
""")

rows = cursor.fetchall()

print("\n=== SentinelIDS Attack Logs ===\n")

dangerous_ip = rows[0][0]
max_score = rows[0][1]

print(f"\nMost Dangerous IP: {dangerous_ip}")
print(f"Highest Threat Score: {max_score}\n")

connection.close()