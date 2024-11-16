# wol -- Wake on LAN python mini-script

A python script that provides wake-on-lan functionality to machines within your LAN.

Service implementation of a Wake on LAN service for linux.
 - It checks every hour if a machine is turned on by pinging it.
 - If the ping fails it sends a magic packet to the machine, waits a minute pings it again and resends a magic pack if it still cant get a ping.
