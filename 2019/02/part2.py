#!/usr/bin/python3
# https://adventofcode.com/2019/day/2#part2

def run(ram):
    ptr = 0

    while ram[ptr] != 99:
        opcode = ram[ptr]
        op0 = ram[ptr + 1]
        op1 = ram[ptr + 2]
        dst = ram[ptr + 3]

        if opcode == 1: # add
            ram[dst] = ram[op0] + ram[op1]
        elif opcode == 2: # multiply
            ram[dst] = ram[op0] * ram[op1]

        ptr += 4

    return ram[0]

def main():
    data = open("input.txt").read()
    rom = [ int(part) for part in data.split(",") if part.isdigit() ]

    for noun in range(100):
        for verb in range(100):
            ram = rom[:]
            ram[1] = noun
            ram[2] = verb

            result = run(ram)
            if result == 19690720:
                print(100 * noun + verb)
                return


main()