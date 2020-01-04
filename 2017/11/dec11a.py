#!/usr/bin/python
# http://adventofcode.com/2017/day/11

import sys
import math
import functools

t1 = math.sin(math.pi / 6)
t2 = math.cos(math.pi / 6)

step = {
    "n": (0, 1),
    "ne": (t2, t1),
    "se": (t2, -t1),
    "s": (0, -1),
    "sw": (-t2, -t1),
    "nw": (-t2, t1),
}

step = {
    "n": (-1, 1),
    "ne": (0, 1),
    "se": (1, 0),
    "s": (1, -1),
    "sw": (0, -1),
    "nw": (-1, 0),
}

def closest_step(start, end):
    best_step = (0, 0)
    min_dist = sys.maxsize

    for key in step:
        s = step[key]
        x = end[0] - start[0] - s[0]
        y = end[1] - start[1] - s[1]
        d = x * x + y * y

        if d < min_dist:
            min_dist = d
            best_step = s

    return best_step

def shortest_path(pos):
    path_length = pos[0] * pos[0] + pos[1] * pos[1]
    start = (0, 0)
    seg_length = 0
    count = 0

    while seg_length < path_length:
        s = closest_step(start, pos)
        start = (start[0] + s[0], start[1] + s[1])
        seg_length = start[0] * start[0] + start[1] * start[1]
        count += 1
    
    #print(pos, path_length)
    #print(start, seg_length)

    return count - 1

def main():
    input_file = open("dec11_input.txt")
    stream = input_file.read()
    path = [ step[direction] for direction in stream.split(",") if direction.isalpha() ]
    end = functools.reduce(lambda s0, s1: (s0[0] + s1[0], s0[1] + s1[1]), path)

    print(shortest_path(end))

main()
