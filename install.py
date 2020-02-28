##Pytender installation script

##Imports
import subprocess
import getpass
import shutil
import sys
import os
import time

##variables
version = "1.00.00"
dependenciesMet = True

if getpass.getuser() != "root":
  sys.stdout.write("\nMust be root\n")
else:
  pass

sys.stdout.write("\nPyTender Installation\n")
sys.stdout.write("\tVersion " + version +"\n")
sys.stdout.write("Checking dependencies...\n")
##Check for flask
if subprocess.call('pip list | grep Flask',shell=True,stdout=open(os.devnull,'w')) == 0:
  sys.stdout.write("\tFlask Installed:\t\tTrue\n"
else:
  sys.stdout.write("\tFlask Installed:\t\tFalse\n"
  dependenciesMet = False
##Check for flaskcors
if subprocess.call('pip list | grep Flask-Cors',shell=True,stdout=open(os.devnull,'w')) == 0:
  sys.stdout.write("\tFlask-Cors Installed:\t\tTrue\n"
else:
  sys.stdout.write("\tFlask-Cors Installed:\t\tFalse\n"
  dependenciesMet = False  
##check for apache2
if subprocess.call('ls /etc/apache2',shell=True,stdout=open(os.devnull,'w')) == 0:
  sys.stdout.write("\tApache2 Installed:\t\tTrue\n"
else:
  sys.stdout.write("\tApache2 Installed:\t\tFalse\n"
  dependenciesMet = False  
##Check for apache2 base dir
if subprocess.call('ls /var/www/html',shell=True,stdout=open(os.devnull,'w')) == 0:
  sys.stdout.write("\t/var/www/html Exists:\t\tTrue\n"
else:
  sys.stdout.write("\t/var/www/html Exists:\t\tFalse\n"
  dependenciesMet = False  
##Go-nogo
if not dependenciesMet:
  sys.stdout.write("Your system does not meet one or more requirements to install")
  sys.exit(0)
else:
  sys.stdout.write("Creating directories and copying files...\n")
  ##Create Dirs
  os.mkdir("/etc/PyTender")
  os.mkdir("/usr/local/PyTender")
  os.mkdir("/usr/local/PyTender/api")
  os.mkdir("/usr/local/PyTender/html")
  os.mkdir("/usr/local/PyTender/orders")
  os.mkdir("/usr/local/PyTender/pending")
  os.mkdir("/usr/local/PyTender/ready")
  os.mkdir("/usr/local/PyTender/recipies")
  os.mkdir("/usr/local/PyTender/utils")
  os.mkdir("/var/www/html/html")
  os.mkdir("/var/www/html/css")
  os.mkdir("/var/www/html/js")
  ##Copy over conf files
  shutil.copy('./backEnd/drinks.txt','/etc/PyTender/drinks.txt')
  shutil.copy('./backEnd/info.txt','/etc/PyTender/info.txt')
  shutil.copy('./backEnd/ingredients.txt','/etc/PyTender/ingredients.txt')
  shutil.copy('./backEnd/paths.txt','/etc/PyTender/paths.txt')
  shutil.copy('./backEnd/pins.txt','/etc/PyTender/pins.txt')
  ##Copy api
  shutil.copy('./backEnd/api/bartenderAPI.py','/usr/local/PyTender/api/bartenderAPI.py')
  ##Copy HTML Builders
  shutil.copy('./backEnd/html/htmlConf.py','/usr/local/PyTender/html/htmlConf.py')
  shutil.copy('./backEnd/html/buildMenuPage.py','/usr/local/PyTender/html/buildMenuPage.py')
  shutil.copy('./backEnd/html/buildPumpConfPage.py','/usr/local/PyTender/html/buildPumpConfPage.py')
  ##Copy drink files
  c = subprocess.call('cp ./backEnd/orders/recipes/* /usr/local/PyTender/orders/recipies/*',shell=True,stdout=open(os.devnull,'w'))
  ##Copy Utils
  c = subprocess.call('cp ./backEnd/utils* /usr/local/PyTender/utils/*',shell=True,stdout=open(os.devnull,'w'))
  ##Copy other python
  shutil.copy('./backEnd/orderWatch.py','/usr/local/PyTender/orderWatch.py')
  shutil.copy('./backEnd/PyTenderCmd.py','/usr/local/PyTender/PyTenderCmd.py')
  ##Copy WEB
  shutil.copy('./frontEnd/index.html','/var/www/html/index.html')
  c = subprocess.call('cp ./frontEnd/html/* /var/www/html/html/*',shell=True,stdout=open(os.devnull,'w'))
  c = subprocess.call('cp ./frontEnd/css/* /var/www/html/css/*',shell=True,stdout=open(os.devnull,'w'))
  c = subprocess.call('cp ./frontEnd/js/* /var/www/html/js/*',shell=True,stdout=open(os.devnull,'w'))
  ##Copy Profile
  shutil.copy('./backEnd/profile/pytender.sh','/etc/profile.d/pytender.sh')
  ##Copy Services
  shutil.copy('./backEnd/services/pytender-api.service','/lib/systemd/system/pytender-api.service')
  shutil.copy('./backEnd/services/pytender-ow.service','/lib/systemd/system/pytender-ow.service')
  ##Set permissions
  chmod = subprocess.call('chmod -R 755 /etc/PyTender',shell=True,stdout=open(os.devnull,'w'))
  chmod = subprocess.call('chmod -R 755 /usr/local/PyTender',shell=True,stdout=open(os.devnull,'w'))
  chmod = subprocess.call('chmod -R 755 /var/www/html',shell=True,stdout=open(os.devnull,'w'))
  sys.stdout.write("Reloading Services...\n")
  reload = subprocess.call('systemctl daemon-reload',shell=True,stdout=open(os.devnull,'w'))
  sys.stdout.write("Enabling Services...\n")
  enable = subprocess.call('systemctl enable pytender-api',shell=True,stdout=open(os.devnull,'w'))
  enable = subprocess.call('systemctl enable pytender-ow',shell=True,stdout=open(os.devnull,'w'))
  sys.stdout.write("Starting Services...\n")
  enable = subprocess.call('systemctl start pytender-api',shell=True,stdout=open(os.devnull,'w'))
  enable = subprocess.call('systemctl start pytender-ow',shell=True,stdout=open(os.devnull,'w'))
  time.sleep(10)
  sys.stdout.write("Checking Services...\n")
  allUp = True
  if subprocess.call('systemctl status pytender-api | grep running',shell=True,stdout=open(os.devnull,'w')) == 0:
    sys.stdout.write("API Running...\n")
  else:
    sys.stdout.write("API Not Running...\n")
    allUp = False
  if subprocess.call('systemctl status pytender-ow | grep running',shell=True,stdout=open(os.devnull,'w')) == 0:
    sys.stdout.write("OrderWatch Running...\n")
  else:
    sys.stdout.write("OrderWatch Not Running...\n")
    allUp = False
  if not allUp:
    sys.stdout.write("One or both services did not start.\n")
    sys.stdout.write("Please run the following commands and check the output for failues\n")
    sys.stdout.write("\tsystemctl status pytender-api\n")
    sys.stdout.write("\tsystemctl status pytender-ow\n")
  else:
    pass
  sys.stdout.write("Cleaning up...\n")
  r = subprocess.call('rm -r ./backEnd',shell=True,stdout=open(os.devnull,'w'))
  r = subprocess.call('rm -r ./frontEnd',shell=True,stdout=open(os.devnull,'w'))
  r = subprocess.call('rm -r ./install.py',shell=True,stdout=open(os.devnull,'w'))
  sys.stdout.write("Install finished...\n")
  


