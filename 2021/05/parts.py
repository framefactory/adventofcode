#!/usr/bin/python3
# https://adventofcode.com/2021/day/5

import re
import numpy as np

def main():
    with open("input.txt") as input_file:
        lines = [ line.strip() for line in input_file.readlines() if len(line.strip()) > 0 ]

    # parse segments: x0, y0 -> x1, y1
    re_coords = re.compile("(\d+),(\d+) -> (\d+),(\d+)")
    segs = np.array([ [ int(n) for n in re.match(re_coords, line).group(1, 2, 3, 4) ] for line in lines ])
    
    size_x = max([ max(s[0], s[2]) for s in segs ]) + 1
    size_y = max([ max(s[1], s[3]) for s in segs ]) + 1

    field = [ [0] * size_x for n in range(size_y) ]
    for s in segs:
        dx, dy = s[2] - s[0], s[3] - s[1]
        if dx == 0 or dy == 0:
            steps = max(abs(dx), abs(dy))
            sx, sy = int(dx / steps), int(dy / steps)
            x, y = s[0], s[1]
            for i in range(steps + 1):
                field[y][x] += 1
                x += sx
                y += sy

    crosspoints_p1 = 0
    for y in range(0, size_y):
        for x in range(0, size_x):
            if field[y][x] > 1:
                crosspoints_p1 += 1

    print(f'Part 1: {crosspoints_p1}')

    field = [ [0] * size_x for n in range(size_y) ]
    for s in segs:
        dx, dy = s[2] - s[0], s[3] - s[1]
        steps = max(abs(dx), abs(dy))
        sx, sy = int(dx / steps), int(dy / steps)
        x, y = s[0], s[1]
        for i in range(steps + 1):
            field[y][x] += 1
            x += sx
            y += sy

    crosspoints_p2 = 0
    for y in range(0, size_y):
        for x in range(0, size_x):
            if field[y][x] > 1:
                crosspoints_p2 += 1

    print(f'Part 2: {crosspoints_p2}')


main()