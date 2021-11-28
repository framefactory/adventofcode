#!/usr/bin/python3
# https://adventofcode.com/2020/day/4

import re
from functools import reduce

def main():
    with open("input.txt") as input_file:
        content = input_file.read()
        
    passports = [ p.strip().split() for p in content.split("\n\n") if len(p) > 0 ]
    print(f'read {len(passports)} passports')

    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = reduce(lambda sum, ok: sum + ok, [ check_passport(p, required) for p in passports ], 0)
    print(f'Part 1: {valid_count} valid passports')

    valid_count = reduce(lambda sum, ok: sum + ok, [ validate_passport(p, required) for p in passports ], 0)
    print(f'Part 2: {valid_count} valid passports')


def check_passport(passport, required):
    flags = [0] * len(required)
    for entry in passport:
        try:
            flags[required.index(entry.split(":")[0])] += 1
        except:
            pass

    return reduce(lambda a, b: a + b, flags, 0) >= len(required)

def validate_passport(passport, required):
    checked = check_passport(passport, required)
    if not checked:
        return False

    for entry in passport:
        [ key, text ] = entry.split(":")
        valid = False

        if key == "byr":
            value = int(text)
            valid = len(text) == 4 and value >= 1920 and value <= 2002 
            
        elif key == "iyr":
            value = int(text)
            valid = len(text) == 4 and value >= 2010 and value <= 2020 
            
        elif key == "eyr":
            value = int(text)
            valid = len(text) == 4 and value >= 2020 and value <= 2030 

        elif key == "hgt":
            match = re.fullmatch("(\d+)(cm|in)", text) 
            if match:
                value = int(match.group(1))
                print(match.group(1), match.group(2))
                if match.group(2) == "cm":
                    valid = value >= 150 and value <= 193
                elif match.group(2) == "in":
                    valid = value >= 59 and value <= 76

        elif key == "hcl":
            valid = re.fullmatch("#[0-9a-f]{6}", text) is not None

        elif key == "ecl":
            valid = re.fullmatch("(amb|blu|brn|gry|grn|hzl|oth)", text) is not None

        elif key == "pid":
            valid = re.fullmatch("\d{9}", text) is not None

        elif key == "cid":
            valid = True

        print(f"{entry} is {'valid' if valid else 'invalid'}")
        if not valid:
            return False

    return True

main()