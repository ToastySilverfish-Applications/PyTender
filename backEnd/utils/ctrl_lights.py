####Control the lights

##Imports
import RPi.GPIO as GPIO
import time
from configBuilder import cb_getConfDict

##Get Conf
conf = cb_getConfDict()

##Set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(conf['pin']['led_red'],GPIO.OUT)

##Variables
testSleepTime = 1

def run_lightTester(color):
  if color == "red":
    light_red()
    time.sleep(testSleepTime)
    dark_red()
    time.sleep(testSleepTime)
    light_red()
    time.sleep(testSleepTime)
    dark_red()
  elif color == "green":
    light_green()
    time.sleep(testSleepTime)
    dark_green()
    time.sleep(testSleepTime)
    light_green()
    time.sleep(testSleepTime)
    dark_green()  
    
    
def light_red():
  GPIO.output(conf['pin']['led_red'],GPIO.HIGH)


def dark_red():
  GPIO.output(conf['pin']['led_red'],GPIO.LOW)


# def light_green():
  # GPIO.output(conf['pin']['led_green'],GPIO.HIGH)


# def dark_green():
  # GPIO.output(conf['pin']['led_green'],GPIO.LOW)