#!/bin/bash

set -e

cd /opt/vikavpn-sub-backend/generator
./venv/bin/python -c "from services.updater import update; update('credentials')"
