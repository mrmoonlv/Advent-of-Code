#!/usr/bin/env python3

import sys

f = open("data.txt", "r")
lines = f.read().splitlines()

valid_passwords = 0

for line in lines:
    parts = line.split(" ")

    ranges = parts[0].split('-')
    start = int(ranges[0])
    stop = int(ranges[1])
    need = parts[1].replace(':', '')
    password = parts[2]
    needs_in_password = 0
    for char in password:
        if(char == need):
            needs_in_password = needs_in_password + 1

    if(needs_in_password in range(start, stop + 1) ):
        valid_passwords = valid_passwords + 1

print("Valid passwords: ", valid_passwords)
