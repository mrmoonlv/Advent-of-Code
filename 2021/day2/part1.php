<?php

$input = file("data.txt");
$x = 0;
$y = 0;

foreach ($input as $step){

    list($instruction, $value) = explode(' ', $step);
    $value = (int) $value;

    if($instruction == 'forward'){
        $x = $x + $value;
    }
    elseif ($instruction == 'up') {
        $y = $y + $value;
    }
    elseif ($instruction == 'down') {
        $y = $y - $value;
    }

}
$y = abs($y);
$result = $x * $y;

echo "Final horizontal position by your final depth multiply is: " . $result . PHP_EOL;
if(1989014 == $result) {
    echo "Answer is correct!";
}
