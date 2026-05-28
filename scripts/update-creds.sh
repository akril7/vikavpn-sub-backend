#!/bin/bash

set -e

cd /opt/sub-backend

./venv/bin/python -c "from services.updater import update; update()"
