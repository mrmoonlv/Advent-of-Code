#!/usr/bin/env python3

def find(numbers, need):
    total = sum(numbers)
    isFind = total, False

    if total == need:
        isFind = total, True

    return isFind


data = list(map(int, open('data.txt').read().splitlines()))
goal = 57195069
border_a = 0
border_b = 0
iterations = 0
while True:
    variant = data[border_a:border_b]
    variant_sum, state = find(variant, goal)
    iterations += +1

    if state:
        answer = min(variant) + max(variant)
        print("Program run with", iterations, "Iterations. The encryption weakness in  XMAS-encrypted data:", answer)
        assert answer == 7409241
        break

    if border_a > len(data):
        print("Borders reached")
        break

    if variant_sum > goal:
        border_a += 1
        border_b = 0
    elif border_b > len(data) - 1:
        border_a += 1
        border_b = 0
    else:
        border_b += 1
