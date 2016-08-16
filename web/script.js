function XMLHTTPObject() {
  var xmlhttp=false;
  //If XMLHTTPReques is available
  if (XMLHttpRequest) {
    try {xmlhttp = new XMLHttpRequest();}
    catch(e) {xmlhttp = false;}
  } else if(typeof ActiveXObject != 'undefined') {
    //Use IE's ActiveX items to load the file.
    try {xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");}
    catch(e) {
      try {xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");}
      catch(E) {xmlhttp = false;}
    }
  } else  { xmlhttp = false;}//Browser don't support Ajax
  return xmlhttp;
}
var http = new XMLHTTPObject();
//This function will be called when the form is submited
function saveData() {
  var guess = document.getElementById("guess").value;

  //By calling this file, we have saved the data.
  http.open("GET","mastermind.php?guess=" + guess ,true);
  document.getElementById("gameresult").innerHTML = "";
  http.onreadystatechange = function() {
    if(http.readyState == 4) {
      if(http.status == 200) {
        var resultobj = JSON.parse(http.responseText);
        if(parseInt(resultobj.tries)==1){
          document.getElementById("result").innerHTML = "";
        } else {
          document.getElementById("result").innerHTML += "\r\n";
        }
        document.getElementById("tries").innerHTML = resultobj.tries;
        document.getElementById("result").innerHTML += "Guess: "
        document.getElementById("result").innerHTML += guess+" Result: "+resultobj.result;
        if(resultobj.won) {
          document.getElementById("gameresult").innerHTML = "You won!";
        }
        else if (resultobj.lost) {
          document.getElementById("gameresult").innerHTML = "You lost :(";
        }
      }
    }
  }
  http.send(null);
  return false;//Prevent the form from being submited
}
function init() {
  document.getElementById("guess").focus();
  document.getElementById("feedback_form").onsubmit = saveData; //The saveData function is attached to the submit action of the form.
}
window.onload = init; //The 'init' function will be called when the page is loaded.
