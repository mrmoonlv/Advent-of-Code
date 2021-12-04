<?php

$logs = file("data.txt");
$sorted_logs = [];
$data = [];
$active_guard = null;
$guard_sleep = false;
$sleep = null;
$awake = null;
$minutes_guard_sleeps = [];
$date = '';

foreach ($logs as $log) {
    $parts = explode("]", $log);
    $string = str_replace("[", "", $parts[0]);
    $timestamp = strtotime($string);
    $sorted_logs[$timestamp] = $log;
}
ksort($sorted_logs);

foreach ($sorted_logs as  $timestamp => $log) {
    $parts = explode(']' , $log);
    $date = substr($parts[0], -11, 5);

    if(strpos($log, 'begins shift') !== false) {
        preg_match('!\d+!', $parts[1], $matches);
        $current_guard = (int) $matches[0];

        if($current_guard != $active_guard) {
            $active_guard = $current_guard;
            echo "Guard changes...Date:: " . $date . PHP_EOL;
            $awake = null;
            $sleep = null;
        }
        echo "Active guard: #" . $current_guard . PHP_EOL;

        if(empty($minutes_guard_sleeps[$current_guard])) {
            $minutes_guard_sleeps[$current_guard] = 0;
        }

    }

    if(strpos($log, 'falls asleep') !== false) {
        $sleep = (int) substr($parts[0], -2);
        echo "Sleep: " . $sleep . PHP_EOL;
    }

    if(strpos($log, 'wakes up') !== false) {
        $awake = (int) substr($parts[0], -2);
        echo "Wakes up: " . $awake . PHP_EOL;

        $total_sleep = $awake - $sleep;
        echo sprintf("Guard #%s sleep from %s to %s . Total %s minutes", $active_guard, $sleep, $awake, $total_sleep) . PHP_EOL;
        $minutes_guard_sleeps[$current_guard] = $minutes_guard_sleeps[$current_guard] + $total_sleep;

        for($sleep; $sleep < $awake; $sleep++){
            $data[$active_guard][$sleep][] = 1;
        }

        $sleep = null;
        $awake = null;
        $total_sleep = null;
    }
}

$most_sleepy_guard = array_search(max($minutes_guard_sleeps), $minutes_guard_sleeps);
$max_times_in_popular_minute = 0;
$popular_minute = 0;

foreach ($data[$most_sleepy_guard] as $minute => $times){
    if($max_times_in_popular_minute < count($times)) {
        $max_times_in_popular_minute = count($times);
        $popular_minute = $minute;
    }
}

$id = $most_sleepy_guard * $popular_minute;

echo sprintf("The ID of the guard multiplied by the minute is: %s", $id) . PHP_EOL;
if(8421 == $id) {
    echo "Answer is correct!";
}
