#!/usr/bin/python3
# https://adventofcode.com/2021/day/6

import re
import numpy as np

def main():
    with open("input.txt") as input_file:
        fish = [ int(f) for f in input_file.read().strip().split(",") ]

    bins = [0] * 9
    for f in fish:
        bins[f] += 1

    for di in range(80):
        zeros = bins[0]
        for bi in range(1, 9):
            bins[bi - 1] = bins[bi]
        bins[6] += zeros
        bins[8] = zeros

    print(f'Part 1: {sum(bins)}')

    with open("input.txt") as input_file:
        fish = [ int(f) for f in input_file.read().strip().split(",") ]

    bins = [0] * 9
    for f in fish:
        bins[f] += 1

    for di in range(256):
        zeros = bins[0]
        for bi in range(1, 9):
            bins[bi - 1] = bins[bi]
        bins[6] += zeros
        bins[8] = zeros

    print(f'Part 2: {sum(bins)}')


main()
