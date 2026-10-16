ip_counts = {}
ip_ports = {}

def track_ip(ip):
    if ip not in ip_counts:
        ip_counts[ip] = 0

    ip_counts[ip] += 1

    return ip_counts[ip]


def track_port(ip, port):
    if ip not in ip_ports:
        ip_ports[ip] = set()

    ip_ports[ip].add(port)

    return len(ip_ports[ip])


def is_suspicious(ip):
    if ip_counts.get(ip, 0) >= 4:
        return True

    return False


def is_port_scan(ip):
    if ip in ip_ports and len(ip_ports[ip]) >= 4:
        return True

    return False

failed_logins = {}
def track_failed_login(ip):

    if ip not in failed_logins:
        failed_logins[ip] = 0

    failed_logins[ip] += 1

    return failed_logins[ip]
def is_bruteforce(ip):

    if failed_logins.get(ip, 0) >= 5:
        return True

    return False