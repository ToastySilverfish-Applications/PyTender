// const xhttp = new XMLHttpRequest();

function showLoader(){
  document.getElementById('pumpConfLoadSpinner').style.display = "block";
}

function hideLoader(){
  document.getElementById('pumpConfLoadSpinner').style.display = "none";
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function makeCall(pumpSet){
  var pump1 = document.getElementById('ps1');
  var pump2 = document.getElementById('ps2');
  var pump3 = document.getElementById('ps3');
  var pump4 = document.getElementById('ps4');
  var pump5 = document.getElementById('ps5');
  var pump6 = document.getElementById('ps6');
  var pv1 = pump1.options[pump1.selectedIndex].value;
  var pv2 = pump2.options[pump2.selectedIndex].value;
  var pv3 = pump3.options[pump3.selectedIndex].value;
  var pv4 = pump4.options[pump4.selectedIndex].value;
  var pv5 = pump5.options[pump5.selectedIndex].value;
  var pv6 = pump6.options[pump6.selectedIndex].value;
  endpoint = "/conf/setPumpConf?";
  const xhttp = new XMLHttpRequest(),
    method = "GET",
    url = "http://192.168.1.200:5000" + endpoint + pumpSet;
  xhttp.open(method, url, false);
  xhttp.send(null);
  return xhttp.responseText;
}

async function submitPumps(){
  var pump1 = document.getElementById('ps1');
  var pump2 = document.getElementById('ps2');
  var pump3 = document.getElementById('ps3');
  var pump4 = document.getElementById('ps4');
  var pump5 = document.getElementById('ps5');
  var pump6 = document.getElementById('ps6');
  var pv1 = pump1.options[pump1.selectedIndex].value;
  var pv2 = pump2.options[pump2.selectedIndex].value;
  var pv3 = pump3.options[pump3.selectedIndex].value;
  var pv4 = pump4.options[pump4.selectedIndex].value;
  var pv5 = pump5.options[pump5.selectedIndex].value;
  var pv6 = pump6.options[pump6.selectedIndex].value;
  endpoint = "/conf/setPumpConf?";
  pumpSet = "p1=" + pv1 + "&p2=" + pv2 + "&p3=" + pv3 + "&p4=" + pv4 + "&p5=" + pv5 + "&p6=" + pv6;
  showLoader();
  document.getElementById('pumpConfSub').innerHTML = "Sending";
  await sleep(100);
  restxt = makeCall(pumpSet);
  window.alert(restxt);
  window.location.replace('main.html');
}