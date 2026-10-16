import sqlite3
import database
from config import DB_PATH

connection = sqlite3.connect(DB_PATH)

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