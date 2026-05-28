import json
import uuid
from pathlib import Path

from config import USERS_FILE


def load_users():
    path = Path(USERS_FILE)

    if not path.exists():
        return {}

    with open(path, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def get_or_create_uid(username):
    users = load_users()

    if username in users:
        return users[username]

    uid = uuid.uuid4().hex

    users[username] = uid

    save_users(users)

    return uid
