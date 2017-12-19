#!/usr/bin/python
# http://adventofcode.com/2017/day/19

from functools import reduce
import re

def advance(sx, sy, x, y, dir):
    if dir == 0 and y > 0:
        return (x, y - 1)
    elif dir == 1 and x < sx - 1:
        return (x + 1, y)
    elif dir == 2 and y < sy - 1:
        return (x, y + 1)
    elif dir == 3 and x > 0:
        return (x - 1, y)

    return (-1, -1)

def turn(maze, sx, sy, x, y, dir):
    dir0 = (dir - 1) % 4
    (x0, y0) = advance(sx, sy, x, y, dir0)
    if x0 != -1 and maze[y0][x0] != " ":
        return (x0, y0, dir0)

    dir1 = (dir + 1) % 4
    (x1, y1) = advance(sx, sy, x, y, dir1)
    return (x1, y1, dir1) 


def main():
    input_file = open("dec19_input.txt")
    #input_file = open("dec19_test.txt")
    stream = input_file.read()
    maze = [ line for line in stream.split("\n") if line ]
    sy = len(maze)
    sx = len(maze[0])
    x = 0
    y = 0

    while x < sx:
        if maze[0][x] != " ":
            break
        x += 1

    chars_found = []
    steps = 0
    dir = 2

    while True:
        char = maze[y][x]

        if char == " ":
            break
        elif char == "+":
            (x, y, dir) = turn(maze, sx, sy, x, y, dir)
        else:
            if char.isalpha():
                chars_found.append(char)
            (x, y) = advance(sx, sy, x, y, dir)

        steps += 1

    print("".join(chars_found))
    print(steps)

main()
