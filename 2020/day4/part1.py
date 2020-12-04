#!/usr/bin/env python3

class Passports:
    f = open("data.txt", "r")
    lines = f.read().split("\n\n")
    valid_passports = 0
    invalid_passports = 0
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]

    def analyzePasswords(self):
        for line in self.lines:
            if line:
                line = line.replace('\n', ' ')
                items = line.split(" ")
                password = {}
                for item in items:
                    field, value = item.split(":")
                    password[field] = value

                print(password)
                if set(self.required_fields).issubset(password):
                    self.valid_passports += +1
                else:
                    self.invalid_passports += +1

        print(self.valid_passports, "Valid passwords")
        print(self.invalid_passports, "Invalid passwords")


Passports().analyzePasswords()
