#!/usr/bin/python3
# https://adventofcode.com/2020/day/2

def main():
    input_file = open("input.txt")
    content = input_file.read()
    lines = content.splitlines()

    valid = 0

    for line in lines:
        rule, pwd = line.split(": ")
        bounds, char = rule.split(" ")
        min, max = [ int(b) for b in bounds.split("-") ]

        filtered_pwd = [ c for c in pwd if c == char ]
        l = len(filtered_pwd)
        if l >= min and l <= max:
            valid += 1

    print(f'Part 1: {valid}')

    valid = 0

    for line in lines:
        rule, pwd = line.split(": ")
        bounds, char = rule.split(" ")
        p0, p1 = [ int(b) - 1 for b in bounds.split("-") ]

        hits = 0
        if pwd[p0] == char:
            hits += 1
        if pwd[p1] == char:
            hits += 1
        if hits == 1:
            valid += 1

    print(f'Part 2: {valid}')

main()