# wol -- Wake on LAN python mini-script

A python script that provides wake-on-lan functionality to machines within your LAN.

Service implementation of a Wake on LAN service for linux.
 - It checks every hour if a machine is turned on by pinging it.
 - If the ping fails it sends a magic packet to the machine, waits a minute pings it again and resends a magic pack if it still cant get a ping.

# Instructions

Copy the project to /usr/bin/
```bash
cp -r /path/to/project/wol /usr/bin/
```

Copy wol.service to /etc/systemd/system
```bash
cp /usr/bin/wol/wol.service /etc/systemd/system
```

Enable wol.service
```bash
systemctl enable wol.service
```

Start wol.service
```bash
systemctl start wol.service
```

You can check it's execution by running:
```bash
systemctl status wol.service
```

To restart the service:
```bash
systemctl restart wol.service
```