SSH settings:\
`sudo nano /etc/ssh/sshd_config`\
`sudo systemctl restart sshd`

RPi Temperature
Once: `vcgencmd measure_temp`
Every N seconds: `watch -n N vcgencmd measure_temp`

Admin cmd's:
`sudo halt` - shutdown
`sudo reboot` - reboot

`nohup program </dev/null &` - exec program in backgroung (with ssh)
`ps` - for find PID, `kill PID` for kill task

Python:
Venv creating: `python -m venv name`
Venv activate: `source name/bin/activate`
Venv install pkg: `name/bin/pip install LibName` (or `pip install LibName` after activating)

Net settings:
Ports checking: `sudo lsof -i -P -n`
