#!/usr/bin/python3
# https://adventofcode.com/2021/day/7

import sys

def main():
    with open("input.txt") as input_file:
        positions = [ int(pos) for pos in input_file.read().split(",") if len(pos.strip()) > 0 ]

        #positions = [16,1,2,0,4,2,7,1,2,14]
        max_pos = max(positions) + 1
        bins = [0] * max_pos
        for p in positions:
            bins[p] += 1
        
        min_fuel = sys.maxsize
        for pi in range(max_pos):
            fuel = 0
            for bi, b in enumerate(bins):
                fuel += abs(pi - bi) * b
            min_fuel = min(min_fuel, fuel)

        print(f'Part 1: {min_fuel}')

        min_fuel = sys.maxsize
        for pi in range(max_pos):
            fuel = 0
            for bi, b in enumerate(bins):
                d = abs(pi - bi)
                fuel += int(d * (d + 1) * b * 0.5)
            min_fuel = min(min_fuel, fuel)

        print(f'Part 2: {min_fuel}')

main()