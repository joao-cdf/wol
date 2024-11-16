# Utility functions go here.

import yaml
import os
from datetime import datetime

def read_file():
  with open('machines.yml', 'r') as file:
    return yaml.safe_load(file)

def get_time():
  now = datetime.now()
  return now.strftime('%H:%M:%S')

def ping(ip):
  return os.system('ping {} -c 2'.format(ip))