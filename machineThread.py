import threading
import time
import logging
from machine import Machine
from wakeonlan import send_magic_packet
from utils import ping, get_time

logging.basicConfig (
  filename='./wol.log',
  filemode='a', 
  format='%(name)s - %(levelname)s - %(message)s',
  level=logging.DEBUG
)

class machineThread():

  def __init__(self, m: Machine):
    self.machine = Machine(m.name, m.ip, m.mac)
    self.initThread()

  def threadFunction(self):
    print("Thread starting for server " + self.machine.name)

    logging.info('%s -- PINGING -- , %s', self.machine.name, get_time())
    if ping(self.machine.ip) != 0:
      try:
        print(self.machine.mac)
        logging.info('%s -- SENDING MAGIC PACKET -- , %s', self.machine.name, get_time())
        send_magic_packet(macs= self.machine.mac)
      except:
        logging.error('%s -- ERROR SENDING MAGIC PACKET -- , %s', self.machine.name , get_time())


    time.sleep(5)
    print("Thread stopping for server " + self.machine.name)

  def initThread(self):
    td = threading.Thread(target= self.threadFunction)
    td.start()
