import sqlite3
from config import DB_PATH

connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attack_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    ip TEXT,
    event_type TEXT,
    threat_score INTEGER

)
""")

connection.commit()


def save_attack(timestamp, ip, event_type, threat_score):

    cursor.execute("""
    INSERT INTO attack_logs
    (timestamp, ip, event_type, threat_score)

    VALUES (?, ?, ?, ?)
    """, (timestamp, ip, event_type, threat_score))

    connection.commit()