# Day 1 — SentinelIDS Project Initialization

## What We Built

Today we created the initial structure of the SentinelIDS project.

We built:
- A logging system
- A detector engine
- An alert generation system
- A modular Python project structure

---

## Project Structure

Created folders:
- src/
- logs/
- docs/
- tests/

Created files:
- main.py
- logger.py
- detector.py
- .gitignore
- README.md

---

## What I Learned

Today I learned:
- Basic Python project structure
- Functions in Python
- Event processing logic
- Logging systems
- Detection systems
- Git initialization
- Git commits
- .gitignore usage

---

## Logging System

We created a custom logging system.

Purpose:
To record security-related events into a log file.

The logger module writes:
- INFO logs
- WARNING logs
- ALERT logs
- ERROR logs

into:
logs/system.log

---

## Detector Engine

We created a basic detection engine.

Purpose:
To analyze incoming events and detect suspicious behavior.

Current detection:
- Multiple port attempts

If suspicious behavior is detected,
the system automatically generates alerts.

---

## Why This Is Important

This is the foundation of a real IDS system.

Real IDS systems:
- receive events
- analyze behavior
- generate alerts
- store logs

SentinelIDS now has the same core logic.

---

## Git Workflow

Initialized Git repository.

Created first commit:

"Initial SentinelIDS core system"

This allows:
- version control
- project history
- rollback capability

---

## Problems Faced

Git commit initially failed because Git user identity was not configured.

Solution:
Configured Git username and email using git config.

---

## Next Goals

Next steps:
- Generate fake traffic
- Simulate attacks
- Analyze IP behavior
- Count suspicious requests
- Improve detection engine
