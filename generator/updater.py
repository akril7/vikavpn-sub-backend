import subprocess
from pathlib import Path

from generators.trusttunnel import generate_trusttunnel
from generators.mieru import generate_mieru
from generators.clash import generate_clash

from config import DOMAIN


def read_creds(creds_path: str):
    creds = []

    with open(creds_path, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            username, password = line.split(":", 1)

            creds.append((username, password))

    return creds


def update(creds_path: str):
    Path("data").mkdir(parents=True, exist_ok=True)

    creds = read_creds(creds_path)
    generate_trusttunnel(creds)
    generate_mieru(creds)
    generate_clash(creds)

    subprocess.run(
        ["systemctl", "restart", "trusttunnel"],
        check=True
    )

    subprocess.run(
        ["mita", "apply", "config", "data/mita.toml"],
        check=True
    )

    subprocess.run(
        ["systemctl", "restart", "mita"],
        check=True
    )

    print()
    print("=== Subscription Links ===")
    print()

    from users import load_users

    users = load_users()

    for username, uid in users.items():
        print(f"{username}: https://{DOMAIN}/sub/{uid}")
