<?php

$input = file("data.txt");
$x = 0;
$y = 0;
$aim = 0;

foreach ($input as $step){

    list($instruction, $value) = explode(' ', $step);
    $value = (int) $value;

    if($instruction == 'forward'){
        $x = $x + $value;

        $y = $y + ($aim * $value) ;
    }
    elseif ($instruction == 'up') {
        $aim = $aim - $value;
    }
    elseif ($instruction == 'down') {
        $aim = $aim + $value;
    }

}

echo sprintf("FINAL: X:%s  Y:%s AIM:%s\n", $x, $y, $aim);
$result = $x * $y;

echo "Final horizontal position by your final depth multiply is: " . $result . PHP_EOL;
if(2006917119 == $result) {
    echo "Answer is correct!";
}
