###Control Hub for PyTender Application

##Imports
import argparse
import subprocess

##Help Message
helpMes = (
"PYTENDER\n\n"
"Actions:\n\n"
"\tstart:        Start the PyTender API and OrderWatch Services\n"
"\tstop:         Stop the PyTender API and OrderWatch Services\n"
"\tstatus:       Report the statuses of the PyTender API and OrderWatch Services\n"
"\tstart-api:    Start the PyTender API Service\n"
"\tstop-api:     Stop the PyTender API Service\n"
"\tstatus-api:   Report the statuses of the PyTender API Service\n"
"\tstart-ow:     Start the PyTender OrderWatch Service\n"
"\tstop-ow:      Stop the PyTender OrderWatch Service\n"
"\tstatus-ow:    Report the statuses of the PyTender OrderWatch Service\n"
"\tinstallPath:  Report the installation paths of PyTender\n"
"\tpins:         Report information about the GPIO pin setup for PyTender\n"
"\tinfo:         Print PyTender Infomation File\n"
"\tuninstall:    Remove PyTender from your system\n"
"\thelp:         This Message\n"
)


def getParms():
  parser = argparse.ArgumentParser(add_help=False)
  ##Main Positional Arguement
  parser.add_argument("action")
  return parser.parse_args()
  

def startApi():
  try:
    call = subprocess.call(['systemctl','start','pytender-api'],shell=False)
    if call != 0:
      sys.stdout.write("Failed to start API")
    else:
      pass
  except Exception as e:
    sys.stdout.write("Failed to start API.  Exception Occured")
    sys.stdout.write(str(e))
    
    
def startOW():
  try:
    call = subprocess.call(['systemctl','start','pytender-ow'],shell=False)
    if call != 0:
      sys.stdout.write("Failed to start OrderWatch")
    else:
      pass
  except Exception as e:
    sys.stdout.write("Failed to start OrderWatch.  Exception Occured")
    sys.stdout.write(str(e))
    
    
def stopApi():
  try:
    call = subprocess.call(['systemctl','stop','pytender-api'],shell=False)
    if call != 0:
      sys.stdout.write("Failed to stop API")
    else:
      pass
  except Exception as e:
    sys.stdout.write("Failed to stop API.  Exception Occured")
    sys.stdout.write(str(e))
    
    
def stopOW():
  try:
    call = subprocess.call(['systemctl','stop','pytender-ow'],shell=False)
    if call != 0:
      sys.stdout.write("Failed to stop OrderWatch")
    else:
      pass
  except Exception as e:
    sys.stdout.write("Failed to stop OrderWatch.  Exception Occured")
    sys.stdout.write(str(e))
  
  
def statusApi():
  try:
    call = subprocess.check_output(['systemctl','status','pytender-api'],shell=False)
    sys.stdout.write("\nPyTender API Status\n\n")
    sys.stdout.write(str(call))
  except Exception as e:
    sys.stdout.write("Failed to check API.  Exception Occured")
    sys.stdout.write(str(e))
    
    
def statusOW():
  try:
    call = subprocess.check_output(['systemctl','status','pytender-ow'],shell=False)
    sys.stdout.write("\nPyTender OrderWatch Status\n\n")
    sys.stdout.write(str(call))
  except Exception as e:
    sys.stdout.write("Failed to check OrderWatch.  Exception Occured")
    sys.stdout.write(str(e))
    
    
def installationPaths():
  sys.stdout.write("\nPyTender Installation Paths:\n")
  sys.stdout.write("\t- /etc/PyTender")
  sys.stdout.write("\t- /usr/local/PyTender")
  sys.stdout.write("\t- /www/var/html")
  sys.stdout.write("\t- /var/log/PyTender")
  
  
def pinInfo():
  sys.path.append("/usr/local/PyTender/utils")
  from configBuilder import getPinInfo
  pins = getPinInfo()
  for i in range(len(pins)):
    p = pins[i].split(":")
    sys.stdout.write(p[0] + "at GPIO:\t\t" + p[1])
    
    
def info():
  fh = open("/etc/PyTender/info.txt")
  i = fh.read()
  fh.close()
  sys.stdout.write("\n" + i + "\n")


def uninstallPyTender():
  ##Add uninstall code later
  
  
def showHelp():
  sys.stdout.write("\n" + helpMes + "\n")
  
  
def main():
  parm = getParms()
  if parm == "start":
    startApi()
    startOW()
  elif parm == "stop":
    stopApi()
    stopOW()    
  elif parm == "status":
    statusApi()
    statusOW()      
  elif parm == "start-api":
    startApi()
  elif parm == "start-ow":
    startOW()    
  elif parm == "stop-api":
    stopApi()
  elif parm == "stop-ow":
    stopOW()    
  elif parm == "status-api":
    statusApi()
  elif parm == "status-ow":
    statusOW()      
  elif parm == "installPath":
    installationPaths()      
  elif parm == "pins":
    pinInfo()      
  elif parm == "info":
    info()          
  elif parm == "uninstall":
    uninstallPyTender()      
  elif parm == "help":
    showHelp()      
  else:
    sys.stdout.write("Invalid Option")
    showHelp()