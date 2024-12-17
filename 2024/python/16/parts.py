# https://adventofcode.com/2024/day/16

from dataclasses import dataclass, field
from heapq import heappop, heappush
import sys 

@dataclass
class Node:
    x: int
    y: int
    code: str
    visits: list['Visit']

with open("input.txt", "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

w = len(lines[0])
h = len(lines)

maze = [[ Node(x, y, lines[y][x], []) for x in range(w) ] for y in range(h) ]

dx = [ 0, 1, 0, -1 ]
dy = [ -1, 0, 1, 0 ]

sx, sy = -1, -1
ex, ey = -1, -1
for y in range(h):
    for x in range(w):
        if maze[y][x].code == 'S':
            sx = x
            sy = y
        if maze[y][x].code == 'E':
            ex = x
            ey = y

@dataclass(order=True)
class Visit:
    node: Node = field(compare=False)
    dir: int = field(compare=False)
    cost: int = field(compare=True)
    prevs: list['Visit'] = field(compare=False)

start = maze[sy][sx]
start_visit = Visit(start, 1, 0, [])
start.visits = [ start_visit ]
queue: list[Visit] = [ start_visit ]

def find_visit(node: Node, dir: int):
    for visit in node.visits:
        if visit.dir == dir:
            return visit
    return None

while queue:
    visit = heappop(queue)
    node = visit.node

    if node.code == 'E':
        continue

    for d in [-1, 0, 1]:
        nb_dir = (visit.dir + d) % 4
        nb = maze[node.y + dy[nb_dir]][node.x + dx[nb_dir]]
        if nb.code != '#':
            nb_cost = visit.cost + (1 if d == 0 else 1001)
            nb_visit = find_visit(nb, nb_dir)
            if nb_visit:
                if nb_cost < nb_visit.cost:
                    nb_visit.cost = nb_cost
                    nb_visit.prevs = [ visit ]
                    if nb_visit not in queue:
                        heappush(queue, nb_visit)
                elif nb_cost == nb_visit.cost:
                    nb_visit.prevs.append(visit)
            else:
                nb_visit = Visit(nb, nb_dir, nb_cost, [visit])
                nb.visits.append(nb_visit)
                heappush(queue, nb_visit)


min_cost = sys.maxsize
end = maze[ey][ex]
for visit in end.visits:
    min_cost = min(min_cost, visit.cost)

pos = set()

def backtrack(visit: Visit):
    node = visit.node
    pos.add(node.y * w + node.x)
    for prev in visit.prevs:
        if prev:
            backtrack(prev)

for visit in end.visits:
    if visit.cost == min_cost:
        backtrack(visit)

print("Part 1:", min_cost)
print("part 2:", len(pos))
