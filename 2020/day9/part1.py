#!/usr/bin/env python3


def isSumFind(variants, need):
    i = 0
    while i < len(variants):
        variant = variants.copy()
        A = variant.pop(i)

        for B in variant:
            if B != A and B + A == need:
                return True
        i += 1

    return False


def find(border: int):
    data = list(map(int, open('data.txt').read().splitlines()))
    line = 1

    while line <= len(data):
        if line > border:
            number: int = data[line]
            range = data[line - border: line]

            if not isSumFind(range, number):
                return number

        line += 1


preamble = 25
answer = find(preamble)
print("answer:", answer)
assert answer == 57195069
