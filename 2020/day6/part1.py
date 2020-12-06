#!/usr/bin/env python3

count: int = 0
for group in open("data.txt", "r").read().split("\n\n"):
    questions = list(set(group.replace('\n', ' ').replace(' ', '')))
    for question in questions:
        if question in 'abcdefghijklmnopqrstuvwxyz':
            count += +1

print("The sum of those counts:", count)
