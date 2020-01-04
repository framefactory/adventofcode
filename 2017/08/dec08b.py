#!/usr/bin/python
# http://adventofcode.com/2017/day/8

import sys

class Instruction:
    def __init__(self, line):
        parts = line.split(" ")
        self.name = parts[0]
        op = parts[1]
        self.offset = int(parts[2]) if op == "inc" else -int(parts[2])
        self.reg = parts[4]
        self.cond = parts[5]
        self.arg = int(parts[6])
        #print(self.name, self.offset, self.reg, self.cond, self.arg)

    def test(self, value):
        expr = "%d %s %d" % (value, self.cond, self.arg)
        return eval(expr)

def main():
    input_file = open("dec08a_input.txt")
    data = input_file.read()
    instructions = [ Instruction(line) for line in data.split("\n") if line ]
    registers = {}
    max_val = -sys.maxsize

    for instr in instructions:
        registers[instr.name] = 0    

    for instr in instructions:
        cond_val = registers[instr.reg]
        if instr.test(cond_val):
            reg_val = registers[instr.name] + instr.offset
            registers[instr.name] = reg_val
            max_val = max(max_val, reg_val)

    print(max_val)

main()
