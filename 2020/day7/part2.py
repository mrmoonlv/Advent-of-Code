#!/usr/bin/env python3
import re


def buildRule(line):
    line_parts = line.split("contain")
    bag = line_parts[0].replace('bags', '').replace('bag', '').lstrip().strip()
    rule = line_parts[1].replace('bags', 'bag').replace(',', '.').replace('bag', '')

    parts = rule.split('.')
    bag_rules = {}
    for part in parts:
        if part in ['']:
            continue
        rule_bag = re.sub('\d+', ' ', part).lstrip().strip()
        if rule_bag in ['no other']:
            continue
        num = re.sub('\D+', ' ', part).lstrip().strip()
        bag_rules[rule_bag] = num

    return bag, bag_rules


def countBagsIn(bag_for_inspection):
    total: int = 1

    for rule_bag, rule_bag_count in dimensions[bag_for_inspection].items():
        total += int(rule_bag_count) * countBagsIn(rule_bag)
    return total


dimensions = dict([buildRule(line) for line in open('data.txt').read().splitlines()])
your_bag = 'shiny gold'
bags_count = countBagsIn('shiny gold') - 1
print(bags_count, 'individual bags are required inside your', your_bag, 'bag')
