# Robot Setup (Raspberry Pi)

This page covers setting up the Raspberry Pi that drives the physical robot: logging in, giving it a static IP on the venue's network, setting up its Python environment, and making its control service start automatically on boot.

## 1. Log in to the robot

Connect to the Raspberry Pi using **VNC** with the robot's IP address. Username and password are both `admin`.

## 2. Set a static IP address

```
admin@raspberrypi:~ $ nmcli connection show
```

You should see output like:

```
NAME                UUID                                  TYPE      DEVICE
preconfigured       bab1e090-17e1-417d-bbee-9f67344bf3d7  wifi      wlan0
lo                  1742d74f-ea92-4767-9e5e-b31860520e96  loopback  lo
Wired connection 1  a537414c-649c-34ab-bb22-70d57162342b  ethernet  --
```

Modify the network connection with the desired static IP (replace `"TP-Link_2110"` with the actual connection name from the list above):

```
sudo nmcli connection modify "TP-Link_2110" ipv4.addresses 192.168.0.106/24
sudo nmcli connection modify "TP-Link_2110" ipv4.gateway 192.168.1.1
sudo nmcli connection modify "TP-Link_2110" ipv4.dns "8.8.8.8 8.8.4.4"
sudo nmcli connection modify "TP-Link_2110" ipv4.method manual
```

Confirm the new address, then reboot:

```
admin@raspberrypi:~ $ ip -a
sudo reboot
```

> **Note:** once the Pi's IP changes, update the IP address the robot listens on / the address Unity connects to in `run_robot.py` (see step 4 below) and on the Unity side — see [unity-dev-setup.md](unity-dev-setup.md).

## 3. Set up the Python environment (on a new robot)

```
cd THRIVE-System
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## 4. Point `run_robot.py` at the robot's IP

Change the IP address the socket server binds to in `run_robot.py` to match the static IP set in step 2.

## 5. Run `robot_ready.sh` automatically on boot

Create the systemd service file:

```
sudo nano /etc/systemd/system/robot_ready.service
```

With contents:

```ini
[Unit]
Description=Robot Ready Service
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/bin/bash /home/admin/THRIVE-System/service/robot_ready.sh
Type=simple
Environment="XDG_RUNTIME_DIR=/run/user/1000"
User=admin
Group=audio
Restart=on-failure
RestartSec=1

[Install]
WantedBy=multi-user.target
```

Then enable and start it:

```
sudo systemctl enable robot_ready.service
sudo systemctl start robot_ready.service
sudo reboot
```

### If it doesn't come up after reboot

Reload and try again:

```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable robot_ready.service
sudo systemctl start robot_ready.service
```

Check the logs for errors:

```
journalctl -u robot_ready.service --no-pager -n 50
```
