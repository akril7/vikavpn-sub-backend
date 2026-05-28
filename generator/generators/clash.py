from pathlib import Path

from config import SERVER
from users import get_or_create_uid

SUBS_DIR = "data/subs"


def generate_clash(creds):
    Path(SUBS_DIR).mkdir(parents=True, exist_ok=True)

    with open("templates/clash.yaml", "r") as f:
        template = f.read()

    generated = []

    for username, password in creds:
        uid = get_or_create_uid(username)

        content = template \
            .replace("{USERNAME}", username) \
            .replace("{PASSWORD}", password) \
            .replace("{SERVER}", SERVER)

        path = f"{SUBS_DIR}/{uid}.yaml"

        with open(path, "w") as out:
            out.write(content)

        generated.append((username, uid))

    return generated
