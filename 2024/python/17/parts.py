# https://adventofcode.com/2024/day/17

import re

re_reg = r"Register \w: (\d+)"
re_prog = r"Program: (\S+)"

init_regs = [ 0, 0, 0 ]
with open("input.txt", "r") as file:
    init_regs[0] = int(re.match(re_reg, file.readline()).group(1))
    init_regs[1] = int(re.match(re_reg, file.readline()).group(1))
    init_regs[1] = int(re.match(re_reg, file.readline()).group(1))
    file.readline()
    prog = re.match(re_prog, file.readline()).group(1)
    prog = [ int(p) for p in prog.split(",") ]

def combo(regs, op: int):
    if op < 4:
        return op
    return regs[op - 4]

def step(regs, output, ip):
    oc = prog[ip]
    op = prog[ip+1]

    if oc == 0: # adv
        regs[0] = regs[0] // (2 ** combo(regs, op))
    elif oc == 1: # bxl
        regs[1] = regs[1] ^ op
    elif oc == 2: # bst
        regs[1] = combo(regs, op) % 8
    elif oc == 3: # jnz
        if regs[0] != 0:
            return op
    elif oc == 4: # bxc
        regs[1] = regs[1] ^ regs[2]
    elif oc == 5: # out
        output.append(str(combo(regs, op) % 8))
    elif oc == 6: # bdv
        regs[1] = regs[0] // (2 ** combo(regs, op))
    elif oc == 7: # cdv
        regs[2] = regs[0] // (2 ** combo(regs, op))

    return ip + 2

ip = 0
output = []
regs = [ r for r in init_regs ]
#regs[0] = 105734774294938

while True:
    if ip >= len(prog):
        break

    ip = step(regs, output, ip)

print("Part 1:", ",".join(output))

output = prog
n = len(output)

def test(A, o):
    B = (A % 8) ^ 5
    C = A // (2 ** B)
    B = B ^ C ^ 6
    return B % 8 == o 

def search(A, i):
    if i < 0:
        return A
    for a in range(8):
        AA = A * 8 + a
        if test(AA, output[i]):
            match = search(AA, i - 1)
            if match >= 0:
                return match
    return -1

A = search(0, n-1)

print("Part 2:", A)
