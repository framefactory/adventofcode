#!/usr/bin/python3
# https://adventofcode.com/2021/day/1

import sys

def main():
    with open("input.txt") as input_file:
        lines = input_file.readlines()

    depths = [ int(line) for line in lines if len(line.strip()) > 0 ]

    inc_count = 0
    prev_depth = sys.maxsize

    for depth in depths:
        if depth > prev_depth:
            inc_count += 1
        prev_depth = depth

    print(f'Part 1: {inc_count}')

    avg_depths = [ sum(depths[i-2:i+1]) for i in range(2, len(depths)) ]

    inc_count = 0
    prev_depth = sys.maxsize

    for depth in avg_depths:
        if depth > prev_depth:
            inc_count += 1
        prev_depth = depth

    print(f'Part 2: {inc_count}')



main()