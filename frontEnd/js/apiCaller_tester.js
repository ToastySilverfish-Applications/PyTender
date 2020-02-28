var xhttp = new XMLHttpRequest();
var mod1 = document.getElementById("modal1")

function changeMes(mes){
  document.getElementById("modal_p").innerHTML = mes; 
  
}

function showMod(){
  document.getElementById("modal1").style.display = "block";
  
}

function closeMod(){
  document.getElementById("modal1").style.display = "none";
  
}


function callAPI(endpoint){
  xhttp.open("GET","http://192.168.1.200:5000/testers/" + endpoint,true);
  xhttp.send(null);
  
}

function test_pump_1(){
  changeMes("Testing Pump 1");
  showMod();
  callAPI("pump_1");
  setTimeout(function(){changeMes("Test Complete");},4000);
  setTimeout(function(){closeMod();},8000);
}

function test_pump_2(){
  changeMes("Testing Pump 2");
  showMod();
  callAPI("pump_2");
  setTimeout(function(){changeMes("Test Complete");},4000);
  setTimeout(function(){closeMod();},8000);
}

function test_pump_3(){
  changeMes("Testing Pump 3");
  showMod();
  callAPI("pump_3");
  setTimeout(function(){changeMes("Test Complete");},4000);
  setTimeout(function(){closeMod();},8000);
}

function test_pump_4(){
  changeMes("Testing Pump 4");
  showMod();
  callAPI("pump_4");
  setTimeout(function(){changeMes("Test Complete");},4000);
  setTimeout(function(){closeMod();},8000);
}

function test_pump_5(){
  changeMes("Testing Pump 5");
  showMod();
  callAPI("pump_5");
  setTimeout(function(){changeMes("Test Complete");},4000);
  setTimeout(function(){closeMod();},8000);
}

function test_pump_6(){
  changeMes("Testing Pump 6");
  showMod();
  callAPI("pump_6");
  setTimeout(function(){changeMes("Test Complete");},4000);
  setTimeout(function(){closeMod();},8000);
}

function test_light_red(){
  changeMes("Testing Red Light");
  showMod();
  callAPI("light_red");
  setTimeout(function(){changeMes("Test Complete");},4000);
  setTimeout(function(){closeMod();},8000);
}