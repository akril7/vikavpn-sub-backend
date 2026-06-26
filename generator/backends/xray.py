import json
import subprocess
from pathlib import Path

from ..users import get_or_create_uid


def setup_xray(credentials, xray_privkey):
    Path('data').mkdir(parents=True, exist_ok=True)

    clients = [{"id": get_or_create_uid(username), "flow": "xtls-rprx-vision"} for username in credentials.keys()]

    with open("templates/xray.json") as f:
        config = json.load(f)

    for inbound in config["inbounds"]:
        inbound["settings"]["clients"] = clients
        inbound["streamSettings"]["realitySettings"]["privateKey"] = xray_privkey

    with open("/usr/local/etc/xray/config.json", "w") as f:
        json.dump(config, f, indent=4)

    subprocess.run(["systemctl", "restart", "xray"])
