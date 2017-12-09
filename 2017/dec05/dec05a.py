#!/usr/bin/python

def main():
    input_file = open("dec05a_input.txt")
    data = input_file.read()

    program = [ int(line.strip()) for line in data.split("\n") if len(line.strip()) > 0 ]
    #program = [ 0, 3, 0, 1, -3 ]

    size = len(program)
    pc = 0
    steps = 0

    while pc >= 0 and pc < size:
        pc_0 = pc
        pc = pc + program[pc]
        program[pc_0] += 1
        steps += 1

    print(steps)

main()
