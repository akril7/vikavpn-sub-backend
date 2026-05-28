import json

from config import MIERU_TEMP_CONFIG


def generate_mieru(creds):
    config = {
        "portBindings": [
            {
                "port": 443,
                "protocol": "TCP"
            }
        ],
        "users": [],
        "loggingLevel": "INFO",
        "mtu": 1400
    }

    for username, password in creds:
        config["users"].append({
            "name": username,
            "password": password
        })

    with open(MIERU_TEMP_CONFIG, "w") as f:
        json.dump(config, f, indent=4)
