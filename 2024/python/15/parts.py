# https://adventofcode.com/2024/day/15

dirs = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3,
}

dx = [ 0, 1, 0, -1 ]
dy = [ -1, 0, 1, 0 ]

map = []

with open("input.txt", "r") as file:
    y = 0
    while True:
        line = file.readline().strip()
        if not line:
            break
        try:
            sx = line.index("@")
            sy = y
        except:
            pass
        map.append([c for c in line])
        y += 1

    lines = ""
    while True:
        line = file.readline().strip()
        if not line:
            break
        lines += line

    moves = [ dirs[m] for m in lines ]

tf = { "#": "##", "O": "[]", ".": "..", "@": "@." }
map2 = []
for line in map:
    line2 = []
    for c in line:
        t = tf[c]
        line2.append(t[0])
        line2.append(t[1])
    map2.append(line2)

w = len(map[0])
h = len(map)

def move(x, y, dir):
    xx = x + dx[dir]
    yy = y + dy[dir]

    if map[yy][xx] == '#':
        return False
    if map[yy][xx] == 'O':
        move(xx, yy, dir)
    
    if map[yy][xx] == '.':
        map[yy][xx] = map[y][x]
        map[y][x] = "."
        return True

x = sx
y = sy
for dir in moves:
    if move(x, y, dir):
        x += dx[dir]
        y += dy[dir]

score = 0
for y in range(h):
    for x in range(w):
        if map[y][x] == 'O':
            score += 100 * y + x

# for line in map:
#     print("".join(line))

print("Part 1:", score)

w = len(map2[0])
h = len(map2)

def move2(x, y, dir, do_move: bool):
    xx = x + dx[dir]
    yy = y + dy[dir]

    if map2[yy][xx] == '#':
        can_move = False

    elif map2[yy][xx] == '[':
        if dir == 0 or dir == 2:
            can_move = move2(xx, yy, dir, do_move) and move2(xx+1, yy, dir, do_move)
        else:
            can_move = move2(xx, yy, dir, do_move)
    if map2[yy][xx] == "]":
        if dir == 0 or dir == 2:
            can_move = move2(xx-1, yy, dir, do_move) and move2(xx, yy, dir, do_move)
        else:
            can_move = move2(xx, yy, dir, do_move)
    
    if map2[yy][xx] == ".":
        can_move = True
        if do_move:
            map2[yy][xx] = map2[y][x]
            map2[y][x] = "."

    return can_move

x = sx * 2
y = sy
for dir in moves:
    if move2(x, y, dir, False):
        move2(x, y, dir, True)
        x += dx[dir]
        y += dy[dir]

score = 0
for y in range(h):
    for x in range(w):
        if map2[y][x] == '[':
            score += 100 * y + x

# for line in map2:
#     print("".join(line))

print("Part 2:", score)