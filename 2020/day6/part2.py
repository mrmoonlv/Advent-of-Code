#!/usr/bin/env python3

count: int = 0
groups = [group.split("\n") for group in open("data.txt", "r").read().split("\n\n")]


def countGroupSameAnswers(group):
    allowed_chars: str = 'abcdefghijklmnopqrstuvwxyz'
    answers_counts = 0
    group_answers = []
    for line in group:
        group_answers.append(line)


    for char in allowed_chars:
        if all([char in group_answer for group_answer in group_answers]):
            answers_counts += 1
    return answers_counts


for group in groups:
    count += countGroupSameAnswers(group)

print("Sum of the count of questions to which everyone answered 'yes':", count)
