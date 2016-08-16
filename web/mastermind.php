<?php
  header('Content-Type: application/json');
  if(!empty( $_GET["guess"])){
    $str = $_GET["guess"];
    preg_replace('/[^1-6]/', '', $str);
    $handle = popen("./mastermind.py $str", "r");
    $read = fread($handle, 100);
    pclose($handle);
    echo $read;
  }
?>
