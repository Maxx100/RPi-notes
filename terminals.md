SSH settings:\
`sudo nano /etc/ssh/sshd_config`\
`sudo systemctl restart sshd`\
Transfer files (SSH): `scp -P PORT file username@host:directory`

RPi Temperature:\
Once: `vcgencmd measure_temp`\
Every N seconds: `watch -n N vcgencmd measure_temp`

Admin cmd's:\
`sudo halt` - shutdown\
`sudo reboot` - reboot

`nohup program </dev/null &` - exec program in backgroung (with ssh)\
`ps` - for find PID, `kill PID` for kill task

Python:\
Venv creating: `python -m venv name`\
Venv activate: `source name/bin/activate`\
Venv install pkg: `name/bin/pip install LibName` (or `pip install LibName` after activating)

Net settings:\
Ports checking: `sudo lsof -i -P -n`\
Net status: `nmcli dev status`\
WIFI on/off: `nmcli radio wifi on/off`

Services:\
CD to serv folder: `cd /lib/systemd/system`\
Create service: `sudo nano <name>.service`\
(recomended use bash script to start your tasks. For example in *1)\
Reload systemctl: `sudo systemctl daemon-reload`\
Enable service: `sudo systemctl enable <name>.service`\
Start service: `sudo systemctl start <name>.service`\
Check service: `sudo systemctl status <name>.service`\
Reload service: `sudo systemctl restart <name>.service`

__________\
*1
```
[Unit]
Description=<name of service>
After=network.target

[Service]
Type=idle
Restart=always
RestartSec=3
User=<username>
WorkingDirectory=<folder with bash script>
ExecStart=/bin/bash ./<name>.sh

[Install]
WantedBy=multi-user.target
```
