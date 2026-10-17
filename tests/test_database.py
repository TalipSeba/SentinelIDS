def test_save_attack_inserts_row(db):
    db.save_attack("2026-10-16 12:00:00", "192.168.1.200", "PORT_SCAN", 15)

    rows = db.cursor.execute(
        "SELECT timestamp, ip, event_type, threat_score FROM attack_logs"
    ).fetchall()

    assert rows == [("2026-10-16 12:00:00", "192.168.1.200", "PORT_SCAN", 15)]
