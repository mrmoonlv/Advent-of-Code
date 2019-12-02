<?php

//Sarg

$items = file("data.txt");

$data = [];
$guard = null;
$date = null;
$min = null;
$state = null;


function getDateInfo($item){
    $parts = explode("]", $item); 
    $string = str_replace("[", "", $parts[0]);
    $timestamp = strtotime($string);

    return array(
        'timestamp' => $timestamp,
        'day' => date('m-d', $timestamp),
        'min' => date('i', $timestamp)
     );
}


function sortItems($items){

    $sorted_items = [];

    foreach ($items as $item) {

        $date_info = getDateInfo($item);
        $event = array(
            'item' => $item,
            'date' => $date_info
            );

        $sorted_items[$date_info['timestamp']] = $event;
    }

    ksort($sorted_items);

    return $sorted_items;
}

function checkGuard($item, $guard){
    if (strpos($item, '#') === false) {
        return $guard;
    }

    $parts = explode("#", $item);
    $guard = floatval($parts[1]);

    return $guard;
}

function checkGuardState($item){
    if (strpos($item, 'asleep') !== false) {
        return 'sleep';
    }
    return 'awake';
}

$i = 1;
$sorted_items = sortItems($items);

print_r($sorted_items);

foreach ($sorted_items as $item) {
    $guard = checkGuard($item, $guard);
    $state = checkGuardState($item);
    $date = getDateInfo($item);
    $data[$guard][$date['day']][$state][] = $date['min'];
}

print_r($data);