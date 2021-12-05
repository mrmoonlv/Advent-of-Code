<?php
$input = file("data.txt");
$numbers = explode(',', $input[0]);

$boards = [];
$unmarked_numbers_sum = 0;
$unmarked_numbers = [];
$bingo = false;

unset($input[0], $input[1]);

$board = [];
foreach ($input as $line){
    if(strlen($line) <= 1){
        continue;
    }

    preg_match_all('/([0-9]{1,2})/', $line, $line_numbers);
    $line_numbers = $line_numbers[0];
    $board[] = $line_numbers;

    if(count($board) == 5) {
        $boards[] = $board;
        $board = [];
    }
}

function fillBoards($boards, $number){
    foreach ($boards as $b => $board){
        foreach ($board as $l => $line){
            foreach ($line as $n => $line_number){
                if($line_number == $number){
                    $boards[$b][$l][$n] = $number."-CHECK";
                }
            }
        }
    }

    return $boards;
}

function checkBingo($boards){
    foreach ($boards as $b => $board){
        //look row
        $row_checks = 0;
        $col_checks = 0;

        //horizontal
        foreach ($board as $line){
            foreach ($line as $number){
                if(strpos($number, '-CHECK') !== false){
                    $row_checks++;
                }
            }

            if($row_checks == 5) {
                return ['board' => $b, 'line'];
            }
            $row_checks = 0;
        }

        //vertical
        for($x = 0; $x < 5; $x++){
            $col_numbers = [];
            for($y = 0; $y < 5; $y++){
                $col_numbers[] = $board[$y][$x];
            }

            foreach ($col_numbers as $col_number){
                if(strpos($col_number, '-CHECK') !== false){
                    $col_checks++;
                }
            }
            if($col_checks == 5) {
                return ['board' => $b, 'col'];
            }
            $col_checks = 0;
        }

    }

    return false;
}

foreach ($numbers as $winer_number) {
    $marked_numbers[$winer_number] = $winer_number;

    $boards = fillBoards($boards, $winer_number);
    $bingo = checkBingo($boards);


    if($bingo) {
        echo "BINGO!!!! Number: " . $winer_number . PHP_EOL;
        break;
    }
}

if($bingo) {
    $winner_board = $boards[$bingo['board']];
    foreach ($winner_board as $line){
        foreach ($line as $number) {
            $number = (int) $number;
            if(!in_array($number, $marked_numbers)){
                $unmarked_numbers_sum += $number;
            }
        }
    }

    $final_score = $unmarked_numbers_sum * $winer_number;

    echo sprintf("My board final score: %s", $final_score . PHP_EOL);

    if($final_score == 8580 ) {
        echo "Answer is correct!" ;
    }
}

