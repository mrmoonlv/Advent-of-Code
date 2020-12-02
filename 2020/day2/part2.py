#!/usr/bin/env python3

import sys

f = open("data.txt", "r")
lines = f.read().splitlines()

valid_passwords = 0

for line in lines:
    parts = line.split(" ")

    ranges = parts[0].split('-')
    first_index = int(ranges[0])
    second_index = int(ranges[1])
    need = parts[1].replace(':', '')
    password = parts[2]

    if(password[first_index-1] != password[second_index-1]):
        if((need == password[first_index-1]) or (need == password[second_index-1])):
            valid_passwords = valid_passwords +1

print("Valid passwords: ", valid_passwords)
