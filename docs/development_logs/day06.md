# Day 6 — SQLite Database Logging and Attack History System

# What We Built

Today we upgraded SentinelIDS with a database logging and attack history system.

We built:
- SQLite database integration
- Attack log database system
- Automatic database logging
- Attack history viewer
- Structured attack storage
- Database-based event analysis
- Attack history monitoring

---

# Project Structure Update

Created new files:
- database.py
- view_logs.py
- sentinelids.db

Updated files:
- main.py
- database.py
- view_logs.py

---

# What I Learned

Today I learned:
- SQLite database systems
- SQL basics
- CREATE TABLE queries
- INSERT INTO queries
- SELECT queries
- Database logging systems
- Attack history storage
- Python sqlite3 module usage

---

# Database System

We integrated SQLite into SentinelIDS.

Purpose:
To permanently store detected attacks and security events.

Previously:
Events only appeared in terminal output.

Now:
Detected attacks are automatically stored inside a database.

Database file:

sentinelids.db

---

# Attack Logs Table

We created a database table named:

attack_logs

Stored fields:
- id
- timestamp
- ip
- event_type
- threat_score

This structure allows SentinelIDS to keep attack history records.

---

# Automatic Database Logging

We created the function:

save_attack()

Purpose:
To automatically save detected attacks into the database.

Current stored attack types:
- BRUTE_FORCE
- PORT_SCAN
- HIGH_RISK

Example database entry:

ID: 1
IP: 192.168.1.200
Event Type: BRUTE_FORCE
Threat Score: 30

---

# Attack History Viewer

We created:

view_logs.py

Purpose:
To read attack history from the database.

The system now displays:
- attack ID
- timestamp
- attacker IP
- event type
- threat score

This simulates real SIEM attack history systems.

---

# Why This Is Important

Real security systems store all attack events inside databases.

This allows:
- historical analysis
- incident investigation
- attack statistics
- forensic analysis
- dashboard integration
- AI training data collection

Today SentinelIDS moved from temporary logging
to permanent attack storage.

---

# Code Logic

Current system flow:

generate attack
→ analyze behavior
→ calculate threat score
→ detect attacks
→ generate alerts
→ save to database
→ store attack history
→ display attack history

---

# Cybersecurity Concept

Today I learned how SIEM systems store attack history.

Modern security systems:
- collect events
- store logs in databases
- analyze historical attacks
- investigate incidents
- track attacker behavior over time

Today SentinelIDS implemented its first attack history database system.

---

# Problems Faced

## 1. datetime import problem

Error:

NameError: datetime is not defined

Cause:
datetime module was not imported inside main.py.

Solution:
Added:

from datetime import datetime

This fixed timestamp generation.

---

## 2. Raw tuple output problem

Initially:
Database records appeared as raw tuples.

Example:

(1, timestamp, ip, event_type, score)

Solution:
Created formatted attack history output using:
- f-strings
- structured printing
- readable layout

---

# Next Goals

Next steps:
- Advanced SQL queries
- Attack filtering
- Attack statistics
- Dashboard development
- Flask web interface
- Live attack monitoring panel
- Graph systems
- AI anomaly analysis