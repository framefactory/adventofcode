# https://adventofcode.com/2024/day/13

import re
from dataclasses import dataclass
from pprint import pprint

with open("input.txt", "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

re_button = r"X\+(\d+), Y\+(\d+)"
re_prize = r"X=(\d+), Y=(\d+)"

@dataclass
class Game:
    a: tuple[int, int]
    b: tuple[int, int]
    p: tuple[int, int]

games = []
for i in range(0, len(lines), 3):
    a = re.search(re_button, lines[i])
    b = re.search(re_button, lines[i+1])
    p = re.search(re_prize, lines[i+2])

    games.append(Game(
        [int(a.group(1)), int(a.group(2))],
        [int(b.group(1)), int(b.group(2))],
        [int(p.group(1)), int(p.group(2))],
    ))

score = 0
for g in games:
    d = g.a[0]*g.b[1] - g.a[1]*g.b[0]
    x = (g.p[0]*g.b[1] - g.p[1]*g.b[0]) / d
    y = (g.p[1]*g.a[0] - g.p[0]*g.a[1]) / d
    if x == int(x) and y == int(y):
        score += int(x*3 + y)

print("Part 1:", score)

score = 0
for g in games:
    p0 = g.p[0] + 10000000000000
    p1 = g.p[1] + 10000000000000

    d = g.a[0]*g.b[1] - g.a[1]*g.b[0]
    x = (p0*g.b[1] - p1*g.b[0]) / d
    y = (p1*g.a[0] - p0*g.a[1]) / d
    if x == int(x) and y == int(y):
        score += int(x*3 + y)

print("Part 2:", score)