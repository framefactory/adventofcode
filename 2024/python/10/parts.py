# https://adventofcode.com/2024/day/10

with open("input.txt", "r") as file:
    lines = [ line.strip() for line in file.readlines() if line.strip() ]

map = [[ int(c) for c in line ] for line in lines ]
w = len(map[0])
h = len(map)

def search_trail(targets: set, prev: int, x: int, y: int):
    if x < 0 or x >= w or y < 0 or y >= h:
        return 0
    
    level = map[y][x]
    if level - prev != 1:
        return 0
    
    if level == 9:
        targets.add(y * w + x)
        return 1
    
    score = search_trail(targets, level, x+1, y)
    score += search_trail(targets, level, x, y+1)
    score += search_trail(targets, level, x-1, y)
    score += search_trail(targets, level, x, y-1)
    return score

score = 0
for y in range(h):
    for x in range(w):
        if map[y][x] == 0:
            targets = set()
            search_trail(targets, -1, x, y)
            score += len(targets)

print("Part 1:", score)

score = 0
for y in range(h):
    for x in range(w):
        if map[y][x] == 0:
            targets = set()
            score += search_trail(targets, -1, x, y)

print("Part 2:", score)
