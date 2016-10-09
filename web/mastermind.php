<?php
error_reporting(E_ALL);

  if(!empty( $_GET["player"]) && !empty( $_GET["guess"])){
    $player = $_GET["player"];
    $player = substr($player, 0, 10);
    preg_replace('/[^a-zA-Z]/', '', $player);
    $guess = $_GET["guess"];
    preg_replace('/[^1-6]/', '', $guess);

    $command = escapeshellcmd("../mastermind.py $player $guess");
    $output = shell_exec($command);
    echo $output;
  }
  else if(!empty( $_GET["show"] )){
    if($_GET["show"]=="highscores"){
      $command = escapeshellcmd("../print_highscores.py");
      $output = shell_exec($command);
      echo $output;
    }
  }
  else{
   echo 'Hallo';
   echo $_GET["player"];
   echo $_GET["guess"];
  }
?>
