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
var http1 = new XMLHTTPObject();
function printhighscores() {
  document.getElementById("highscores").innerHTML = "";
  http1.open("GET","mastermind.php?show=highscores",true);
  http1.onreadystatechange = function() {
    if(http1.readyState == 4) {
      if(http1.status == 200) {
        document.getElementById("highscores").innerHTML = http1.responseText;
      }
    }
  }
  http1.send(null);
}


//This function will be called when the form is submited
function saveData() {
  //disable the button until we have received the result, as to prevent double submit
  document.getElementById("action").disabled = true;

  var http = new XMLHTTPObject();
  var player = document.getElementById("player").value;
  var guess = document.getElementById("guess").value;
  console.log('saving '+player+' '+guess);

  //By calling this file, we have saved the data.
  http.open("GET","mastermind.php?player="+player+"&guess=" + guess ,true);
  document.getElementById("gameresult").innerHTML = "";
  http.onreadystatechange = function() {
    if(http.readyState == 4) {
      if(http.status == 200) {
        document.getElementById("action").disabled = false;
        var res = http.responseText
        if(res != null){
          var resultobj = JSON.parse(res);
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
            document.getElementById("action").disabled = true;
            printhighscores();
          }
          else if (resultobj.lost) {
            document.getElementById("gameresult").innerHTML = "You lost :(";
            document.getElementById("action").disabled = true;
          }
        }
      }
    }
  }
  http.send(null);
  return false;//Prevent the form from being submited
}

function init() {
  document.getElementById("action").disabled = false;//make sure the button is enabled
  printhighscores();
  document.getElementById("player").focus();
  document.getElementById("feedback_form").onsubmit = saveData; //The saveData function is attached to the submit action of the form.
  document.getElementById("newgame_form").onsubmit = newGame;

  document.getElementById("guess").value = '';
  document.getElementById("tries").innerHTML = '';
  document.getElementById("result").innerHTML = '';
  document.getElementById("gameresult").innerHTML = '';
}

function newGame(){
  var player = document.getElementById("player").value;
  console.log('newgame '+player);
  if( player != '') {
    var http2 = new XMLHTTPObject();
    http2.open("GET","mastermind.php?player="+player+"&new=game" ,true);
    http2.onreadystatechange = function() {
      if(http2.readyState == 4) {
        if(http2.status == 200) {
          //wait until it has been loaded
        }
      }
     }
    http2.send(null);
  }
  init();//reset the page
  document.getElementById("guess").focus();
  return false;//Prevent the form from being submited
}


window.onload = init; //The 'init' function will be called when the page is loaded.

