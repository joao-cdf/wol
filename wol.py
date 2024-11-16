import time
from utils import read_file
from machineThread import machineThread
from machine import Machine

LOOPBACK = True
LOOPBACK_TIME = 30
TIME = 60

if __name__ == "__main__":

  server_list = read_file()
  while(True):
    for key, value in server_list.items():
      machineThread(m= Machine(value['name'], value['ip'], value['mac']))
    time.sleep(60)
