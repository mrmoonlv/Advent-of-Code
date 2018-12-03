<?php

$items = file("data.txt");
$rectangles = [];

function getItemGeometry($item){
    $rectangle = [];
    $parts = explode("@", $item);

    $rectangle ['id'] = str_replace(array("#", " "), "", $parts['0']);
    $parts = explode(",", $parts[1]);
    $rectangle ['left'] = (int)$parts[0];
    $parts = explode(":", $parts[1]);
    $rectangle ['top'] = (int)$parts[0];
    $parts = explode("x", $parts[1]);
    $rectangle ['x'] = (int)$parts[0];
    $rectangle ['y'] = (int)$parts[1];
    $rectangle['size'] = $rectangle ['x'] * $rectangle ['y'];

    return $rectangle;
}

function makeGridArray($x = 20, $y = 20){
    $grid = [];
    $line = [];

    for ($i = 1; $i <= $x; $i++) {
        $line[] = 0;
    }

    for ($i = 1; $i <= $y; $i++) {
        $grid[] = $line;
    }

    return $grid;
}

function fillGridWithItems($rectangles, $grid){
    foreach ($rectangles as $rectangle) {

        $line = $rectangle['top'];

        for ($i = 1; $i <= $rectangle['y']; $i++) {
            $left = $rectangle['left'];
            for ($ii = 1; $ii <= $rectangle['x']; $ii++) {
                if (!isset($grid[$line][$left]) || $grid[$line][$left] == 0) {
                    $grid[$line][$left] = $rectangle['id'];
                } else {
                    $grid[$line][$left] = "X";
                }

                $left++;
            }
            $line++;
        }
    }

    return $grid;
}

function draw($grid){
    echo "=========================================" . PHP_EOL;
    foreach ($grid as $line) {

        $count = count($line);
        $i = 0;
        foreach ($line as $item) {
            $i++;
            echo $item;
            if ($i == $count) {
                echo PHP_EOL;
            }
        }
    }
    echo "=========================================" . PHP_EOL;
}

function find($rectangles, $grid){

    $picture = [];

    foreach ($grid as $line) {
        foreach ($line as $id) {

            if (!isset($picture[$id])) {
                $picture[$id] = 0;
            }

            $picture[$id]++;
        }
    }

    $results = [];

    foreach ($rectangles as $id => $rectangle) {

        $size = $rectangle['size'];

        if (isset($picture[$id])) {
            if ($picture[$id] == $size) {
                $results[$size] = $id;
            }
        }

    }

    ksort($results);

    return $results;
}

$grid = makeGridArray(1200, 1200);

foreach ($items as $item) {
    $rectangle = getItemGeometry($item);
    $rectangles[$rectangle['id']] = $rectangle;
}

$grid = fillGridWithItems($rectangles, $grid);
$results = find($rectangles, $grid);

end($results);

echo "Found ID: " . $results[key($results)] . PHP_EOL;