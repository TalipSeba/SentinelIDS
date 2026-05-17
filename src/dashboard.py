from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    connection = sqlite3.connect("sentinelids.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM attack_logs")
    total_attacks = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(threat_score) FROM attack_logs")
    max_score = cursor.fetchone()[0]

    cursor.execute("""
    SELECT ip, MAX(threat_score)
    FROM attack_logs
    """)

    result = cursor.fetchone()

    dangerous_ip = result[0]

    connection.close()

    return f"""
<html>

<head>
    <title>SentinelIDS Dashboard</title>
</head>

<body style="background-color:#0f172a;
             color:white;
             font-family:Arial;
             padding:40px;">

    <h1 style="color:#38bdf8;">
        SentinelIDS Dashboard
    </h1>

    <div style="background:#1e293b;
                padding:20px;
                border-radius:10px;
                width:400px;">

        <h2>System Status: ACTIVE</h2>

        <p>Total Attacks: {total_attacks}</p>

        <p>Highest Threat Score: {max_score}</p>

        <p>Most Dangerous IP: {dangerous_ip}</p>

    </div>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(debug=True)

