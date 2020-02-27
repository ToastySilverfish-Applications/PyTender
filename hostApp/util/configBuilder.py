##Build and provides acces to conf dictonary for application use

def getPathInfo():
  fh = open("/etc/PyTender/paths.txt","r")
  tmp = fh.readlines()
  fh.close()
  return tmp


def getPinInfo():
  fh = open("/etc/PyTender/pins.txt","r")
  tmp = fh.readlines()
  fh.close()
  return tmp


def cb_getConfDict():
  pathInfo = getPathInfo()
  pinInfo = getPinInfo()
  confDict = {}
  pathDict = {}
  pinDict = {}
  for index in range(len(pathInfo)):
    pair = pathInfo[index].split(':')
    pathDict[pair[0].strip()] = pair[1].strip()
  for index in range(len(pinInfo)):
    pair = pinInfo[index].split(':')
    pinDict[pair[0].strip()] = int(pair[1].strip())
  confDict['path'] = pathDict
  confDict['pin'] = pinDict
  return confDict
  
  
def buildPumpConfFile(p1Drink,p2Drink,p3Drink,p4Drink,p5Drink,p6Drink,conf):
  fh = open(conf['path']['python_conf'] + "pumps.txt",'w')
  fh.write(p1Drink + ":1\n")
  fh.write(p2Drink + ":2\n")
  fh.write(p3Drink + ":3\n")
  fh.write(p4Drink + ":4\n")
  fh.write(p5Drink + ":5\n")
  fh.write(p6Drink + ":6")
  fh.close()


def cb_getPumps():
  conf = cb_getConfDict()
  fh = open(conf['path']['python_conf'] + "pumps.txt",'r')
  tmp = fh.readlines()
  fh.close()
  pumpDict = {}
  for index in range(len(tmp)):
    pconf = tmp[index].split(":")
    pumpDict[(pconf[0].strip()).upper()] = int(pconf[1].strip())
  return pumpDict
  
def cb_createMenuFile():
  outString = ""
  conf = cb_getConfDict()
  pumps = cb_getPumps().keys()
  print pumps
  fh = open(conf['path']['python_conf'] + "drinks.txt",'r')
  drinkFile = fh.readlines()
  fh.close()
  for i in range(len(drinkFile)):
    found = True
    tmp = drinkFile[i].split("|")
    cnt = 1
    while cnt < len(tmp):
      print tmp[cnt].strip()
      if tmp[cnt].strip().upper() not in pumps:
        found = False
      cnt = cnt + 1
    if found:
      outString = outString + tmp[0] + "\n"
  fh = open(conf['path']['python_conf'] + "menu.txt",'w')
  fh.write(outString)
  fh.close()
  
  
  