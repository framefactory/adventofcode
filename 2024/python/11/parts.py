# https://adventofcode.com/2024/day/11

from pprint import pprint

with open("input.txt", "r") as file:
    line = file.readline().strip()

stones = [ int(s.strip()) for s in line.split(" ") ]
n = len(stones)

def blink(x: int) -> tuple[int, int]:
    sx = str(x)
    x1 = None
    if x == 0:
        x = 1
    elif len(sx) % 2 == 0:
        p = len(sx) // 2
        x = int(sx[:p])
        x1 = int(sx[p:])
    else:
        x *= 2024
    return x, x1

max_steps = 75
runs: list[dict[int, int]] = [ {} for _ in range(max_steps + 1) ]

def run(x: int, steps: int):
    count = 1
    splits: list[tuple[int, int]] = []
    for i in range(steps):
        x, x1 = blink(x)
        if x1 is not None:
            splits.append((x1, steps - i - 1))

    for split in reversed(splits):
        x, steps = split
        if x not in runs[steps]:
            runs[steps][x] = run(x, steps)

        count += runs[steps][x]

    return count

count = 0
steps = 25

for x in stones:
    if x not in runs[steps]:
        runs[steps][x] = run(x, steps)
    count += runs[steps][x]

print("Part 1:", count)

count = 0
steps = 75

for x in stones:
    if x not in runs[steps]:
        runs[steps][x] = run(x, steps)
    count += runs[steps][x]

print("Part 2:", count)
