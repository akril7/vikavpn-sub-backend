import json


def generate_mieru(creds):
    with open("templates/mita.json") as f:
        config = json.load(f)

    for username, password in creds:
        config["users"].append({
            "name": username,
            "password": password
        })

    with open("data/mita.json", "w") as f:
        json.dump(config, f, indent=2)
