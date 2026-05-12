import random

ports = [21, 22, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

attacker_ip = "192.168.1.200"

def generate_ip():
    return f"192.168.1.{random.randint(1, 254)}"


def generate_event():
    attack_chance = random.randint(1, 100)

    if attack_chance <= 40:
        ip = attacker_ip
    else:
        ip = generate_ip()

    if ip == attacker_ip:
       attack_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
       port = random.choice(attack_ports)
    else:
       port = random.choice(ports)

    return ("INFO", f"{ip} connected to port {port}")

def generate_login_event():

    ip = attacker_ip

    usernames = ["admin", "root", "user", "test"]
    passwords = ["123456", "admin", "password", "qwerty"]

    username = random.choice(usernames)
    password = random.choice(passwords)

    return ("LOGIN_FAILED", f"{ip} failed login with username={username} password={password}")