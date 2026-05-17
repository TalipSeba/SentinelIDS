# Day 7 - Flask Dashboard and Attack Analytics

## Goal

Today the SentinelIDS project was transformed from a terminal-based IDS into a web-based monitoring platform using Flask.

The main objective was to create the first security dashboard interface and display live attack analytics directly from the SQLite database.

---

# Features Added

## 1. Flask Web Dashboard

A Flask-based web server was developed.

The dashboard can now be accessed from a browser using:

http://127.0.0.1:5000

This was the first step toward building a real SOC/SIEM-style interface.

---

## 2. Live Database Integration

The dashboard was connected directly to the SQLite attack_logs database.

Attack information is now dynamically pulled from the database instead of using static values.

---

## 3. Total Attack Counter

SQL COUNT queries were added.

The dashboard now displays:

- Total detected attacks

This allows analysts to quickly monitor attack activity.

---

## 4. Highest Threat Score Detection

SQL MAX queries were implemented.

The dashboard can now identify:

- The highest threat score recorded in the system

This helps determine the severity of attacks.

---

## 5. Most Dangerous IP Analysis

The system now identifies:

- The IP address associated with the highest threat score

This creates the foundation for attacker profiling and threat intelligence analysis.

---

## 6. Dashboard UI Improvements

The dashboard interface was redesigned using custom HTML styling.

Improvements included:

- Dark background
- Modern colors
- Security dashboard layout
- Styled analytics panel

The interface now resembles a lightweight SOC monitoring dashboard.

---

# Technologies Used

- Python
- Flask
- SQLite3
- SQL Queries
- HTML
- Inline CSS

---

# Problems Faced

## 1. Flask Installation Restriction on Kali Linux

While installing Flask, Kali Linux blocked system-wide package installation because of externally managed Python packages.

Solution:

Flask was installed using:

pip install flask --break-system-packages

---

## 2. Flask Server Process

The Flask server occupied the terminal session while running.

Solution:

The server was stopped safely using:

CTRL + C

---

# Results

At the end of Day 7, SentinelIDS successfully evolved into a browser-accessible monitoring platform.

The project now supports:

- Live dashboard monitoring
- Attack analytics
- Threat score visualization
- Dangerous IP detection
- Database-driven reporting

This day marked the beginning of the project's SOC/SIEM dashboard architecture.

---

# Next Goals

Next development targets:

- Real-time attack feed
- Attack tables
- Dashboard charts
- Packet analysis integration
- Login system
- Docker attack lab integration
- AI-supported anomaly detection