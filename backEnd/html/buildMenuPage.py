##This builds the Main Menu page based on the selections for the Pump Configurations

##Imports
from htmlConf import *

##Get Conf Dict
confDict = cb_getConfDict()

##Set Paths
confPath = confDict['path']['python_conf'] + "menu.txt"
wwwPath = confDict['path']['www_html'] + "makeDrink.html"

##Read Makeable drinks into list
fh = open(confPath,'r')
drinkList = fh.readlines()
fh.close()
drinkList.sort()

##Create rest of html
htmlString = htmlConf_pageTop + '<body>' + '\n'
htmlString = htmlString + '\t<button class="back2main" id="b_m" type="button" onclick="gotoMain()">Main</button>' + '/n'
htmlString = htmlString + '\t<div class="modal_drinkConf" id="modal_dc">' + '\n'
htmlString = htmlString + '\t\t<strong><p id="modal_drink">Create Order for Drink?</p></strong>' + '\n'
htmlString = htmlString + '\t\t<button class="mkdrinkMod-button" id="mkdrink_confBut" type="button" onclick="confDrink(1)">Make Drink</button>' + '\n'
htmlString = htmlString + '\t\t<button class="mkdrinkMod-button" id="mkdrink_canBut" type="button" onclick="confDrink(0)">Cancel</button>' + '\n'
htmlString = htmlString + '\t\t<strong id="drinkSubmit" style="display:none;"></strong>' + '\n'
htmlString = htmlString + '\t</div>' + '\n'

htmlString = htmlString + '\t<div class="modal_drinkOrdered" id="modal_ordered">' + '\n'
htmlString = htmlString + '\t\t<strong><p>Drink Ordered</p></strong>' + '\n'
htmlString = htmlString + '\t\t<strong><p id="modal_order_num"></p></strong>' + '\n'
htmlString = htmlString + '\t\t<strong><p id="modal_status"></p></strong>' + '\n'
htmlString = htmlString + '\t\t<button class="mkdrinkPour-button" id="modal_pourButton" type="button" onclick="pourDrink()">Pour</button>' + '\n'
htmlString = htmlString + '\t</div>' + '\n'


##Create Dynamic HTML
for i in range(len(drinkList)):
  drinkRecipeName = (drinkList[i].replace(" ","_")).upper()
  htmlString = htmlString + '\t<button id="' + drinkList[i].strip() + '" class="main-button center" type="button" onclick="loadConfirm(\'' + (drinkRecipeName).strip() + '\')">' + (drinkList[i]).strip() + '</button>' + '\n'

fh = open(wwwPath,'w')
fh.write(htmlString)
fh.close()

