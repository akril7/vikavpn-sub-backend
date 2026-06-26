import json
import subprocess
from pathlib import Path


def setup_mita(credentials):
    Path('data').mkdir(parents=True, exist_ok=True)

    with open("templates/mita.json") as f:
        config = json.load(f)

    users = [{"name": username, "password": password} for username, password in credentials.items()]
    config["users"] = users

    with open("data/mita.json", "w") as f:
        json.dump(config, f, indent=4)

    subprocess.run(["mita", "apply", "config", "data/mita.json"])
    subprocess.run(["systemctl", "restart", "mita"])
