# https://adventofcode.com/2024/day/6

from pprint import pprint

with open("input.txt", "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

w = len(lines[0])
h = len(lines)

FREE = 0
UP = 1
RIGHT = 2
DOWN = 4
LEFT = 8
VISITED = 15
BLOCK = 16

base_map = [[BLOCK if lines[y][x] == "#" else FREE for x in range(w)] for y in range(h)]

for sy in range(h):
    try:
        sx = lines[sy].index("^")
        break
    except:
        continue

def trace(x, y, map, path:set=None):
    dir = UP

    while(True):
        if path is not None:
            path.add(y * w + x)
            
        if map[y][x] & dir > 0:
            return True

        map[y][x] |= dir

        if dir == UP:
            if y-1 < 0:
                return False
            if map[y-1][x] == BLOCK:
                dir = RIGHT
            else:            
                y = y - 1

        elif dir == RIGHT:
            if x+1 >= w:
                return False
            if map[y][x+1] == BLOCK:
                dir = DOWN
            else:
                x = x + 1

        elif dir == DOWN:
            if y+1 >= h:
                return False
            if map[y+1][x] == BLOCK:
                dir = LEFT
            else:
                y = y + 1

        elif dir == LEFT:
            if x-1 < 0:
                return False
            if map[y][x-1] == BLOCK:
                dir = UP
            else:
                x = x - 1


map = [ [ x for x in row ] for row in base_map ]
path = set()

trace(sx, sy, map, path)

count = 0
for y in range(h):
    for x in range(w):
        if map[y][x] & VISITED > 0:
            count += 1

print("Part 1:", count)

num_loops = 0
for pos in path:
    py = pos // w
    px = pos - py * w

    if px == sx and py == sy:
        continue

    map = [ [ x for x in row ] for row in base_map ]
    map[py][px] = BLOCK

    if trace(sx, sy, map):
        num_loops += 1

print("Part 2:", num_loops)