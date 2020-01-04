#!/usr/bin/python3
# https://adventofcode.com/2019/day/2

def main():
    data = open("input.txt").read()
    mem = [ int(part) for part in data.split(",") if part.isdigit() ]

    mem[1] = 12
    mem[2] = 2

    ptr = 0

    while mem[ptr] != 99:
        opcode = mem[ptr]
        op0 = mem[ptr + 1]
        op1 = mem[ptr + 2]
        dst = mem[ptr + 3]

        if opcode == 1: # add
            mem[dst] = mem[op0] + mem[op1]
        elif opcode == 2: # multiply
            mem[dst] = mem[op0] * mem[op1]

        ptr += 4

    print(mem[0])

main()