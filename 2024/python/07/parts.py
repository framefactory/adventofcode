# https://adventofcode.com/2024/day/7

from pprint import pprint

with open("input.txt", "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

eqs = []
for line in lines:
    parts = line.split(":")
    eq = [ int(parts[0].strip()) ]
    for num in parts[1].strip().split(" "):
        eq.append(int(num.strip()))
    eqs.append(eq)

def test_eq1(eq):
    n = len(eq) - 2
    for ops in range(2**n):
        total = eq[1]
        for i in range(n):
            total = total + eq[i + 2] if ops & (2**i) else total * eq[i + 2]
        if total == eq[0]:
            return True
        
    return False

count = 0
for eq in eqs:
    if test_eq1(eq):
        count += eq[0]

print("Part 1:", count)

def test_eq2(eq):
    n = len(eq) - 2
    for ops in range(3**n):
        total = eq[1]
        pos = 3**n
        for i in range(n):
            pos = pos // 3 # shift right
            op = ops // pos
            ops = ops - op * pos

            if op == 0:
                total = total + eq[i + 2]
            elif op == 1:
                total = total * eq[i + 2]
            else:
                total = int(str(total) + str(eq[i + 2]))
        if total == eq[0]:
            return True
        
    return False

count = 0
for eq in eqs:
    if test_eq2(eq):
        count += eq[0]

print("Part 2:", count)