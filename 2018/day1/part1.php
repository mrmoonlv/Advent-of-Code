<?php 
$frequencies = [];
$total = 0;

$input = file("data.txt");	
	
foreach ($input as  $value) {
	$value = (int) $value;
	$total =  $total + $value;
}

echo "Total: $total". PHP_EOL; 