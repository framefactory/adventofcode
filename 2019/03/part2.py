#!/usr/bin/python3
# https://adventofcode.com/2019/day/3#part2

# Note: this replaces part 1 and provides answers for part 1 and part 2.

def read_wire(line):
    return [ (entry[0], int(entry[1:])) for entry in line.split(",") if entry[0].isalpha() ]

def check_position(cursor, field0, field1, hits):
    x, y, steps = cursor
    key = str(x) + "," + str(y)

    if field1 != None:
        if not key in field1:
            field1[key] = steps
        if key in field0:
            hits.append((x, y, field0[key] + field1[key]))

    elif not key in field0:
        field0[key] = steps

def check_wire(wire, field0, field1, hits):
    cursor = (0, 0, 0)
    for entry in wire:
        op, arg = entry

        for i in range(0, arg):
            x, y, steps = cursor
            
            if op == 'L':
                cursor = (x - 1, y, steps + 1)
            elif op == 'R':
                cursor = (x + 1, y, steps + 1)
            elif op == 'U':
                cursor = (x, y - 1, steps + 1)
            elif op == 'D':
                cursor = (x, y + 1, steps + 1)

            check_position(cursor, field0, field1, hits)


def main():
    input_file = open("input.txt")  
    wire0 = read_wire(input_file.readline())
    wire1 = read_wire(input_file.readline())

    field0 = {}
    field1 = {}    
    hits = []

    check_wire(wire0, field0, None, None)
    check_wire(wire1, field0, field1, hits)

    min_steps = 1000000
    min_dist = 1000000

    for hit in hits:
        x, y, steps = hit
        min_dist = min(min_dist, abs(x) + abs(y))
        min_steps = min(min_steps, steps)

    print(min_dist)
    print(min_steps)

main()