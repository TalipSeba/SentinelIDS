ip_counts = {}

def track_ip(ip):
    if ip not in ip_counts:
        ip_counts[ip] = 0

    ip_counts[ip] += 1

    return ip_counts[ip]


def is_suspicious(ip):
    if ip_counts[ip] >= 4:
        return True

    return False