threat_scores = {}

def increase_score(ip, points):

    if ip not in threat_scores:
        threat_scores[ip] = 0

    threat_scores[ip] += points

    return threat_scores[ip]


def is_high_risk(ip):

    if ip in threat_scores and threat_scores[ip] >= 30:
        return True

    return False