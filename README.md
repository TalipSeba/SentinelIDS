# SentinelIDS

SentinelIDS is a small intrusion detection simulator with a Flask SOC dashboard.

- `src/main.py` generates simulated network and login traffic, tracks each source IP, detects
  suspicious activity, port scans and brute-force attempts, and assigns threat scores. Events are
  written to `logs/system.log` and detected attacks are saved to a SQLite database (`sentinelids.db`).
- `src/dashboard.py` serves a web dashboard that reads that database and shows total attacks, the
  highest threat score, recent attacks, attack type counts, top attacker IPs and a distribution chart.
  It refreshes every 5 seconds.
- `src/view_logs.py` prints the most dangerous IP and its threat score in the terminal.

## Requirements

- Python 3.9+
- Flask (see `requirements.txt`)

## Setup

```bash
git clone https://github.com/TalipSeba/SentinelIDS.git
cd SentinelIDS
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

Run the detector and the dashboard in two separate terminals. Both can be started from any
directory: the `logs/` folder and `sentinelids.db` are always created in the repository root.

Terminal 1, the detection engine (stop with Ctrl+C):

```bash
python src/main.py
```

Terminal 2, the dashboard:

```bash
python src/dashboard.py
```

Then open http://127.0.0.1:5000 in your browser. The dashboard starts empty and fills in as
`main.py` detects attacks.

To print a quick summary in the terminal instead:

```bash
python src/view_logs.py
```

## Project layout

```
src/
  main.py               detection loop
  dashboard.py          Flask dashboard
  view_logs.py          terminal summary
  config.py             repository-relative paths for the database and logs
  database.py           SQLite storage
  logger.py             log file writer
  detector.py, tracker.py, threat_score.py, traffic_generator.py
docs/                   development logs
```

The database and logs are generated at runtime and are not tracked in git.
