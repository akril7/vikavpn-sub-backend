import subprocess

from generators.trusttunnel import generate_trusttunnel
from generators.mieru import generate_mieru
from generators.clash import generate_clash

from config import CREDS_FILE, DOMAIN, MIERU_TEMP_CONFIG


def read_creds():
    creds = []

    with open(CREDS_FILE, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            username, password = line.split(":", 1)

            creds.append((username, password))

    return creds


def update():
    creds = read_creds()

    generate_trusttunnel(creds)

    generate_mieru(creds)

    generate_clash(creds)

    subprocess.run(
        ["systemctl", "restart", "trusttunnel"],
        check=True
    )

    subprocess.run(
        ["mita", "apply", "config", MIERU_TEMP_CONFIG],
        check=True
    )

    subprocess.run(
        ["systemctl", "restart", "mita"],
        check=True
    )

    print()
    print("=== Subscription Links ===")
    print()

    from models.users import load_users

    users = load_users()

    for username, uid in users.items():
        print(f"{username}: {DOMAIN}/sub/{uid}")
