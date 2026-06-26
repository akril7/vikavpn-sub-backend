from pathlib import Path

from ..users import get_or_create_uid

SUBS_DIR = "data/subs"


def create_clash_configs(server, credentials, xray_pubkey):
    Path(SUBS_DIR).mkdir(parents=True, exist_ok=True)

    with open("templates/clash.yaml", "r") as f:
        template = f.read()

    generated = []

    for username, password in credentials.items():
        uuid = get_or_create_uid(username)

        content = template \
            .replace("{UUID}", uuid) \
            .replace("{USERNAME}", username) \
            .replace("{PASSWORD}", password) \
            .replace("{SERVER}", server) \
            .replace("{REALITY-PUBLIC-KEY}", xray_pubkey)

        path = f"{SUBS_DIR}/{uuid}.yaml"

        with open(path, "w") as out:
            out.write(content)

        generated.append((username, uuid))

    return generated
