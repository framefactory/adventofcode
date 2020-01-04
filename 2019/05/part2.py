#!/usr/bin/python3
# https://adventofcode.com/2019/day/5#part2

import time

def arg(prg, ptr, mode):
    return prg[ptr] if mode == 1 else prg[prg[ptr]]

def step(prg, ptr, inp):
    cmd = "00000" + str(prg[ptr])
    opcode = int(cmd[-2:])

    if (opcode == 99):
        return -1

    modes = [ int(cmd[-p-3]) for p in range(0, 3) ]

    if opcode == 1: # add
        prg[prg[ptr + 3]] = arg(prg, ptr + 1, modes[0]) + arg(prg, ptr + 2, modes[1])
        ptr += 4    
    elif opcode == 2: # multiply
        prg[prg[ptr + 3]] = arg(prg, ptr + 1, modes[0]) * arg(prg, ptr + 2, modes[1])  
        ptr += 4  
    elif opcode == 3: # input
        prg[prg[ptr + 1]] = inp.pop(0)
        ptr += 2
    elif opcode == 4: # output
        print(arg(prg, ptr + 1, modes[0]))
        ptr += 2
    elif opcode == 5: # jump-if-true
        if arg(prg, ptr + 1, modes[0]) != 0:
            ptr = arg(prg, ptr + 2, modes[1])
        else:
            ptr += 3
    elif opcode == 6: # jump-if-false
        if arg(prg, ptr + 1, modes[0]) == 0:
            ptr = arg(prg, ptr + 2, modes[1])
        else:
            ptr += 3
    elif opcode == 7: # less than
        prg[prg[ptr + 3]] = 1 if arg(prg, ptr + 1, modes[0]) < arg(prg, ptr + 2, modes[1]) else 0
        ptr += 4    

    elif opcode == 8: # equals
        prg[prg[ptr + 3]] = 1 if arg(prg, ptr + 1, modes[0]) == arg(prg, ptr + 2, modes[1]) else 0
        ptr += 4    
    else:
        print("unknown opcode ", prg[ptr])

    return ptr

def run(prg, inp):
    ptr = 0
    while ptr > -1:
        ptr = step(prg, ptr, inp)


def main():
    data = open("input.txt").read()
    prg = [ int(part) for part in data.split(",") if len(part.strip()) > 0 ]
    run(prg, [ 5 ])

main()