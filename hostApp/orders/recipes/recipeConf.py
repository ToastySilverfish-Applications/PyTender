###This controls and provides the funcitons used within the various drink scripts.
###to work the various pumps and pour the drinks.

import sys, time, subprocess
sys.path.append("/usr/local/lib/PyTender/utils")
from ctrl_pumps import *
from configBuilder import cb_getConfDict
from configBuilder import cb_getPumps
conf = cb_getConfDict()
pumps = cb_getPumps()

def pour(info):
  ##Lets say 1 second per 10 ml
  ##Init i#p
  i1p,i2p,i3p,i4p,i5p,i6p = 0,0,0,0,0,0
  i1t,i2t,i3t,i4t,i5t,i6t = 0,0,0,0,0,0
  totalRun = 0
  runLeft = 0
  allParts = []
  validParts = []
  timer = 0
  mlPerSec = 10
  
  ##Figure out the timing for each pump run
  if len(info) >= 1:
    i1p = pumps[info['ing1']['name']]
    i1t = info['ing1']['ml'] / mlPerSec
  if len(info) >= 2:
    i2p = pumps[info['ing2']['name']]
    i2t = info['ing2']['ml'] / mlPerSec
  if len(info) >= 3:
    i3p = pumps[info['ing3']['name']]
    i3t = info['ing3']['ml'] / mlPerSec
  if len(info) >= 4:
    i4p = pumps[info['ing4']['name']]
    i4t = info['ing4']['ml'] / mlPerSec
  if len(info) >= 5:
    i5p = pumps[info['ing5']['name']]
    i5t = info['ing5']['ml'] / mlPerSec
  if len(info) >= 6:
    i6p = pumps[info['ing6']['name']]
    i6t = info['ing6']['ml'] / mlPerSec
  
  ##Get the total runtime
  tmp = [i1t,i2t,i3t,i4t,i5t,i6t]
  totalRun =  max(tmp)
  allParts = [[i1t,i1p],[i2t,i2p],[i3t,i3p],[i4t,i4p],[i5t,i5p],[i6t,i6p]]
  
  ##Figure out which pumps are actually being used for this recipe
  for i in range(6):
    if allParts[i][0] != 0:
      validParts.append([allParts[i][0],allParts[i][1]])
    else:
      pass
  
  try:
    ##Kick all the used pumps on
    for i in range(len(validParts)):
      subprocess.Popen(['python', '/home/pytender/util/pump' + str(validParts[i][1]) + '.py','on'])
  
    ##Shut down all the pumps as their experation approaches
    while timer < totalRun:
      for i in range(len(validParts)):
        if validParts[i][0] <= timer:
          subprocess.Popen(['python', '/home/pytender/util/pump' + str(validParts[i][1]) + '.py','off'])
        else:
          pass
      time.sleep(1)
      timer = timer + 1
  except:  
    pass
    
  ##Safey shutoff for all pumps if there is a failure
  for i in range(len(validParts)):
    subprocess.Popen(['python', '/home/pytender/util/pump' + str(validParts[i][1]) + '.py','off'])
  
  
