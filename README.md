# VPN Subscription backend

**Program manage miero, xray and trusttunnel endpoint, config use clash format**


### Install

1. Clone
```
git clone https://github.com/akril7/vikavpn-sub-backend.git /opt/vikavpn-sub-backend
```

2. Setup
```
cd /opt/vikavpn-sub-backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Service
```
nano /etc/systemd/system/vikavpn-sub-backend.service
systemctl daemon-reload
systemctl enable vikavpn-sub-backend
systemctl start vikavpn-sub-backend
```

```
[Unit]
Description=VikaVPN Subscription Backend
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/vikavpn-sub-backend
ExecStart=/opt/vikavpn-sub-backend/.venv/bin/python /opt/vikavpn-sub-backend/webserver.py
Restart=always
RestartSec=3
User=root
Group=root
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

4. Edit configs
server data
```
nano generator/config.py
```

clash template
```
nano generator/templates/clash.yaml
```

mieru template
```
nano generator/templates/mita.json
```

xray template
```
nano generator/templates/xray.json
```

5. Get links
```
python -m generator
```
