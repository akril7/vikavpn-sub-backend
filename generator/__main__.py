import os
from pathlib import Path

from .backends.trusttunnel import setup_trusttunnel
from .backends.clash import create_clash_configs
from .backends.mieru import setup_mieru

from . import config

os.chdir(Path(__file__).parent.resolve())

create_clash_configs(config.SERVER, config.CREDENTIALS)
setup_trusttunnel(config.CREDENTIALS)
setup_mieru(config.CREDENTIALS)

print()
print("=== Subscription Links ===")
print()

from users import load_users

users = load_users()

for username, uid in users.items():
    print(f"{username}: https://{config.DOMAIN}/sub/{uid}")
