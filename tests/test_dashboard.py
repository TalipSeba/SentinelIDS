from dashboard import app


def test_dashboard_returns_200(db):
    db.save_attack("2026-10-16 12:00:00", "192.168.1.200", "BRUTE_FORCE", 35)

    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"SentinelIDS Dashboard" in response.data
    assert b"192.168.1.200" in response.data

def test_dashboard_empty_database_shows_no_none(db):
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Total Alerts" in response.data
    assert b"None" not in response.data

def test_chart_shows_every_attack_type_even_zero(db):
    db.save_attack("2026-10-17 10:00:00", "192.168.1.200", "BRUTE_FORCE", 20)
    db.save_attack("2026-10-17 10:00:01", "192.168.1.200", "HIGH_RISK", 30)

    response = app.test_client().get("/")

    assert b'labels: ["BRUTE_FORCE", "PORT_SCAN"]' in response.data
    assert b"data: [1, 0]" in response.data


def test_dashboard_shows_hourly_trend(db):
    db.save_attack("2026-10-17 10:05:00", "192.168.1.200", "BRUTE_FORCE", 20)
    db.save_attack("2026-10-17 11:15:00", "192.168.1.200", "BRUTE_FORCE", 40)

    response = app.test_client().get("/")

    assert b"trendChart" in response.data
    assert b'labels: ["2026-10-17 10:00", "2026-10-17 11:00"]' in response.data
    assert b"data: [1, 1]" in response.data


def test_dashboard_shows_last_record_and_data_source(db):
    db.save_attack("2026-10-17 10:05:00.123456", "192.168.1.200", "BRUTE_FORCE", 20)

    response = app.test_client().get("/")

    assert b"ACTIVE" not in response.data
    assert b"Last Record" in response.data
    assert b"2026-10-17 10:05:00" in response.data
    assert b".123456" not in response.data
    assert b"simulated test traffic" in response.data
