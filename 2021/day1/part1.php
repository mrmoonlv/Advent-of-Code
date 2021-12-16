<?php

$input = file("data.txt");
$times = 0;
$last_measurement = 0;

foreach ($input as $current_dept) {
	$current_dept = (int) $current_dept;

	if($current_dept > $last_measurement && $last_measurement != 0) {
	    $times++;
    }

	$last_measurement = $current_dept;
	print_r(sprintf("Last measurement: %s  Times: %s  Current dept: %s ", $last_measurement, $times, $current_dept) . PHP_EOL);

}

echo sprintf("there are %s measurements that are larger than the previous measurement.", $times) . PHP_EOL;
if(1266 == $times) {
    echo "Answer is correct!";
}
