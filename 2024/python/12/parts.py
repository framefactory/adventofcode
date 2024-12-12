# https://adventofcode.com/2024/day/12

from pprint import pprint

with open("input.txt", "r") as file:
    plots = [ line.strip() for line in file.readlines() if line.strip() ]

w = len(plots[0])
h = len(plots)

filled = [[ False for _ in row ] for row in plots ]
borders = []

def valid(x, y):
    return x >= 0 and x < w and y >= 0 and y < h

def same(c, x, y):
    return valid(x, y) and plots[y][x] == c

def fill(border, c, x, y):
    if not same(c, x, y):
        return 0, 1
    if filled[y][x]:
        return 0, 0

    filled[y][x] = True

    a0, p0 = fill(border, c, x+1, y)
    a1, p1 = fill(border, c, x, y+1)
    a2, p2 = fill(border, c, x-1, y)
    a3, p3 = fill(border, c, x, y-1)

    if a0 == 0 or a1 == 0 or a2 == 0 or a3 == 0:
        border.append([x, y])

    area = 1 + a0 + a1 + a2 + a3
    peri = 0 + p0 + p1 + p2 + p3
    return area, peri

score = 0
for y in range(h):
    for x in range(w):
        if not filled[y][x]:
            border = []
            area, peri = fill(border, plots[y][x], x, y)
            if area > 0:
                score += area * peri
                borders.append((border, area))

print("Part 1:", score)

dx = [ 0, 1, 0, -1 ]
dy = [ -1, 0, 1, 0 ]
dbit = [ 1, 2, 4, 8 ]

score = 0
for border, area in borders:
    visited = [[ 0 for _ in row ] for row in plots ]
    sides = 0

    for p in border:
        # find start direction
        x, y = p
        c = plots[y][x]
        d = 0
        while(d < 4):
            r = (d + 1) % 4
            if visited[y][x] & dbit[d] == 0 and not same(c, x + dx[r], y + dy[r]):
                # dir not visited and right is blocked
                break
            d += 1

        if d == 4:
            # not a suitable start position
            continue
        
        steps = 0
        while visited[y][x] & dbit[d] == 0:
            visited[y][x] |= dbit[d]
            #print(f"step {steps} at ({x}, {y}) in dir {d}")

            if same(c, x + dx[d], y + dy[d]):
                # ahead free, check right
                r = (d + 1) % 4
                nx = x + dx[d] + dx[r]
                ny = y + dy[d] + dy[r]
                
                if same(c, nx, ny):
                    # at convex corner, turn right
                    d = (d + 1) % 4
                    sides += 1
                    x = nx
                    y = ny
                else:
                    # go straight
                    x += dx[d]
                    y += dy[d]

            else:
                # at concave corner, turn left
                d = (d - 1) % 4
                sides += 1

    #print(f"char: {c}, area: {area}, sides: {sides}")
    score += area * sides

print("Part 2:", score)
