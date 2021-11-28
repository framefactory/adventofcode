#!/usr/bin/python3
# https://adventofcode.com/2020/day/3

def main():
    with open("input.txt") as input_file:
        content = input_file.read()
        lines = [ line for line in content.splitlines() if len(line) > 0 ]

    tree_count = count_trees(lines, [3, 1])
    print(f'Part 1: {tree_count} trees')

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    prod = 1
    for slope in slopes:
        prod *= count_trees(lines, slope)
    print(f'Part 2: {prod}')

def count_trees(lines, slope):
    x = slope[0]
    y = slope[1]
    tree_count = 0
    size_x = len(lines[0])


    while y < len(lines):
        if lines[y][x % size_x] == '#':
            tree_count += 1
        x += slope[0]
        y += slope[1]

    print(tree_count)
    return tree_count

main()