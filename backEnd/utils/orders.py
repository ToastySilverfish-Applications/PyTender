####Ordering Functions

##imports
import os, subprocess
from configBuilder import cb_getConfDict
import shutil


##Get Config Info
conf = cb_getConfDict()


def get_readyFiles():
  orders = []
  for roots,dirs,files in os.walk(conf['path']['orders_ready']):
    for filename in files:
      orders.append(filename)
  orders.sort()
  return orders


def get_pendingFiles():
  orders = []
  for roots,dirs,files in os.walk(conf['path']['orders_pending']):
    for filename in files:
      orders.append(filename)
  orders.sort()
  return orders


def check_readyToMake(orderNum):
  orders = get_readyFiles()
  if len(orders) == 0:
    return False
  elif (orders[0])[:-4] != orderNum:
    return False
  elif (orders[0])[:-4] == orderNum:
    return True
  else:
    return False
    

def check_readyEmpty():
  orders = get_readyFiles()
  if len(orders) == 0:
    return True
  else:
    return False


def check_pendingEmpty():
  orders = get_pendingFiles()
  if len(orders) == 0:
    return True
  else:
    return False
 
 
def move_pendingToReady():
  if check_pendingEmpty():
    pass
  else:
    orders = get_pendingFiles()
    shutil.move(conf['path']['orders_pending'] + orders[0].strip(), conf['path']['orders_ready'] + orders[0].strip())
  
  
def delete_finOrder(orderNum):
  os.remove(conf['path']['orders_ready'] + orderNum + ".txt")
  
  
def create_order(orderNum, order):
  if check_readyEmpty():
    fh = open(conf['path']['orders_ready'] + orderNum + ".txt", 'w')
    fh.write(order.strip())
    fh.close()
    if os.path.exists(conf['path']['orders_ready'] + orderNum + ".txt"):
      return True
    else:
      return False
  else:
    fh = open(conf['path']['orders_pending'] + orderNum + ".txt", 'w')
    fh.write(order.strip())
    fh.close()
    if os.path.exists(conf['path']['orders_pending'] + orderNum + ".txt"):
      return True
    else:
      return False 
      
      
def order_makeOrder(orderNum):
  if os.path.exists(conf['path']['orders_ready'] + orderNum + ".txt"):
    fh = open(conf['path']['orders_ready'] + orderNum + ".txt",'r')
    drink = fh.read().strip()
    fh.close()
    subprocess.Popen(['python','/usr/local/lib/PyTender/orders/recipes/' + drink.upper() + '.py'],shell=False).wait()
    delete_finOrder(orderNum)
    move_pendingToReady()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  