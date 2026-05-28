#!/bin/bash

set -e

cd /opt/vikavpn-sub-backend/generator
../.venv/bin/python -c "from updater import update; update('credentials')"
