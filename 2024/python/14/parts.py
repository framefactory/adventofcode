# https://adventofcode.com/2024/day/14

import re
import copy
from dataclasses import dataclass


@dataclass
class Bot:
    p: tuple[int, int]
    v: tuple[int, int]

def quadrant_histogram(bots, size):
    scores = [ [0, 0] for y in range(2) ]
    h = [ size[0] // 2, size[1] // 2 ]
    for bot in bots:
        if bot.p[0] != h[0] and bot.p[1] != h[1]:
            scores[int(bot.p[0] // (h[0] + 0.5))][int(bot.p[1] // (h[1] + 0.5))] += 1
    return scores

def create_map(bots, size):
    lines = [ "".join([ "." for _ in range(size[0]) ]) for _ in range(size[1]) ]
    for bot in bots:
        x = bot.p[0]
        y = bot.p[1]
        lines[y] = lines[y][:x] +"X" + lines[y][x+1:]
    return lines


#s = [11, 7]
s = [101, 103]
with open("input.txt", "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

re_bot = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

bots = []
for line in lines:
    m = re.search(re_bot, line)
    bots.append(Bot([int(m.group(1)), int(m.group(2))], [int(m.group(3)), int(m.group(4))]))

bots_copy = copy.deepcopy(bots)

for i in range(100):
    for bot in bots:
        bot.p[0] = (bot.p[0] + bot.v[0]) % s[0]
        bot.p[1] = (bot.p[1] + bot.v[1]) % s[1]
        
scores = quadrant_histogram(bots, s)
score = scores[0][0] * scores[0][1] * scores[1][0] * scores[1][1]

print("Part 1:", score)

bots = bots_copy
max_dev = 0
max_index = 0

for i in range(10000):
    field = [ 0 for _ in range(s[0]) ]

    for bot in bots:
        x = bot.p[0] = (bot.p[0] + bot.v[0]) % s[0]
        y = bot.p[1] = (bot.p[1] + bot.v[1]) % s[1]

    counts = quadrant_histogram(bots, s)
    avg = (counts[0][0] + counts[0][1] + counts[1][0] + counts[1][1]) / 4
    d = max([
        abs(counts[0][0] - avg),
        abs(counts[0][1] - avg),
        abs(counts[1][0] - avg),
        abs(counts[1][1] - avg),
    ])

    if d > max_dev:
        max_dev = d
        max_index = i
        max_bots = copy.deepcopy(bots)

lines = create_map(max_bots, s)
for line in lines:
    print(line)

print(f"#{max_index}: {max_dev}\n")

print("Part 2:", max_index + 1)
