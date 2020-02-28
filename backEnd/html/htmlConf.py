####This is the Conf for the main header of the dynamic HTML pages created by PyTender

##Imports
import sys
sys.path.append('/usr/local/PyTender/utils')
from configBuilder import cb_getConfDict


##Static HTML
htmlConf_pageTop = ('<!DOCTYPE html>' + '\n' +
'<html>\n<head>' + '\n' + 
'\t<title>Bartender_Main</title>' + '\n' + 
'\t<link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet">' + '\n' +
'\t<link rel="stylesheet" media="screen and (min-device-width: 500px)" type="text/css" href="../css/bartender.css">' + '\n' +
'\t<link rel="stylesheet" media="screen and (max-device-width: 500px)" type="text/css" href="../css/bartender_m.css">' + '\n' +
'\t<script type="text/javascript" src="../js/pageSwitcher.js"></script>' + '\n' +
'\t<script type="text/javascript" src="../js/pumpConf.js"></script>' + '\n' +
'\t<script type="text/javascript" src="../js/webOrders.js"></script>' + '\n' +
'</head>' + '\n')