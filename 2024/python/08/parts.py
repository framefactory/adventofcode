# https://adventofcode.com/2024/day/8

from pprint import pprint

with open("input.txt", "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

w = len(lines[0])
h = len(lines)

ants: dict[str, list] = {}

for y in range(h):
    for x in range(w):
        c = lines[y][x]
        if c != ".":
            ant = ants[c] = ants.get(c, [])
            ant.append([x, y])

nodes = []
unique_nodes = {}

for key in ants.keys():
    ant = ants[key]
    n = len(ant)
    for i in range(n):
        a1 = ant[i]
        for j in range(i + 1, n):
            a2 = ant[j]
            x1 = 2 * a2[0] - a1[0]
            x2 = 2 * a1[0] - a2[0]
            y1 = 2 * a2[1] - a1[1]
            y2 = 2 * a1[1] - a2[1]

            if x1 >= 0 and x1 < w and y1 >= 0 and y1 < h:
                nodes.append([x1, y1])
                unique_nodes[y1*w + x1] = True
            if x2 >= 0 and x2 < w and y2 >= 0 and y2 < h:
                nodes.append([x2, y2])
                unique_nodes[y2*w + x2] = True

#pprint(ants)
#pprint(nodes)

count = len(unique_nodes.keys())
print("Part 1:", count)

nodes = []
unique_nodes = {}

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for key in ants.keys():
    ant = ants[key]
    n = len(ant)
    for i in range(n):
        a1 = ant[i]
        for j in range(i + 1, n):
            a2 = ant[j]
            dx = a2[0] - a1[0]
            dy = a2[1] - a1[1]
            sx = 1 if dy == 0 else 0 if dx == 0 else dx / gcd(abs(dx), abs(dy))
            sy = 1 if dx == 0 else 0 if dy == 0 else dy / gcd(abs(dy), abs(dx))
            x = a1[0]
            y = a1[1]
            while x - sx >= 0 and x - sx < w and y - sy >= 0 and y - sy < h:
                x = x - sx
                y = y - sy

            while x >= 0 and x < w and y >= 0 and y < h:
                nodes.append([x, y])
                unique_nodes[y*w + x] = True
                x = x + sx
                y = y + sy

count = len(unique_nodes.keys())
print("Part 2:", count)
