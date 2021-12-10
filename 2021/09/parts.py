#!/usr/bin/python3
# https://adventofcode.com/2021/day/9

def main():
    with open("input.txt") as input_file:
        floor = [ [ int(c) for c in line.strip() ] for line in input_file.readlines() if len(line.strip()) > 0 ]

    size_x = len(floor[0])
    size_y = len(floor)
    score = 0
    for y in range(size_y):
        for x in range(size_x):
            if is_low_point(floor, x, y):
                score += 1 + floor[y][x]

    print(f'Part 1: {score}')

    visited = [ [False] * size_x for line in floor ]
    basins = []
    for y in range(size_y):
        for x in range(size_x):
            if is_low_point(floor, x, y):
                basins.append(find_basin(floor, visited, x, y))

    basins.sort(reverse=True)
    print(basins)
    print(f'Part 2: {basins[0] * basins[1] * basins[2]}')

def find_basin(floor, visited, x, y):
    if visited[y][x]:
        return 0

    visited[y][x] = True
    p = floor[y][x]
    score = 1

    if x > 0:
        pn = floor[y][x - 1]
        if pn < 9 and pn > p:
            score += find_basin(floor, visited, x - 1, y)
    if x < len(floor[0]) - 1:
        pn = floor[y][x + 1]
        if pn < 9 and pn > p:
            score += find_basin(floor, visited, x + 1, y)
    if y > 0:
        pn = floor[y - 1][x]
        if pn < 9 and pn > p:
            score += find_basin(floor, visited, x, y - 1)
    if y < len(floor) - 1:
        pn = floor[y + 1][x]
        if pn < 9 and pn > p:
            score += find_basin(floor, visited, x, y + 1)

    return score


def is_low_point(floor, x, y):
    max_x = len(floor[0]) - 1
    max_y = len(floor) - 1
    px0 = floor[y][x - 1] if x > 0 else 10
    px1 = floor[y][x + 1] if x < max_x else 10
    py0 = floor[y - 1][x] if y > 0 else 10
    py1 = floor[y + 1][x] if y < max_y else 10
    p = floor[y][x]
    return p < px0 and p < px1 and p < py0 and p < py1

main()