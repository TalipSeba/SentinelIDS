def parse_event(level, message):

    parts = message.split()
    ip = parts[0]

    if level == "LOGIN_FAILED":
        return "LOGIN_FAILED", ip, None

    if "connected to port" in message:
        return "CONNECTION", ip, parts[-1]

    return None, ip, None
