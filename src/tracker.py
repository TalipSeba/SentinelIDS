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
    if ip_counts[ip] >= 4:
        return True

    return False


def is_port_scan(ip):
    if ip in ip_ports and len(ip_ports[ip]) >= 4:
        return True

    return False