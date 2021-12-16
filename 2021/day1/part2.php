<?php

$input = file("data.txt");
$total_lines =count($input);

$last_sum = 0;
$increased = 0;
$runs = 0;
$key1 = 0;
$key2 = 1;
$key3 = 2;

while (true) {
    $a = (int) $input[$key1];
    $b = (!empty($input[$key2])) ? (int) $input[$key2]: null;
    $c = (!empty($input[$key3])) ? (int) $input[$key3]: null;
    $sum = array_sum([$a,  $b,  $c]);

    $runs++;
    $key1++;
    $key2++;
    $key3++;

    if($sum > $last_sum && $last_sum != 0){
        $increased++;
    }
    $last_sum = $sum;

    if($total_lines - $runs == 2) {
        break;
    }
}

print_r(sprintf("%s sums are larger than the previous sum", $increased) . PHP_EOL);
if(1217 == $increased) {
    echo "Answer is correct!";
}

