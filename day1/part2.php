<?php 

$frequencies = [];
$current = 0;
$found = false;
$input = file("data.txt");	

function find($frequencies, $current, $found, $input){
	foreach ($input as  $value) {
	$value = (int) $value;
	$current =  $current + $value;
		if(in_array($current, $frequencies)) {
			die("Found: " . $current . PHP_EOL);
		}

		$frequencies[] = $current;
	}

	find($frequencies, $current, $found, $input);
}

find($frequencies, $current, $found, $input);
