#!/usr/bin/env python3

import re


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

                if self.validateFieldValue(password):
                    self.valid_passports += +1
                else:
                    self.invalid_passports += +1

        print(self.valid_passports, "Valid passwords")
        print(self.invalid_passports, "Invalid passwords")

    def validateFieldValue(self, password):

        if set(self.required_fields).issubset(password):
            for key in password:
                value = password[key]
                if key == 'byr':
                    value = int(value)
                    if 1920 <= value <= 2002:
                        continue
                    else:
                        print("KEY:", key, "VALUE", value, "INVALID")
                        return False

                elif key == 'iyr':
                    value = int(value)
                    if 2010 <= value <= 2020:
                        continue
                    else:
                        print("KEY:", key, "VALUE", value, "INVALID")
                        return False

                elif key == 'eyr':
                    value = int(value)
                    if 2020 <= value <= 2030:
                        continue
                    else:
                        print("KEY:", key, "VALUE", value, "INVALID")
                        return False
                elif key == 'hgt':

                    height_type = value[-2:]
                    if not height_type:
                        print("height_type INVALID")
                        return False

                    height_value = value[:-2]
                    if not height_value:
                        print("KEY:", key, "VALUE", value, "INVALID")
                        return False
                    height_value = int(height_value)

                    if height_type in ['cm', 'in']:
                        if height_type == 'cm' and (150 <= height_value <= 193):
                            continue
                        if height_type == 'in' and (59 <= height_value <= 76):
                            continue
                        else:
                            print("KEY:", key, "VALUE", value, "INVALID")
                            return False
                    else:
                        print("KEY:", key, "VALUE", value, "INVALID NOT CM or IN")
                        return False

                elif key == 'hcl':
                    if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):
                        continue
                    else:
                        print("KEY:", key, "VALUE", value, "INVALID")
                        return False
                elif key == 'ecl':
                    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        continue
                    else:
                        print("KEY:", key, "VALUE", value, "INVALID")
                        return False
                elif key == 'pid':
                    if len(value) != 9:
                        print("KEY:", key, "VALUE", value, "INVALID NOT 9 CHARS")
                        return False

                    value = int(value)

                    if type(value) == int:
                        continue
                    else:
                        print("KEY:", key, "VALUE", value, "INVALID")
                        return False
                else:
                    continue
            return True
        else:
            return False


Passports().analyzePasswords()