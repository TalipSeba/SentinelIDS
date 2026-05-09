def detect_event(message):

    if "multiple ports" in message:

        ip = message.split()[0]

        return "ALERT", f"Possible port scan detected from {ip}"

    return None