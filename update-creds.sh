#!/bin/bash

set -e

cd /opt/vikavpn-sub-backend/generator
../.venv/bin/python -c "from generator.updater import update; update('credentials')"
