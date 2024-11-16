# wol -- Wake on LAN python mini-script

A python script that provides wake-on-lan functionality to machines within your LAN.

Service implementation of a Wake on LAN service for linux using systemd.

The program uses the file **machines.yml** to load the information about the machines (The file must be created with the correct info).

Example -- **machines.yml**
```yml
# List of servers to be added to the wakeonlan program.

machine-1:
  name: 'machine-1'
  ip:   '192.168.1.XXX'
  mac:  'XX:XX:XX:XX:XX:XX'

machine-2:
  name: 'machine-2'
  ip:   '192.168.1.XXX'
  mac:  'XX:XX:XX:XX:XX:XX'
```

The program reads **machines.yml** every minute and sends a ping for each machine. A ping is sent to each machine and if the ping fails then it sends a magic packet to the mac address of the machine that failed to answer the ping.

# Installation instructions

Copy the project to /usr/bin/
```bash
cp -r /path/to/project/wol /usr/bin/
```

Create virtual environment
```bash
cd /usr/bin/wol
python3 -m venv virtual
```

Install dependencies
```bash
cd /usr/bin/wol
source virtual/bin/activate
python -m pip install $(cat requirements.txt)
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

--

You can check if the service is running:
```bash
systemctl status wol.service
```

To restart the service:
```bash
systemctl restart wol.service
```