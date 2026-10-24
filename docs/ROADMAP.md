# SentinelIDS Roadmap

## Vision

SentinelIDS will become an easy-to-install, Turkish-language security monitoring system for small organizations (small businesses, schools, municipalities) that do not have a dedicated security team.

Large tools such as Suricata and Wazuh are powerful but need an expert to install and manage. SentinelIDS aims to fill that gap: collect events from several sources, correlate them into attack stories, respond automatically, and report clearly.

## Current State (Day 9)

- Detection rules for brute force and port scan, with a cumulative threat score
- SQLite alert log and Flask dashboard (statistic cards, bar chart, hourly trend)
- 18 automated tests (pytest)
- Data source: simulated traffic only (`traffic_generator.py`), not real network traffic

## Phases

Each phase builds on the previous one. A phase is complete only when it is tested and the results are measured, not just when the code runs.

### Phase 1: Reliable detection engine
- Time windows in detection rules (reduce false positives)
- One alert per attacker per time period (stop alert flooding)
- Score limit and detection state that survives a restart
- Flask debug mode off

### Phase 2: First real data source
- `source` column (`simulated` / `live`) to keep test and real data separate
- Read SSH login failures from system logs (`auth.log` / `journalctl`)
- Decide how `sentinelids.db` is handled in Git

### Phase 3: Live network traffic
- Capture packets from the network interface with Scapy
- Detect port scans from real traffic

### Phase 4: Test lab and measurement
- Isolated VirtualBox host-only network with a separate attacker VM
- Run known attacks (`nmap`, `hydra`) against the lab only
- Measure detection rate and false positive rate with real numbers

### Phase 5: Agents and correlation
- Small agents on each machine send logs (SSH, web server, Windows logons) to a central server
- Correlation engine: link events into one attack chain (for example scan, then brute force, then successful login)
- Rules in YAML files, compatible with the Sigma format where possible
- Map alerts to MITRE ATT&CK techniques

### Phase 6: Response and anomaly detection
- Automatic IP blocking on the firewall
- Notifications (Telegram / e-mail)
- Anomaly detection with machine learning, measured in the lab

### Phase 7: Production quality
- Dashboard login, secure configuration
- One-command installation with Docker
- Turkish interface and incident reports suitable for KVKK
- GitHub Actions running tests on every push
- Complete README, architecture documentation and a demo video

## Principles

- Never present simulated data as real
- Every number on the dashboard is defined and tested
- Small, tested steps; one daily log per day in `docs/development_logs/`
- No secrets or database files in Git
