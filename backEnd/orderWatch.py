###Order watch checks the ready folder periodically and removes ready orders that are not being poured

##Imports
import sys
import os
import shutil
import logging
import time

##Import Bartender Modules
sys.path.append("/usr/local/PyTender/utils")
from orders import check_readyEmpty
from orders import check_pendingEmpty
from orders import move_pendingToReady
from configBuilder import cb_getConfDict

##Logging Config
logging.basicConfig(filename="/var/log/PyTender/error.log",level=logging.DEBUG)

##Variables
checkInterval = 60 ##Seconds - Default is 1 minute
maxOrderTime = 300 ##Seconds - Default is 5 minutes
orderWatchEnd = False
conf = cb_getConfDict()

while not orderWatchEnd:
  if not check_readyEmpty():
    if not check_pendingEmpty():
      orderTime = time.time() - maxOrderTime
      for roots, dirs, files in os.walk(conf['path']['orders_ready']):
        for file in files:
          fpath = os.path.join(root,file)
          stat = os.stat(fpath)
          if stat.st_mtime <= orderTime:
            os.remove(file)
          else:
            pass
      move_pendingToReady()
    else:
      pass
  else:
    pass
  time.sleep(checkInterval)
  
  