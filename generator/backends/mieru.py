import json
import subprocess
from pathlib import Path


def setup_mieru(credentials):
    Path('data').mkdir(parents=True, exist_ok=True)

    with open("templates/mita.json") as f:
        config = json.load(f)

    for username, password in credentials.item():
        config["users"].append({
            "name": username,
            "password": password
        })

    with open("data/mita.json", "w") as f:
        json.dump(config, f, indent=4)

    subprocess.run(["mita", "apply", "config", "data/mita.toml"])
    subprocess.run(["systemctl", "restart", "mita"])
