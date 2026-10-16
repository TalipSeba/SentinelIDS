threat_scores = {}
high_risk_ips = set()

def increase_score(ip, points):

    if ip not in threat_scores:
        threat_scores[ip] = 0

    threat_scores[ip] += points

    return threat_scores[ip]


def get_score(ip):

    return threat_scores.get(ip, 0)


def is_high_risk(ip):

    if ip in threat_scores and threat_scores[ip] >= 30:
        return True

    return False


def mark_high_risk(ip):

    # True only the first time an IP crosses the threshold
    if not is_high_risk(ip) or ip in high_risk_ips:
        return False

    high_risk_ips.add(ip)

    return True
