#!/bin/bash

set -e

REPO_URL="https://github.com/hugmeagn/vikavpn-sub-backend.git"
INSTALL_DIR="/opt/vikavpn-sub-backend"

echo "========================================"
echo "VikaVPN Sub Backend Installer"
echo "========================================"
echo

read -p "DOMAIN (example: sub.example.com:9443): " DOMAIN
read -p "SERVER (example: 1.2.3.4 or vpn.example.com): " SERVER

echo
echo "[1/9] Installing packages..."

apt update

apt install -y \
    git \
    python3 \
    python3-pip \
    python3-venv \
    nginx

echo
echo "[2/9] Cloning repository..."

rm -rf "$INSTALL_DIR"

git clone "$REPO_URL" "$INSTALL_DIR"

cd "$INSTALL_DIR"

echo
echo "[3/9] Creating venv..."

python3 -m venv .venv

./.venv/bin/pip install -r requirements.txt

echo
echo "[4/9] Configuring generator/config.py..."

cat > generator/config.py << EOF
DOMAIN = "${DOMAIN}"
SERVER = "${SERVER}"

TRUSTTUNNEL_CONFIG = "/opt/trusttunnel/credentials.toml"
EOF

echo
echo "[5/9] Creating systemd service..."

cat > /etc/systemd/system/vikavpn-sub-backend.service << EOF
[Unit]
Description=VikaVPN Subscription Backend
After=network.target

[Service]
Type=simple

WorkingDirectory=${INSTALL_DIR}

ExecStart=${INSTALL_DIR}/.venv/bin/python ${INSTALL_DIR}/webserver.py

Restart=always
RestartSec=3

User=root
Group=root

Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

echo
echo "[6/9] Configuring nginx..."

cat > /etc/nginx/sites-available/vikavpn-sub-backend << EOF
server {
    listen 7071 ssl http2;

    server_name ${DOMAIN};

    ssl_certificate /etc/ssl/certs/vikavikavika.ru;
    ssl_certificate_key /etc/ssl/private/vikavikavika.ru;

    location /sub/ {
        proxy_pass http://127.0.0.1:5000;

        proxy_set_header Host \$host;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }
}
EOF

ln -sf \
    /etc/nginx/sites-available/vikavpn-sub-backend \
    /etc/nginx/sites-enabled/vikavpn-sub-backend

echo
echo "[7/9] Reloading services..."

systemctl daemon-reload

systemctl enable vikavpn-sub-backend
systemctl restart vikavpn-sub-backend

nginx -t

systemctl restart nginx

echo
echo "[8/9] Creating credentials file..."

if [ ! -f "${INSTALL_DIR}/credentials" ]; then
cat > "${INSTALL_DIR}/credentials" << EOF
changeme-login:changeme-password
EOF
fi

chmod +x "${INSTALL_DIR}/update-creds.sh"

echo
echo "[9/9] Done."

echo
echo "========================================"
echo "Installed successfully"
echo "========================================"
echo
echo "Backend directory:"
echo "${INSTALL_DIR}"
echo
echo "Edit credentials:"
echo "${INSTALL_DIR}/credentials"
echo
echo "Generate subscriptions:"
echo "cd ${INSTALL_DIR} && ./update-creds.sh"
echo
echo "Subscription URL format:"
echo "https://${DOMAIN}/sub/<uid>"
echo
echo "Service status:"
echo "systemctl status vikavpn-sub-backend"
echo
echo "Logs:"
echo "journalctl -u vikavpn-sub-backend -f"
echo
echo "========================================"
