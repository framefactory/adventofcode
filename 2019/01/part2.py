#!/usr/bin/python3
# https://adventofcode.com/2019/day/1#part2

import math

def calc_fuel_recursively(mass):
    fuel = math.floor(mass / 3) - 2
    return 0 if fuel <= 0 else fuel + calc_fuel_recursively(fuel)

def main():
    input_file = open("input.txt")
    data = input_file.read()
    entries = [ int(part) for part in data.split() if part.isdigit() ]

    result = 0
    for fuel in entries:
        result += calc_fuel_recursively(fuel)

    print(result)

main()