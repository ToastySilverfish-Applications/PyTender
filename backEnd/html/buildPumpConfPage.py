##Builds the HTML for the Pump Config Page

##Imports
from htmlConf import *

##Get Conf Dict
confDict = cb_getConfDict()

##Set Paths
confPath = confDict['path']['python_conf'] + "ingredients.txt"
wwwPath = confDict['path']['www_html'] + "pumpConf.html"

##Read Ingredients into list
fh = open(confPath,'r')
ingList = fh.readlines()
fh.close()
ingList.sort()

##Create the rest of the html
htmlString = htmlConf_pageTop + '<body>' + '\n'
htmlString = htmlString + '\t<button class="back2main" id="b_m" type="button" onclick="gotoMain()">Main</button>' + '/n'
htmlString = htmlString + '\t<div id="pumpConfLoadSpinner" class="loader_one"></div>' + '\n'
htmlString = htmlString + '\t<div class="pump_conf_div" >' + '\n'
for i in range(6):
  htmlString = htmlString + '\t\t<div class="center2">' + '\n'
  htmlString = htmlString + '\t\t\t<strong class="midFont">Pump ' + (str(i + 1)) + '</strong>' + '\n'
  htmlString = htmlString + '\t\t\t<select id="ps' + (str(i + 1)) + '" name="pump' + (str(i + 1)) + '" class="pumpConfPage midFont">' + '\n'
  htmlString = htmlString + '\t\t\t\t<option value="NONE">NONE</option>' + '\n'
  for k in range(len(ingList)):
    htmlString = htmlString + '\t\t\t\t<option value="' + ingList[k].strip().upper() + '">' + ingList[k].strip().upper() + '</option>' + '\n'
  htmlString = htmlString + '\t\t\t</select>' + '\n'
  htmlString = htmlString + '\t\t</div>' + '\n'
htmlString = htmlString + '<button class="pumpSub center midFont" id="pumpConfSub" type="button" onclick="submitPumps()">Save</button>' + '\n'
htmlString = htmlString + '\t</div>' + '\n'
htmlString = htmlString + '</body>\n</html>'

fh = open(wwwPath,'w')
fh.write(htmlString)
fh.close()






