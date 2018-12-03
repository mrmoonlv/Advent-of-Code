<?php

$items = file("data.txt");
$rectangles = [];

function getItemGeometry($item)
{
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

    return $rectangle;
}

function makeGridArray( $x =20, $y = 20) {
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

function fillGridWithItems($rectangles, $grid) {
    foreach ($rectangles as $rectangle) {

        $line = $rectangle['top'];

        for($i = 1; $i <= $rectangle['y']; $i++ ) {
            $left = $rectangle['left'];
            for($ii = 1; $ii <= $rectangle['x']; $ii++) {

                $count =$grid[$line][$left];
                $count++;
                $grid[$line][$left] = $count;
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

function countSquareInches($grid){
    $found = 0;

    foreach ($grid as $line) {
        foreach ($line as $item) {
            if ($item  > 1) {
                $found++;
            }

        }
    }
    return $found;
}

$grid = makeGridArray(1200, 1200);


foreach ($items as $item) {
    $rectangles[] = getItemGeometry($item);
}

$grid = fillGridWithItems($rectangles, $grid);

//draw($grid);

echo "Total: " . countSquareInches($grid) . PHP_EOL;