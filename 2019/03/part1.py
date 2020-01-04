#!/usr/bin/python3
# https://adventofcode.com/2019/day/3

def read_wire(line):
    return [ (entry[0], int(entry[1:])) for entry in line.split(",") if entry[0].isalpha() ]

def check_position(field, pos, hits):
    key = str(pos[0]) + "," + str(pos[1])

    if hits != None:
        if key in field:
            hits.append(pos)
    else:
        field[key] = True

def check_segment(field, pos, entry, hits):
    op, arg = entry
    x0, y0 = pos
    if op == 'L':
        for x in range(x0 - arg, x0):
            check_position(field, (x, y0), hits)
        return (x0 - arg, y0)
    if op == 'R':
        for x in range(x0 + 1, x0 + arg + 1):
            check_position(field, (x, y0), hits)
        return (x0 + arg, y0)
    if op == 'U':
        for y in range(y0 - arg, y0):
            check_position(field, (x0, y), hits) 
        return (x0, y0 - arg)
    if op == 'D':
        for y in range(y0 + 1, y0 + arg + 1):
            check_position(field, (x0, y), hits)
        return (x0, y0 + arg)

def main():
    input_file = open("input.txt")  
    wire0 = read_wire(input_file.readline())
    wire1 = read_wire(input_file.readline())

    field = {}    
    hits = []

    pos = (0, 0)
    for entry in wire0:
        pos = check_segment(field, pos, entry, None)

    pos = (0, 0)
    for entry in wire1:
        pos = check_segment(field, pos, entry, hits)

    min_dist = 10000000

    for hit in hits:
        dist = abs(hit[0]) + abs(hit[1])
        min_dist = min(min_dist, dist)

    print(min_dist)

main()