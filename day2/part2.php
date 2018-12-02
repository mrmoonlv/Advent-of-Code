<?php 

function diff($a, $b) {
	$diff = 0;
	$aa = str_split($a);
	$bb = str_split($b);
	$times = count($aa) -1;

	for($i = 1; $i<=$times; $i++){
		if ($aa[$i-1] != $bb[$i-1]) {
			$diff++;
		}
	}
	return $diff;
}

//TEST
//echo diff("abcde", "axcye") . PHP_EOL;
//echo diff("fghij", "fguij") . PHP_EOL;
//echo diff("fghij","klmno"). PHP_EOL;
//echo diff("Xbcde","edcbY"). PHP_EOL;
//echo diff("Xbcde","Xbcde"). PHP_EOL;

$strings = file("data.txt");
$times = count($strings);

$results = [];

for ($i = 1; $i <= $times; $i++) {
 	$a = $strings[$i-1];
	unset($strings[$i-1]);

	foreach ($strings as $b) {
		$diff = diff($a, $b);
		if ($diff ==  1) {
		$results[] = array('a' => $a, "b" => $b, "diff" => $diff );	
		}
		
	}
}
print_r($results);