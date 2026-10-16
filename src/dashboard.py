from flask import Flask
import sqlite3
import database
from config import DB_PATH

app = Flask(__name__)

@app.route("/")
def home():

    connection = sqlite3.connect(DB_PATH)

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

    cursor.execute("""
    SELECT *
    FROM attack_logs
    ORDER BY id DESC
    LIMIT 10
    """)

    recent_attacks = cursor.fetchall()
    cursor.execute("""
    SELECT event_type, COUNT(*)
    FROM attack_logs
    GROUP BY event_type
    """)

    attack_type_counts = cursor.fetchall()
    cursor.execute("""
    SELECT ip, COUNT(*)
    FROM attack_logs
    GROUP BY ip
    ORDER BY COUNT(*) DESC
    LIMIT 5
    """)

    top_attackers = cursor.fetchall()
    chart_labels = [item[0] for item in attack_type_counts]
    chart_values = [item[1] for item in attack_type_counts]
    connection.close()
    return f"""
<html>

<head>
    <title>SentinelIDS Dashboard</title>
    <meta http-equiv="refresh" content="5">
     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

</head>

<body style="background-color:#0f172a;
             color:white;
             font-family:Arial;
             padding:40px;">

    <h1 style="color:#38bdf8;">
        SentinelIDS Dashboard
    </h1>

    <div style="display:flex; gap:20px; margin-top:20px;">

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>System Status</h3>
        <h2 style="color:#22c55e;">ACTIVE</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Total Attacks</h3>
        <h2 style="color:#38bdf8;">{total_attacks}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Highest Threat Score</h3>
        <h2 style="color:#ef4444;">{max_score}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Most Dangerous IP</h3>
        <h2 style="color:#facc15;">{dangerous_ip}</h2>
    </div>

</div>
    <h2 style="margin-top:40px; color:#38bdf8;">
    Recent Attacks
</h2>

<table style="
    width:80%;
    background:#1e293b;
    border-radius:10px;
    padding:10px;
    color:white;
    border-collapse:collapse;
    overflow:hidden;
">

<tr style="border-bottom:1px solid #334155;">
    <th>ID</th>
    <th>IP</th>
    <th>Event</th>
    <th>Threat Score</th>
</tr>

{''.join([
f'''
<tr>
    <td>{attack[0]}</td>
    <td>{attack[2]}</td>
    <td style="color:{
    '#ef4444' if attack[3] == 'HIGH_RISK' else
    '#fb923c' if attack[3] == 'BRUTE_FORCE' else
    '#facc15'
}; font-weight:bold;">
    {attack[3]}
</td>
    <td style="color:{
    '#22c55e' if attack[4] < 50 else
    '#facc15' if attack[4] < 100 else
    '#ef4444'
}; font-weight:bold;">
    {attack[4]}
</td>
</tr>
'''
for attack in recent_attacks
])}

</table>
<h2>Attack Type Counts</h2>

<div style="display:flex; gap:20px; margin-top:20px;">

{''.join([
f'''
<div style="background:#1e293b; padding:20px; border-radius:10px; width:200px;">
    <h3 style="color:{
    '#ef4444' if attack_type[0] == 'HIGH_RISK' else
    '#fb923c' if attack_type[0] == 'BRUTE_FORCE' else
    '#38bdf8'
};">
    {attack_type[0]}
</h3>
    <p>{attack_type[1]}</p>
</div>
'''
for attack_type in attack_type_counts
])}

</div>
<h2 style="margin-top:40px;">
Top Attacker IPs
</h2>

<div style="display:flex; gap:20px; margin-top:20px;">

{''.join([
f'''
<div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
    <h3 style="color:#facc15;">{attacker[0]}</h3>
    <p>{attacker[1]} attacks</p>
</div>
'''
for attacker in top_attackers
])}

</div>
<h2 style="margin-top:40px;">
Attack Distribution Chart
</h2>

<div style="background:#1e293b; padding:20px; border-radius:10px; width:500px; margin-top:20px;">
    <canvas id="attackChart"></canvas>
    <p style="margin-top:20px; color:#94a3b8;">
       Dashboard updates automatically every 5 seconds.
       Attack statistics are generated from live SQLite logs.
    </p>
</div>

<script>
const ctx = document.getElementById('attackChart');

new Chart(ctx, {{
    type: 'pie',
    data: {{
        labels: {chart_labels},
        datasets: [{{
            label: 'Attack Distribution',
            data: {chart_values},
            backgroundColor: [
                '#ef4444',
                '#fb923c',
                '#38bdf8',
                '#22c55e',
                '#facc15'
            ],
            borderWidth: 1
        }}]
    }}
}});
</script>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(debug=True)

