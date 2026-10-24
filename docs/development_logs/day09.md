cat > docs/development_logs/day09.md <<'MDEOF'
# Day 9 — Honest Dashboard Statistics and Automated Tests

## What Was Done?

The goal of the day was a dashboard where every number has a clear meaning and is proven by a test, not by looking at the screen.

Work was done on the branch `day09-dashboard-stats`, in small steps. Each step was committed separately:

| Commit | Change |
|---|---|
| `0d29c77` | PR #1 (pytest tests) merged into `main`. `threat_score.high_risk_ips.clear()` was added to `tests/conftest.py` so tests do not affect each other |
| `25b760d` | Dashboard SQL queries moved from `home()` into a separate `get_stats()` function, plus a test for it |
| `6a97564` | Honest statistic cards: Total Alerts, Unique Source IPs, Brute Force Alerts, Port Scan Alerts, High Risk IPs. Empty database shows `0` / `-` instead of `None` |
| `2bbea5a` | HIGH_RISK removed from the attack type distribution. One color per attack type, defined once in `ATTACK_COLORS` |
| `19b4c8e` | Attack distribution changed from a pie chart to a bar chart. Types with zero alerts (for example PORT_SCAN = 0) are still shown |
| `558300c` | Hourly alert trend (line chart), grouped with `substr(timestamp, 1, 13)` |
| `fe550b4` | Hard-coded "ACTIVE" replaced by "Last Record" (`MAX(timestamp)`). Data source label added. Time column added to the Recent Attacks table. "attacks" renamed to "alerts" in Top Attacker IPs |
| `092dff6` | `docs/day07.md` moved into `docs/development_logs/`, where the other daily logs are |

Test count: 8 tests at the start of the day, 18 tests at the end. All 18 pass (`python3 -m pytest -q`).

## Why Was It Done?

Before today some dashboard numbers were misleading:

- "Total Attacks 8" was really 8 alert rows from one simulated attacker in a 4-second test run (2026-05-13 09:59:42-45).
- HIGH_RISK was shown as an attack type next to BRUTE_FORCE. It is a risk level, not a behavior, so the same event was counted twice.
- "ACTIVE" was a fixed text. It was shown even when the program was not running.
- The page said "live SQLite logs", but the data comes from `traffic_generator.py`, not from a real network.

## How the Numbers Are Counted

| Card | SQL | Meaning |
|---|---|---|
| Total Alerts | `COUNT(*)` | Number of alert rows |
| Unique Source IPs | `COUNT(DISTINCT ip)` | How many different IPs created alerts |
| Brute Force Alerts | `COUNT(*) WHERE event_type = 'BRUTE_FORCE'` | Brute force alert rows |
| Port Scan Alerts | `COUNT(*) WHERE event_type = 'PORT_SCAN'` | Port scan alert rows |
| High Risk IPs | `COUNT(DISTINCT ip) WHERE event_type = 'HIGH_RISK'` | Number of risky IPs (not rows) |
| Highest Threat Score | `COALESCE(MAX(threat_score), 0)` | Highest cumulative score of one IP |
| Last Record | `MAX(timestamp)` | Time of the newest alert |

## End-to-End Check

The database was backed up first (`cp sentinelids.db ~/sentinelids-backup.db`), because `sentinelids.db` is tracked by Git.

Then `src/dashboard.py` and `src/main.py` were run together for about one minute (2026-10-24, around 12:06-12:10).

Every card was compared with a read-only database query (`mode=ro`):

| Card | Dashboard | Database |
|---|---|---|
| Total Alerts | 81 | 81 |
| Highest Threat Score | 1200 | 1200 |
| Unique Source IPs | 1 | 1 |
| Brute Force Alerts | 46 | 46 |
| Port Scan Alerts | 29 | 29 |
| High Risk IPs | 1 | 1 (6 rows, 1 distinct IP) |
| Last Record | 2026-10-24 12:10:04 | 2026-10-24 12:10:04.752040 |

All values matched. After the check the backup was copied back and `git status` was clean.

## Findings

These were observed today. They are not fixed yet:

1. **No score limit.** After the thresholds are passed, every new event from the attacker adds points again. The score reached 1200 in about one minute.
2. **Alert flooding.** After the 5th failed login, every new failed login creates a new BRUTE_FORCE alert. One attacker produced 46 brute force alerts. In a SOC this is called alert fatigue.
3. **Detection memory is only in RAM.** Counters, scores and the "already marked HIGH_RISK" set are reset when `main.py` restarts. Today two HIGH_RISK rows were written for the same IP (12:06:41 and 12:08:25), both with score 45. This shows the program started again from zero at around 12:08.
4. **No time window in the rules (known from earlier analysis).** Rules count "4 ports in all time", not "4 ports in 10 seconds". In an earlier isolated simulation of 20,000 events (run during the Day 9 analysis, not on this machine), 253 normal IPs were also marked as PORT_SCAN and HIGH_RISK. In today's one-minute run only 192.168.1.200 created alerts.
5. **Flask debug mode is on.** This is acceptable on 127.0.0.1 for development, but must be turned off if the dashboard is opened to a network.

## New Concepts Learned

- pytest, `assert`, fixtures (`tmp_path`, `monkeypatch.chdir`), Arrange-Act-Assert
- TDD: write a failing test first (red), then make it pass (green)
- Refactoring: changing code structure without changing behavior
- SQL: `WHERE`, `COUNT(DISTINCT ...)`, `COALESCE`, NULL, `substr`, `GROUP BY` on time
- `?` parameters and why they prevent SQL injection
- `json.dumps` for safely passing Python data to JavaScript
- `{{` and `}}` inside Python f-strings
- Git: branch, merge, pull request, fast-forward, adding files by name instead of `git add .`
- GitHub fine-grained personal access token (least privilege)
- `less` pager: press `q` before typing new commands

## Errors Encountered and Solutions

1. **`git push` asked for a password.** GitHub no longer accepts account passwords for Git. A fine-grained personal access token was created and used instead.
2. **`NameError: name 'op_attackers' is not defined`.** A letter was lost while pasting. Reading the traceback from the bottom and the "Did you mean" hint showed the typo.
3. **`NameError: name 'app' is not defined` in `test_stats.py`.** A dashboard test was pasted into the wrong file. It was moved to `test_dashboard.py`. The old copy stayed because the file was not saved.
4. **A file named `t -q` appeared.** While `git diff` was open in `less`, typing a command made `less` save its help page to a file. The file was checked and deleted.

## Next Goals

- Time window for detection rules (fix false positives)
- Stop alert flooding: one alert per attacker per time period
- Add a `source` column (`simulated` / `live`) to keep test and real data separate
- Decide what to do with `sentinelids.db` being tracked by Git
- First real data source: SSH login failures from system logs
MDEOF