#!/usr/bin/python3
# https://adventofcode.com/2020/day/1

from typing import List

def main():
    input_file = open("input.txt")
    content = input_file.read()
    entries = [ int(entry) for entry in content.splitlines() if len(entry) > 0 ]

    print(f'Part 1: {part1(entries)}')
    print(f'Part 2: {part2(entries)}')

def part1(entries: List[int]) -> int:
    for i0, e0 in enumerate(entries):
        for e1 in entries[i0+1:]:
            if e0 + e1 == 2020:
                return e0 * e1

def part2(entries: List[int]) -> int:
    for i0, e0 in enumerate(entries):
        for i1, e1 in enumerate(entries[i0+1:]):
            for e2 in entries[i1+1:]:
                if e0 + e1 + e2 == 2020:
                    return e0 * e1 * e2

main()
