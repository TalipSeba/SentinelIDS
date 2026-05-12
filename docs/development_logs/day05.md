# Day 5 — Threat Score and High Risk Detection System

# What We Built

Today we upgraded SentinelIDS with a threat scoring and risk classification system.

We built:
- A threat score engine
- Risk point calculation logic
- High-risk attacker detection
- CRITICAL alert generation
- Risk-based behavior analysis
- Dynamic attack severity classification

---

# Project Structure Update

Created new file:
- threat_score.py

Updated files:
- main.py
- threat_score.py

---

# What I Learned

Today I learned:
- Threat scoring systems
- Risk-based analysis
- Dynamic score calculation
- Attack severity classification
- High-risk detection logic
- Security scoring concepts
- Risk correlation systems
- CRITICAL alert logic

---

# Threat Score System

We created a threat scoring engine.

Purpose:
To calculate how dangerous an IP address is based on its behavior.

The system now assigns points for malicious actions.

Current scoring rules:

- Suspicious activity → +5
- Port scan behavior → +10
- Brute-force attack → +20

Example:

192.168.1.200 → threat score = 35

This allows SentinelIDS to classify attackers based on risk level.

---

# High Risk Detection

We created a high-risk classification system.

Current rule:
If an IP address reaches 30 or more threat points,
the system generates a CRITICAL alert.

Example:

[CRITICAL] High risk attacker detected from 192.168.1.200

This simulates enterprise-level security risk analysis systems.

---

# Risk-Based Analysis

Previously:
The IDS system only detected attacks.

Now:
The system also evaluates:
- attack severity
- attacker behavior
- overall risk level

This is an important step toward SIEM-like behavior analysis.

---

# Why This Is Important

Real security systems do not only detect attacks.

They also:
- calculate risk levels
- prioritize threats
- classify attackers
- evaluate attack severity

For example:
- low-risk activity
- medium-risk activity
- high-risk attackers

Today SentinelIDS started performing risk-based security analysis.

---

# Code Logic

Current system flow:

generate attack
→ analyze behavior
→ detect suspicious activity
→ assign threat points
→ calculate risk score
→ classify attacker
→ generate CRITICAL alerts
→ continue monitoring

---

# Cybersecurity Concept

Today I learned how threat scoring systems work.

Modern SIEM and IDS systems use:
- behavior analysis
- attack correlation
- severity scoring
- risk classification

to determine how dangerous an attacker is.

Instead of treating all attacks equally,
security systems prioritize:
- more dangerous attackers
- repeated attacks
- combined attack behavior

Today SentinelIDS implemented its first risk-analysis engine.

---

# Problems Faced

## 1. Python indentation problem

Problem:
The write_log() function inside:

if is_high_risk(ip):

was not indented correctly.

Solution:
Corrected the indentation structure.

---

## 2. KeyError problem

Problem:
The system tried to access an IP threat score before it existed.

Error:

KeyError: '192.168.1.200'

Cause:
The IP was not yet stored in the threat_scores dictionary.

Solution:
Updated:

if threat_scores[ip] >= 30:

to:

if ip in threat_scores and threat_scores[ip] >= 30:

This prevented the system from crashing.

---

# Next Goals

Next steps:
- Threat score decay system
- Dynamic risk reduction
- Multi-attack correlation
- Database integration
- Dashboard interface
- Live attack statistics
- Docker attack environment
- AI-based anomaly analysis