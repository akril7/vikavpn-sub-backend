from pathlib import Path

from config import SUBS_DIR, SERVER_IP
from models.users import get_or_create_uid

TEMPLATE_PATH = "/opt/sub-backend/templates/clash.yaml"


def generate_clash(creds):
    Path(SUBS_DIR).mkdir(parents=True, exist_ok=True)

    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    generated = []

    for username, password in creds:
        uid = get_or_create_uid(username)

        content = template \
            .replace("{USERNAME}", username) \
            .replace("{PASSWORD}", password) \
            .replace("{SERVER}", SERVER_IP)

        path = f"{SUBS_DIR}/{uid}.yaml"

        with open(path, "w") as out:
            out.write(content)

        generated.append((username, uid))

    return generated
