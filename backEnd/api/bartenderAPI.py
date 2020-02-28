####FLASK API FOR PyTender
##This is the main interaction API code for PyTender
##It is advised to not edit anything within this file
##The javascript for the front end expects that this api is available at port 5000.  
###If this is changed, javascript will also need to be changed.

##Imports
from flask import Flask, jsonify, request
from flask_cors import CORS
import RPi.GPIO as GPIO
import time
import sys
import os
import shutil
import logging

##Import Bartender Modules
sys.path.append("/usr/local/PyTender/utils")
sys.path.append("/usr/local/PyTender/orders/recipes")
from configBuilder import cb_getConfDict
from configBuilder import cb_createMenuFile
from orders import *
from ctrl_pumps import *
from ctrl_lights import *

##Logging Conf
logging.basicConfig(filename="/var/log/PyTender/error.log",level=logging.DEBUG)

##Variables
orderNum = 0000
app = Flask(__name__)
CORS(app)
hostIP = '0.0.0.0'
portNum = 5000

##GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

##Get Config Info
conf = cb_getConfDict()

####New Run Setup Code
##Clear orders from last run
try:
  for roots,dirs,files in os.walk(conf['path']['orders_ready']):
    for f in files:
      os.remove(os.path.join(root,f))  
except Exception as e:
  logging.error("Failed to clear ready orders")
  logging.error(str(e))
  pass
try:
  for roots,dirs,files in os.walk(conf['path']['orders_pending']):
    for f in files:
      os.remove(os.path.join(root,f))  
except Exception as e:
  logging.error("Failed to clear pending orders")
  logging.error(str(e))
  pass
try:
  for roots,dirs,files in os.walk(conf['path']['www_orders']):
    for f in files:
      os.remove(os.path.join(root,f))  
except Exception as e:
  logging.error("Failed to clear www orders")
  logging.error(str(e))
  pass
##Clear pump and menu configs
try:
  os.remove(conf['path']['python_conf'] + "pumps.txt")
except Exception as e:
  logging.error("Failed to pumps.txt")
  logging.error(str(e))
  pass
try:
  os.remove(conf['path']['www_orders'] + "menu.txt")
except Exception as e:
  logging.error("Failed to menu.txt")
  logging.error(str(e))
  pass
try:
  os.remove(conf['path']['www_html'] + "pumpConf.html")
except Exception as e:
  logging.error("Failed to pumpConf.html")
  logging.error(str(e))
  pass
####Clear build time html

##Build pump conf choices
os.system("python " + conf['path']['python_html'] + "buildPumpConfPage.py")

####API Functions
@app.route('/conf/setPumpConf', methods=['GET'])
def createPumpConfFile():
  ##Pump config page maker.  Creates config file based on user selection on pumpConf.html
  ##Passed in values
  parser = request.args
  pc1=parser['p1']
  pc2=parser['p2']
  pc3=parser['p3']
  pc4=parser['p4']
  pc5=parser['p5']
  pc6=parser['p6']
  ##check fo duplicate entries
  nodups = [pc1,pc2,pc3,pc4,pc5,pc6]
  nodups = filter(lambda a: a != "NONE", nodups)
  if len(nodups) != len(set(nodups)):
    return "No Duplicate Pumps Allowed"
  else:
    pass
  ####Create config file
  fh = open(conf['path']['python_conf'] + "pumps.txt",'w')
  fh.write(pc1 + ':1\n' + pc2 + ':2\n' + pc3 + ':3\n' + pc4 + ':4\n' + pc5 + ':5\n' + pc6 + ':6')
  fh.close()
  time.sleep(2)
  if os.path.exists(conf['path']['python_conf'] + "pumps.txt"):
    try:
      cb_createMenuFile()
      if os.path.exists(conf['path']['python_conf'] + "menu.txt"):
        os.system("python " + conf['path']['python_html'] + "buildMenuPage.py")
      else:
        logging.error("Failed to create menu page")
        return "Failed to Create Menu"
    except Exception as e:
      logging.error("Exception occured creating menu"
      logging.error(str(e))
      return "Failed to Create Menu"
    return "Pump Conf Saved"
  else:
    logging.error("Failed to save pumpconf")
    return "Failed to Save Pump Conf"

##Orders    
@app.route('/orders/createNew', methods=['GET'])    
def createNewOrder():
  global orderNum
  parser = request.args
  ordered = parser['order']
  if create_order(str(orderNum), ordered):
    set_return = str(orderNum)
    orderNum = orderNum + 1
    return set_return
  else:
    logging.error("Failed to create new order " + orderNum)
    return "failed"

@app.route('/orders/pour', methods=['GET'])    
def makeOrder():
  parser = request.args
  number = parser['number']
  order_makeOrder(str(number))
  return "Order Made"

@app.route('/orders/check', methods=['GET'])    
def checkOrder():
  parser = request.args
  number = parser['number']
  if check_readyToMake(str(number)):
    return "True"
  else:
    return "False"
    
##Testers
@app.route('/testers/pump_1', methods=['GET'])
def test_pump_1():
  run_pumpTester(1)
  return "Test Finished"

@app.route('/testers/pump_2', methods=['GET'])
def test_pump_2():
  run_pumpTester(2)
  return "Test Finished"
  
@app.route('/testers/pump_3', methods=['GET'])
def test_pump_3():
  run_pumpTester(3)
  return "Test Finished"
  
@app.route('/testers/pump_4', methods=['GET'])
def test_pump_4():
  run_pumpTester(4)
  return "Test Finished"
  
@app.route('/testers/pump_5', methods=['GET'])
def test_pump_5():
  run_pumpTester(5)
  return "Test Finished"
  
@app.route('/testers/pump_6', methods=['GET'])
def test_pump_6():
  run_pumpTester(6)
  return "Test Finished"
  
@app.route('/testers/light_red', methods=['GET'])
def test_light_red():
  run_lightTester("red")
  return "Test Finished"


##Trigger Host
app.run(host=hostIP, port= portNum)