#!/usr/bin/python3
# https://adventofcode.com/2019/day/1

import math

def main():
    input_file = open("input.txt")
    data = input_file.read()
    entries = [ int(part) for part in data.split() if part.isdigit() ]

    result = 0
    for fuel in entries:
        result += math.floor(fuel / 3) - 2

    print(result)

main()
