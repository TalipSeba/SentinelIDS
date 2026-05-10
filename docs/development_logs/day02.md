# Day 2 — IP Tracking and Suspicious Activity Detection

## What We Built

Today we improved the SentinelIDS detection logic.

We built:
- An IP tracking system
- A request counting system
- A threshold-based detection system
- A suspicious activity warning mechanism

---

## Project Structure Update

Created new file:
- tracker.py

Updated files:
- main.py
- tracker.py

---

## What I Learned

Today I learned:
- Dictionary usage in Python
- IP-based tracking logic
- Request counting
- Threshold-based detection
- Suspicious activity analysis
- Behavior-based security detection
- Importing multiple functions from a module

---

## IP Tracking System

We created a tracker module.

Purpose:
To count how many times each IP address sends requests or appears in security events.

The tracker module stores IP counts using a dictionary.

Example:

192.168.1.20 → 4 requests  
192.168.1.30 → 2 requests

This allows the system to understand which IP address is more active or suspicious.

---

## Threshold Detection

We added a threshold rule.

Current rule:
If an IP address sends 4 or more requests,
the system marks it as suspicious.

This is a basic behavior-based detection method.

---

## Suspicious Activity Detection

When an IP address reaches the threshold,
SentinelIDS generates a warning log.

Example:

[WARNING] Suspicious IP activity detected from 192.168.1.20

This means the system is no longer only logging events.
It is now analyzing behavior and detecting suspicious activity.

---

## Why This Is Important

This is an important step toward a real IDS system.

Real IDS systems do not only look at single events.
They analyze behavior over time.

For example:
- Too many requests from one IP
- Multiple port attempts
- Repeated login failures
- Unusual traffic patterns

Today we added the first behavior analysis feature to SentinelIDS.

---

## Code Logic

The tracker.py module keeps request counts for each IP address.

The main.py file:
- reads events
- extracts the IP address
- sends the IP to tracker.py
- checks if the IP is suspicious
- generates a warning if needed

Current flow:

event → extract IP → count request → check threshold → generate warning → write log

---

## Cybersecurity Concept

Today I learned the basic idea of behavior-based detection.

Behavior-based detection means:
Instead of checking only one event,
the system watches repeated actions and detects suspicious patterns.

This is useful for detecting:
- port scans
- brute-force attempts
- reconnaissance activity
- suspicious repeated requests

---

## Problems Faced

No major technical error occurred today.

One important point was remembering to import the new function correctly.

We updated:

from tracker import track_ip

to:

from tracker import track_ip, is_suspicious

---

## Next Goals

Next steps:
- Generate dynamic fake traffic
- Create random IP events
- Simulate attacker behavior
- Improve port scan detection
- Add threat score logic
- Prepare for real-time event processing