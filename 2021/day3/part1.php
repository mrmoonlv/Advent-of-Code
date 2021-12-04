<?php

$input = file("data.txt");
$data = [];
$bit_count = strlen($input[0]) -2;
$memory = [];

$gamma_rate = '';
$epsilon_rate = '';

//Gamma calculation
for($i = 0; $i <= $bit_count; $i++){
    foreach ($input as $line){
        $bit = (int) $line[$i];
        if($bit == 0) {
            $memory[0][] = 1;
        } else {
            $memory[1][] = 1;
        }
    }

    $common_bits_count = [0 => count($memory[0]), 1 => count($memory[1])];
    $common_bit = array_search(max($common_bits_count), $common_bits_count);
    $gamma_rate .=  strval($common_bit);
    $memory = [];
    $common_bit = null;
    $common_bits_count = null;
}
$gamma_rate = bindec($gamma_rate);

$memory = [];
//Epsilon calculation
for($i = 0; $i <= $bit_count; $i++){
    foreach ($input as $line){
        $bit = $line[$i];
        if($bit == 0) {
            $memory[0][] = 1;
        } else {
            $memory[1][] = 1;
        }
    }

    $common_bits_count = [0 => count($memory[0]), 1 => count($memory[1])];
    $common_bit = ($common_bits_count[0] < $common_bits_count[1])?  : $common_bits_count[1];
    $common_bit = array_search($common_bit, $common_bits_count);
    $epsilon_rate .= strval($common_bit);
    $memory = [];
    $common_bit = null;
    $common_bits_count = null;
}
$epsilon_rate = bindec($epsilon_rate);
$power_consumption = $gamma_rate * $epsilon_rate;

echo sprintf("The power consumption of the submarine is %s", $power_consumption . PHP_EOL);

if(2498354 == $power_consumption) {
    echo "Answer is correct!";
}
