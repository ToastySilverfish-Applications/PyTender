####Control the pumps

##Imports
import RPi.GPIO as GPIO
import time
from configBuilder import cb_getConfDict

##Get Conf
conf = cb_getConfDict()

##Set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

##Variables
testSleepTime = 2

def run_pumpTester(pumpNum):
  if pumpNum == 1:
    run_pump1()
    time.sleep(testSleepTime)
    stop_pump1()
  elif pumpNum == 2:
    run_pump2()
    time.sleep(testSleepTime)
    stop_pump2()
  elif pumpNum == 3:
    run_pump3()
    time.sleep(testSleepTime)
    stop_pump3()
  elif pumpNum == 4:
    run_pump4()
    time.sleep(testSleepTime)
    stop_pump4()
  elif pumpNum == 5:
    run_pump5()
    time.sleep(testSleepTime)
    stop_pump5()
  elif pumpNum == 6:
    run_pump6()
    time.sleep(testSleepTime)
    stop_pump6()
    
    
def run_pump1():
  GPIO.setup(conf['pin']['pump_one'],GPIO.OUT)
  
  
def run_pump2():
  GPIO.setup(conf['pin']['pump_two'],GPIO.OUT)
  
  
def run_pump3():
  GPIO.setup(conf['pin']['pump_three'],GPIO.OUT)


def run_pump4():
  GPIO.setup(conf['pin']['pump_four'],GPIO.OUT)


def run_pump5():
  GPIO.setup(conf['pin']['pump_five'],GPIO.OUT)


def run_pump6():
  GPIO.setup(conf['pin']['pump_six'],GPIO.OUT)


def stop_pump1():
  GPIO.setup(conf['pin']['pump_one'],GPIO.IN)
  
  
def stop_pump2():
  GPIO.setup(conf['pin']['pump_two'],GPIO.IN)
  
  
def stop_pump3():
  GPIO.setup(conf['pin']['pump_three'],GPIO.IN)


def stop_pump4():
  GPIO.setup(conf['pin']['pump_four'],GPIO.IN)


def stop_pump5():
  GPIO.setup(conf['pin']['pump_five'],GPIO.IN)


def stop_pump6():
  GPIO.setup(conf['pin']['pump_six'],GPIO.IN)
  
def stop_allPumps():
  GPIO.setup(conf['pin']['pump_one'],GPIO.IN)
  GPIO.setup(conf['pin']['pump_two'],GPIO.IN)
  GPIO.setup(conf['pin']['pump_three'],GPIO.IN)
  GPIO.setup(conf['pin']['pump_four'],GPIO.IN)
  GPIO.setup(conf['pin']['pump_five'],GPIO.IN)
  GPIO.setup(conf['pin']['pump_six'],GPIO.IN)