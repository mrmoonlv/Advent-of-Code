<?php 

$strings = file("data.txt");

function find($strings, $need_for_boxes) {
	$founded = 0;
	foreach ($strings as $line) {
		$lines = [];
		$line = str_split($line);

		foreach ($line as $char) {
			if(array_key_exists($char, $lines)) {
				$lines[$char] = $lines[$char]+1;
			} else {
				$lines[$char] = 1;	
			}		
		}

		if(in_array($need_for_boxes, $lines)) {
			$founded++;
		}
	}

	return $founded;
}

$two = find($strings, 2);
$three = find($strings, 3);

echo "Found $two boxes with two chars and $three with three chars" . PHP_EOL;
$total = $two * $three;
echo "Cheksum: $total" . PHP_EOL;
