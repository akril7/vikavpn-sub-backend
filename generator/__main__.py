import os
from pathlib import Path

from .backends.trusttunnel import setup_trusttunnel
from .backends.clash import create_clash_configs
from .backends.mita import setup_mita
from .backends.xray import setup_xray

from .users import load_users

from . import config

os.chdir(Path(__file__).parent.resolve())

create_clash_configs(config.SERVER, config.CREDENTIALS, config.XRAY_PUBLIC_KEY)
setup_trusttunnel(config.CREDENTIALS)
setup_mita(config.CREDENTIALS)
setup_xray(config.CREDENTIALS)

print("=== Subscription Links ===")
print()

users = load_users()

for username, uuid in users.items():
    print(f"{username}: https://{config.SUB_DOMAIN}/sub/{uuid}")
