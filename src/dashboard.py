from flask import Flask
import json
import sqlite3

app = Flask(__name__)

ATTACK_COLORS = {
    "BRUTE_FORCE": "#fb923c",
    "PORT_SCAN": "#facc15",
}

def get_stats():

    connection = sqlite3.connect("sentinelids.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM attack_logs")
    total_attacks = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(MAX(threat_score), 0) FROM attack_logs")
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
    WHERE event_type != 'HIGH_RISK'
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

    cursor.execute("""
    SELECT substr(timestamp, 1, 13) AS hour, COUNT(*)
    FROM attack_logs
    WHERE event_type != 'HIGH_RISK'
    GROUP BY hour
    ORDER BY hour
    """)
    hourly_trend = cursor.fetchall()

    cursor.execute("SELECT COUNT(DISTINCT ip) FROM attack_logs")
    unique_ips = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM attack_logs WHERE event_type = 'BRUTE_FORCE'")
    brute_force_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM attack_logs WHERE event_type = 'PORT_SCAN'")
    port_scan_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT ip) FROM attack_logs WHERE event_type = 'HIGH_RISK'")
    high_risk_ips = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(timestamp) FROM attack_logs")
    last_seen = cursor.fetchone()[0]

    connection.close()

    return {
        "total_attacks": total_attacks,
        "max_score": max_score,
        "dangerous_ip": dangerous_ip,
        "recent_attacks": recent_attacks,
        "attack_type_counts": attack_type_counts,
        "top_attackers": top_attackers,
        "hourly_trend": hourly_trend,
        "last_seen": last_seen,
        "unique_ips": unique_ips,
        "brute_force_count": brute_force_count,
        "port_scan_count": port_scan_count,
        "high_risk_ips": high_risk_ips,
    }


@app.route("/")
def home():

    stats = get_stats()

    total_attacks = stats["total_attacks"]
    max_score = stats["max_score"]
    dangerous_ip = stats["dangerous_ip"]
    recent_attacks = stats["recent_attacks"]
    attack_type_counts = stats["attack_type_counts"]
    top_attackers = stats["top_attackers"]
    unique_ips = stats["unique_ips"]
    brute_force_count = stats["brute_force_count"]
    port_scan_count = stats["port_scan_count"]
    high_risk_ips = stats["high_risk_ips"]
    last_seen = stats["last_seen"]

    type_counts = dict(attack_type_counts)
    chart_labels = list(ATTACK_COLORS)
    chart_values = [type_counts.get(label, 0) for label in chart_labels]
    chart_colors = [ATTACK_COLORS.get(label, "#38bdf8") for label in chart_labels]
    hourly_trend = stats["hourly_trend"]
    trend_labels = [row[0] + ":00" for row in hourly_trend]
    trend_values = [row[1] for row in hourly_trend]
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

    <p style="color:#94a3b8;">
        Data source: simulated test traffic (traffic_generator.py). This is not real network traffic.
    </p>

    <div style="display:flex; gap:20px; margin-top:20px;">

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Last Record</h3>
        <h2 style="color:#22c55e; font-size:20px;">{last_seen[:19] if last_seen else "-"}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Total Alerts</h3>
        <h2 style="color:#38bdf8;">{total_attacks}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Highest Threat Score</h3>
        <h2 style="color:#ef4444;">{max_score}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Most Dangerous IP</h3>
        <h2 style="color:#facc15;">{dangerous_ip or "-"}</h2>
    </div>
</div>

    <div style="display:flex; gap:20px; margin-top:20px;">

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Unique Source IPs</h3>
        <h2 style="color:#38bdf8;">{unique_ips}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Brute Force Alerts</h3>
        <h2 style="color:#fb923c;">{brute_force_count}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>Port Scan Alerts</h3>
        <h2 style="color:#facc15;">{port_scan_count}</h2>
    </div>

    <div style="background:#1e293b; padding:20px; border-radius:10px; width:250px;">
        <h3>High Risk IPs</h3>
        <h2 style="color:#ef4444;">{high_risk_ips}</h2>
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
    <th>Time</th>
    <th>IP</th>
    <th>Event</th>
    <th>Threat Score</th>
</tr>

{''.join([
f'''
<tr>
    <td>{attack[0]}</td>
    <td>{attack[1][:19]}</td>
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
    <h3 style="color:{ATTACK_COLORS.get(attack_type[0], '#38bdf8')};">
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
    <p>{attacker[1]} alerts</p>
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
       Statistics are read from the SQLite alert log (sentinelids.db).
    </p>
</div>

<h2 style="margin-top:40px;">
Hourly Alert Trend
</h2>

<div style="background:#1e293b; padding:20px; border-radius:10px; width:500px; margin-top:20px;">
    <canvas id="trendChart"></canvas>
    <p style="margin-top:20px; color:#94a3b8;">
       Brute force and port scan alerts per hour (HIGH_RISK not counted).
    </p>
</div>

<script>
const ctx = document.getElementById('attackChart');

new Chart(ctx, {{
    type: 'bar',
    data: {{
        labels: {json.dumps(chart_labels)},
        datasets: [{{
            label: 'Alerts',
            data: {json.dumps(chart_values)},
            backgroundColor: {json.dumps(chart_colors)},
            borderWidth: 1
        }}]
    }},
    options: {{
        plugins: {{
            legend: {{ display: false }}
        }},
        scales: {{
            y: {{
                beginAtZero: true,
                ticks: {{ precision: 0 }}
            }}
        }}
    }}
}});

new Chart(document.getElementById('trendChart'), {{
    type: 'line',
    data: {{
        labels: {json.dumps(trend_labels)},
        datasets: [{{
            label: 'Alerts per hour',
            data: {json.dumps(trend_values)},
            borderColor: '#38bdf8',
            backgroundColor: '#38bdf8',
            pointRadius: 5
        }}]
    }},
    options: {{
        plugins: {{
            legend: {{ display: false }}
        }},
        scales: {{
            y: {{
                beginAtZero: true,
                ticks: {{ precision: 0 }}
            }}
        }}
    }}
}});
</script>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(debug=True)

