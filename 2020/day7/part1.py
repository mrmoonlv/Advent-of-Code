#!/usr/bin/env python3
import re

your_bag = 'shiny gold'
lines = open('data.txt').read().splitlines()
bag_dimensions = {}
bags_can_hanndle_my_bag = 0

def parseBag(string):
    return string.replace('bags', '').replace('bag', '').lstrip().strip()


def parseRules(rule):
    rule = rule.replace('bags', 'bag').replace(',', '.').replace('bag', '')
    rule = re.sub(" \d+", " ", rule)
    contents = []

    parts = rule.split('.')
    for part in parts:
        part = part.lstrip().strip()
        if part == '' or part == '  ' or part == 'no other':
            continue
        part = part.lstrip().strip()
        if len(part) > 0:
            contents.append(part)

    return ','.join(contents)


for line in lines:
    parts = line.split("contain")
    bag_dimensions[parseBag(parts[0])] = parseRules(parts[1]).split(',')


def isCanHoldShiny(baggage, bag_for_inspection):
    can_handle_dimensions = 0

    for bag_dimension in bag_dimensions[baggage]:
        if bag_dimension == '':
            return 0
        elif bag_for_inspection in bag_dimension:
            return 1
        else:
            can_handle_dimensions += isCanHoldShiny(bag_dimension, bag_for_inspection)

    return can_handle_dimensions


for bag_dimension in bag_dimensions:
    if isCanHoldShiny(bag_dimension, your_bag):
        bags_can_hanndle_my_bag += +1

print('Bag colors who can contain at least one shiny gold bag:', bags_can_hanndle_my_bag)
