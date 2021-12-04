<?php

$numbers = file("data.txt");
$data = [];
$bit_count = strlen($numbers[0]) -2;

$life_support_rating = null;
$oxygen_generator_rating = null;
$co2_scrubber_rating = null;

function countNumbersInColByBit($numbers, $col, $filter) {
    $data = [];
    $col_nummbers = '';
    foreach ($numbers as $line){
        $col_nummbers .= strval($line[$col]);
    }

    $high_bit = (int) substr_count($col_nummbers, 1);
    $low_bit = (int) substr_count($col_nummbers, 0);

    if($filter == 'more') {
        $common_bit = ($high_bit >= $low_bit) ? 1 : 0;
    }
    elseif ($filter == 'low') {
        $common_bit = ($high_bit >= $low_bit) ? 0 : 1;
    }

    foreach ($numbers as $line) {
        if($line[$col] == $common_bit) {
            $data[] = $line;
        }
    }


    return $data;
}

for($i = 0; $i <= $bit_count; $i++){
    $numbers = countNumbersInColByBit($numbers, $i, 'more');

    if(count($numbers) == 1) {
        $oxygen_generator_rating = bindec($numbers[0]);
        echo sprintf("Found oxygen generator rating: %s", $oxygen_generator_rating . PHP_EOL);
        break;
    }
}

$numbers = file("data.txt");
for($i = 0; $i <= $bit_count; $i++){
    $numbers = countNumbersInColByBit($numbers, $i, 'low');

    if(count($numbers) == 1) {
        $co2_scrubber_rating = bindec($numbers[0]);
        echo sprintf("Found CO2 scrubber rating: %s", $co2_scrubber_rating . PHP_EOL);
        break;
    }
}

$life_support_rating = $oxygen_generator_rating * $co2_scrubber_rating;
echo sprintf("The life support rating of the submarine: %s", $life_support_rating . PHP_EOL);

if(3277956 == $life_support_rating) {
    echo "Answer is correct!";
}