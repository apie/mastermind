<?php
error_reporting(E_ALL);

  if(!empty( $_GET["player"]) && !empty( $_GET["guess"])){
    $player = $_GET["player"];
    $player = substr($player, 0, 10);
    $player = preg_replace('/[^a-zA-Z]/', '', $player);

    $guess = $_GET["guess"];
    $guess = preg_replace('/[^1-6]/', '', $guess);

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
  else if(!empty( $_GET["new"] ) && !empty( $_GET["player"])){
    $player = $_GET["player"];
    $player = substr($player, 0, 10);
    $player = preg_replace('/[^a-zA-Z]/', '', $player);
    if($_GET["new"]=="game"){
      $command = escapeshellcmd("../new_game.py $player");
      $output = shell_exec($command);
      echo $output;
    }
  }
  else{
   echo 'Hallo<br>';
   echo $_GET["player"];
  }
?>
