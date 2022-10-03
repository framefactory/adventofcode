#!/usr/bin/python
# http://adventofcode.com/2017/day/20

import re

def main():
    input_file = open("dec20_input.txt")
    #input_file = open("dec20_test.txt")
    stream = input_file.read()
    lines = [ line for line in stream.split("\n") if line ]

    pos = [ re.search("p=<(-?\d+),(-?\d+),(-?\d+)>", line) for line in lines ]
    vel = [ re.search("v=<(-?\d+),(-?\d+),(-?\d+)>", line) for line in lines ]
    acc = [ re.search("a=<(-?\d+),(-?\d+),(-?\d+)>", line) for line in lines ]

    pos = [ [ float(p.group(1)), float(p.group(2)), float(p.group(3)) ] for p in pos ]
    vel = [ [ float(v.group(1)), float(v.group(2)), float(v.group(3)) ] for v in vel ]
    acc = [ [ float(a.group(1)), float(a.group(2)), float(a.group(3)) ] for a in acc ]
    data = zip(pos, vel, acc)

    t = 10000

    end_pos = [ [ d[0][0] + d[1][0]*t + 0.5*d[2][0]*t*t,
        d[0][1] + d[1][1]*t + 0.5*d[2][1]*t*t,
        d[0][2] + d[1][2]*t + 0.5*d[2][2]*t*t ] for d in data ]

    dist = [ abs(p[0]) + abs(p[1]) + abs(p[2]) for p in end_pos ]
    min_index = dist.index(min(dist))
    print(min_index)

main()
