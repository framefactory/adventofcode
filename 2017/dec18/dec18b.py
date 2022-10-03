#!/usr/bin/python
# http://adventofcode.com/2017/day/18

from collections import deque

def exec(prog, regs, snd_queue, rcv_queue, pos):
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
        snd_queue.append(val1)
        regs["z"] += 1
    elif cmd == "rcv":
        if len(rcv_queue) == 0:
            return 0
        regs[op1] = rcv_queue.popleft()
    elif cmd == "jgz":
        if val1 > 0:
            return val2

    return 1

def main():
    input_file = open("dec18_input.txt")
    #input_file = open("dec18b_test.txt")
    stream = input_file.read()
    prog = [ line.split(" ") for line in stream.split("\n") if line ]
    size = len(prog)

    pos0 = 0
    pos1 = 0
    regs0 = { r: 0 for r in "abcdfipz" }
    regs1 = { r: 0 for r in "abcdfipz" }
    regs1["p"] = 1
    queue0 = deque([])
    queue1 = deque([])

    while True:
        offset0 = exec(prog, regs0, queue1, queue0, pos0)
        offset1 = exec(prog, regs1, queue0, queue1, pos1)
        if offset0 == 0 and offset1 == 0:
            break

        pos0 += offset0
        pos1 += offset1
        if pos0 < 0 or pos1 < 0 or pos0 >= size or pos1 >= size:
            break

    print(regs1["z"])

main()
