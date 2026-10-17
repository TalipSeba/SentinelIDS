from dashboard import get_stats


def test_get_stats_counts_rows(db):
    db.save_attack("2026-10-17 10:00:00", "192.168.1.200", "BRUTE_FORCE", 20)
    db.save_attack("2026-10-17 10:00:01", "192.168.1.200", "BRUTE_FORCE", 40)
    db.save_attack("2026-10-17 10:00:02", "192.168.1.50", "PORT_SCAN", 10)

    stats = get_stats()

    assert stats["total_attacks"] == 3
    assert stats["max_score"] == 40
    assert stats["dangerous_ip"] == "192.168.1.200"
    assert dict(stats["attack_type_counts"]) == {"BRUTE_FORCE": 2, "PORT_SCAN": 1}
    assert stats["top_attackers"][0] == ("192.168.1.200", 2)





def test_get_stats_honest_counts(db):
    db.save_attack("2026-10-17 10:00:00", "192.168.1.200", "BRUTE_FORCE", 20)
    db.save_attack("2026-10-17 10:00:01", "192.168.1.200", "BRUTE_FORCE", 40)
    db.save_attack("2026-10-17 10:00:01", "192.168.1.200", "HIGH_RISK", 40)
    db.save_attack("2026-10-17 10:00:02", "192.168.1.200", "HIGH_RISK", 40)
    db.save_attack("2026-10-17 10:00:03", "192.168.1.50", "PORT_SCAN", 10)

    stats = get_stats()

    assert stats["unique_ips"] == 2
    assert stats["brute_force_count"] == 2
    assert stats["port_scan_count"] == 1
    assert stats["high_risk_ips"] == 1


def test_get_stats_empty_database(db):
    stats = get_stats()

    assert stats["total_attacks"] == 0
    assert stats["max_score"] == 0
    assert stats["unique_ips"] == 0
    assert stats["brute_force_count"] == 0
    assert stats["port_scan_count"] == 0
    assert stats["high_risk_ips"] == 0



