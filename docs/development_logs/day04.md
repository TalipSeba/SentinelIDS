# Day 4 — Real-Time Monitoring and Brute Force Detection

# What We Built

Today we upgraded SentinelIDS into a real-time monitoring system.

We built:
- A real-time IDS monitoring loop
- Continuous traffic analysis
- Login attack simulation
- Failed login tracking
- Brute-force attack detection
- Real-time alert generation
- Continuous monitoring behavior

---

# Project Structure Update

Updated files:
- main.py
- tracker.py
- traffic_generator.py

---

# What I Learned

Today I learned:
- Infinite loops in Python
- Real-time monitoring logic
- time.sleep() usage
- Login attack simulation
- Failed login tracking
- Brute-force detection logic
- Security event correlation
- Continuous IDS behavior

---

# Real-Time Monitoring System

We converted SentinelIDS from a static script into a continuously running monitoring engine.

Previously:
The system generated only limited events and stopped.

Now:
The system continuously:
- generates events
- analyzes behavior
- detects attacks
- creates alerts
- writes logs

The IDS now behaves like a real monitoring system.

---

# Real-Time Loop

We replaced:

for i in range(10):

with:

while True:

This allows the system to run continuously.

We also added:

time.sleep(1)

This creates a delay between events and simulates realistic traffic timing.

---

# Login Attack Simulation

We created a new login attack generator.

The system now generates events such as:

[LOGIN_FAILED] 192.168.1.200 failed login with username=admin password=123456

This simulates brute-force login attacks.

The attacker repeatedly tries:
- different usernames
- different passwords

This behavior is common in real cyber attacks.

---

# Failed Login Tracking

We added a failed login tracking system.

Purpose:
To count how many failed logins each IP address performs.

Example:

192.168.1.200 → 5 failed logins

This allows SentinelIDS to detect brute-force attacks.

---

# Brute Force Detection

We added a new detection rule.

Current rule:
If an IP address performs 5 or more failed login attempts,
the system generates an ALERT.

Example:

[ALERT] Brute force attack detected from 192.168.1.200

This simulates real login attack detection systems.

---

# Why This Is Important

Real attackers commonly use brute-force attacks to:
- guess passwords
- gain unauthorized access
- compromise accounts

Real IDS and SIEM systems monitor:
- repeated failed logins
- suspicious authentication behavior
- login attack patterns

Today SentinelIDS started detecting real attack behavior patterns.

---

# Code Logic

Current system flow:

generate login attack
→ track IP
→ track failed logins
→ analyze behavior
→ detect suspicious activity
→ detect brute-force attack
→ generate alerts
→ write logs
→ continue monitoring

---

# Cybersecurity Concept

Today I learned how brute-force attacks work.

Brute-force attacks:
- repeatedly try passwords
- attempt unauthorized access
- automate login attempts

Behavior-based IDS systems can detect:
- repeated failed logins
- high authentication activity
- suspicious login behavior

Today SentinelIDS successfully simulated and detected brute-force attacks in real time.

---

# Problems Faced

## 1. Infinite monitoring loop control

Problem:
The IDS system continuously ran without stopping.

Solution:
Used:

CTRL + C

to manually stop the monitoring engine.

This generated a normal:

KeyboardInterrupt

message.

---

## 2. Brute-force alert initially did not appear

Problem:
The system stopped before reaching the failed login threshold.

Solution:
Allowed the system to continue running until:
5 failed logins

were reached.

After that:
Brute force alerts were successfully generated.

---

# Next Goals

Next steps:
- Threat score system
- Risk-based analysis
- Multi-attack correlation
- Dashboard development
- Database integration
- Real packet analysis
- Docker attack lab
- AI-based anomaly detection