#!/usr/bin/env python3

def buildInstruction():
    program = []

    for line in open('data.txt').read().splitlines():
        parts = line.split(" ")
        program.append((parts[0], int(parts[1])))

    return program


def process(program):
    accumulator: int = 0
    index = 0
    touched_indexes = []

    while index not in touched_indexes:
        instruction = program[index]
        code, signal = instruction
        touched_indexes.append(index)

        if code == 'jmp':
            index += signal

        if code == 'acc':
            accumulator += signal
            index += 1
        if code == 'nop':
            index += 1

        if index >= len(data):
            print("Exit process")
            return accumulator, False

    print("Loop found! Exit...")
    return accumulator, True


program_cycle = 0
instructions = buildInstruction()

while True:
    data = instructions.copy()
    operator, value = data[program_cycle]
    if operator == 'nop':
        data[program_cycle] = ('jmp', value)
    elif operator == 'jmp':
        data[program_cycle] = ('nop', value)

    print("Run program #", program_cycle, "with", data)

    accumulator_value, state = process(data)

    if not state:
        print("Found accumulator:", accumulator_value)
        assert accumulator_value == 640
        break
    program_cycle += +1
