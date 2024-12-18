# https://adventofcode.com/2024/day/17

from dataclasses import dataclass, field
from heapq import heappop, heappush
import sys

# file_name = "test.txt"
# size = 6 + 1
# count = 12

file_name = "input.txt"
size = 70 + 1
count = 1024

with open(file_name, "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

pos = [[ int(n) for n in line.split(",") ] for line in lines ]

FREE = sys.maxsize - 1
BLOCKED = sys.maxsize

dx = [ 0, 1, 0, -1 ]
dy = [ -1, 0, 1, 0 ]

@dataclass(order=True)
class Node:
    x: int = field(compare=False)
    y: int = field(compare=False)
    cost: int = field(compare=True)


map: list[list[int]] = [[ FREE for _ in range(size) ] for _ in range(size) ]

for i in range(count):
    map[pos[i][1]][pos[i][0]] = BLOCKED


def solve(map):
    map[0][0] = 0 
    queue: list[Node] = [ Node(0, 0, 0) ]
    
    while queue:
        node = heappop(queue)

        if node.x == size - 1 and node.y == size - 1:
            return node.cost

        for d in range(4):
            xx = node.x + dx[d]
            yy = node.y + dy[d]
            if xx < 0 or xx >= size or yy < 0 or yy >= size:
                continue
            nb_cost = map[yy][xx]
            if nb_cost == BLOCKED:
                continue
            if node.cost + 1 < nb_cost:
                map[yy][xx] = node.cost
                if not any([ n.x == xx and n.y == yy for n in queue ]):
                    heappush(queue, Node(xx, yy, node.cost + 1))

    return 0

cost = solve(map)
print("Part 1:", cost)

solution = ""
for n in range(count, len(pos)):
    map: list[list[int]] = [[ FREE for _ in range(size) ] for _ in range(size) ]

    for i in range(n):
        map[pos[i][1]][pos[i][0]] = BLOCKED

    cost = solve(map)
    if cost == 0:
        solution = ",".join([str(x) for x in pos[n-1]])
        break
    
print("Part 2:", solution)