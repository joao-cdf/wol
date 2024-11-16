import os
import time
from utils import read_file
from datetime import datetime
from wakeonlan import send_magic_packet
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

  #send_magic_packet('40:B0:34:1D:EE:54')
  #td = machineThread(m = Machine('dalaran', '192.168.10.200', '40:B0:34:1D:EE:54'))



# dobby = Machine('Dobby', '192.168.10.100', '20:89:84:B4:17:9F')


# logging.basicConfig(filename='./wol.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# while(True):
#  if ping(dobby.ip) != 0:
#   try:
#    send_magic_packet(dobby.mac)
#   except:
#    logging.error('--ERROR SENDING MAGIC PACKET-- , %s', get_time())
#   time.sleep(60)
#   while(LOOPBACK):
#    code = ping(dobby.ip)
#    if code == 0:
#     logging.info('--MACHINE %s UP-- , %s', dobby.name, get_time())
#     LOOPBACK = False
#    else:
#     logging.warning('--MACHINE %s DOWN RESENDING PACKET-- , %s', dobby.name, get_time())
#     try:
#      send_magic_packet(dobby.mac)
#     except:
#      logging.error('--ERROR SENDING MAGIC PACKET-- , %s'. get_time())
#     time.sleep(LOOPBACK_TIME)
#  time.sleep(TIME)
