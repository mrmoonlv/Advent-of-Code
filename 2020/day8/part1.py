#!/usr/bin/env python3
import sys
from typing import Dict, List


def buildInstruction():
    data: List[Dict[str, int]] = []

    for line in open('data.txt').read().splitlines():
        parts = line.split(" ")
        data.append({parts[0]: int(parts[1])})

    return data


def walk():
    global index
    global accumulator
    global touched_instructions
    global instructions

    if index in touched_instructions:
        print("Accumulator is:", accumulator)
        assert accumulator == 1528
        sys.exit()

    touched_instructions.append(index)

    for operator, value in instructions[index].items():
        print(operator, value)
        if operator == 'jmp':
            index += value

        if operator == 'acc':
            accumulator += + value
            index += +1

        if operator == 'nop':
            index += +1

    return True


instructions = buildInstruction()
accumulator = 0
touched_instructions = []
index = 0

while True:
    walk()
