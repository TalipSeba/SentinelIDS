from threat_score import increase_score, is_high_risk
from tracker import is_bruteforce, is_port_scan, track_failed_login, track_port

IP = "192.168.1.200"


def test_port_scan_needs_four_distinct_ports():
    for port in ["21", "22", "80"]:
        track_port(IP, port)
    assert not is_port_scan(IP)

    track_port(IP, "443")
    assert is_port_scan(IP)


def test_repeated_port_does_not_count_twice():
    for _ in range(5):
        track_port(IP, "22")
    assert not is_port_scan(IP)


def test_port_scan_unknown_ip():
    assert not is_port_scan("10.0.0.1")


def test_brute_force_needs_five_failures():
    for _ in range(4):
        track_failed_login(IP)
    assert not is_bruteforce(IP)

    track_failed_login(IP)
    assert is_bruteforce(IP)


def test_high_risk_at_score_30():
    increase_score(IP, 20)
    assert not is_high_risk(IP)

    assert increase_score(IP, 10) == 30
    assert is_high_risk(IP)


def test_high_risk_unknown_ip():
    assert not is_high_risk("10.0.0.1")
