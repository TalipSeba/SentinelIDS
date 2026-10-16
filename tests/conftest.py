import importlib
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import threat_score
import tracker


@pytest.fixture(autouse=True)
def reset_state():
    tracker.ip_counts.clear()
    tracker.ip_ports.clear()
    tracker.failed_logins.clear()
    threat_score.threat_scores.clear()
    yield


@pytest.fixture
def db(tmp_path, monkeypatch):
    # database.py and dashboard.py open "sentinelids.db" relative to the cwd,
    # so run them from a temp dir to keep the real database untouched.
    monkeypatch.chdir(tmp_path)
    sys.modules.pop("database", None)
    database = importlib.import_module("database")
    yield database
    database.connection.close()
    sys.modules.pop("database", None)
