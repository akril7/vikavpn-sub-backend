#!/bin/bash

set -e

cd /opt/vikavpn-sub-backend/
.venv/bin/python -c "from updater import update; update()"
