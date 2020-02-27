
function loadConfirm(drink){
  var drinkFormatted = drink.replace(/_/g," ");
  document.curDrink = drink;
  document.getElementById('modal_drink').innerHTML = "Create drink order for<br>" + drinkFormatted;
  document.getElementById('modal_dc').style.display = "block";
}

function checkOrderReady(orderNum){
  var drinkReady = false;
  const xhttp = new XMLHttpRequest(),
    method = "GET",
    url = "http://192.168.1.200:5000" + "/orders/check?number=" + orderNum;
  while (drinkReady != true){
    xhttp.open(method, url, false);
    xhttp.send(null);
  
    if (xhttp.responseText == "True"){
      document.getElementById('modal_status').innerHTML = "Status: Ready";
      document.getElementById('modal_pourButton').style.display = "inline-block";
      drinkReady = true;
    }
    else {
      setTimeout(function(){checkOrderReady(orderNum);},10000);
    }
  }
}

function getOrderNum(){
  var drinkToMake = document.getElementById('drinkSubmit').value
  const xhttp = new XMLHttpRequest(),
    method = "GET",
    url = "http://192.168.1.200:5000" + "/orders/createNew?order=" + document.curDrink;
  xhttp.open(method, url, false);
  xhttp.send(null);
  document.orderNum = xhttp.responseText;
  return xhttp.responseText;
}

function confDrink(conf){
  if (conf == 0){
    document.getElementById('modal_dc').style.display = "none";
  }
  else if (conf == 1){
    var orderNum = getOrderNum();
    var drinkReady = false;
    document.getElementById('modal_order_num').innerHTML = "Order Num: " + orderNum;
    document.getElementById('modal_status').innerHTML = "Status: Queued";
    document.getElementById('modal_pourButton').style.display = "none";
    document.getElementById('modal_dc').style.display = "none";
    document.getElementById('modal_ordered').style.display = "block";
    setTimeout(function(){checkOrderReady(orderNum);},250);
  }
}

function pourDrink(){
  var orderNum = document.orderNum;
  const xhttp = new XMLHttpRequest(),
    method = "GET",
    url = "http://192.168.1.200:5000" + "/orders/pour?number=" + orderNum; 
  xhttp.open(method, url, false);
  xhttp.send(null);
  setTimeout(function(){document.getElementById('modal_ordered').style.display = "none";},2000)
}

