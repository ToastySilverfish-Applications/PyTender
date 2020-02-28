##Imports
import RPi.GPIO as GPIO
import argparse
from configBuilder import cb_getConfDict
##Get Conf
conf = cb_getConfDict()
##Set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

parser = argparse.ArgumentParser()
parser.add_argument('cmd')
args = parser.parse_args()

if args.cmd == "on":
  GPIO.setup(conf['pin']['pump_five'],GPIO.OUT) ##Pump On
else:
  GPIO.setup(conf['pin']['pump_five'],GPIO.IN)##Pump off

