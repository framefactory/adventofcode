#!/usr/bin/python
# http://adventofcode.com/2017/day/18

def main():
    input_file = open("dec18_input.txt")
    #input_file = open("dec18a_test.txt")
    stream = input_file.read()
    prog = [ line.split(" ") for line in stream.split("\n") if line ]
    size = len(prog)

    pos = 0
    regs = { r: 0 for r in "abfip" }
    last_played = 0

    while pos >= 0 and pos < size:
        instr = prog[pos]
        cmd = instr[0]
        op1 = instr[1]
        op2 = instr[2] if len(instr) == 3 else "a"

        val1 = regs[op1] if op1.isalpha() else int(op1)
        val2 = regs[op2] if op2.isalpha() else int(op2)

        if cmd == "set":
            regs[op1] = val2
        elif cmd == "add":
            regs[op1] += val2
        elif cmd == "mul":
            regs[op1] *= val2
        elif cmd == "mod":
            regs[op1] %= val2
        elif cmd == "snd":
            last_played = val1
        elif cmd == "rcv":
            if val1 != 0:
                print(last_played)
                break
        elif cmd == "jgz":
            if val1 > 0:
                pos = pos + val2 - 1

        pos += 1


main()
