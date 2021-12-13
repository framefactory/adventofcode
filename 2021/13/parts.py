#!/usr/bin/python3
# https://adventofcode.com/2021/day/13

import numpy as np

def main():
    with open("input.txt") as input_file:
        [ dot_part, fold_part ] = input_file.read().split("\n\n")
        dots = [ [ int(part) for part in line.strip().split(",") ] for line in dot_part.split("\n") if "," in line ]
        folds = [ line.strip().split("=") for line in fold_part.split("\n") if len(line.strip()) > 0 ]
        folds = [ (fold[0][-1], int(fold[1])) for fold in folds ]

        size_x = 0
        size_y = 0
        for dot in dots:
            size_x = max(size_x, dot[0] + 1)
            size_y = max(size_y, dot[1] + 1)

        field =[ [0] * size_x for y in range(size_y) ]
        for dot in dots:
            field[dot[1]][dot[0]] = 1

        # Part 1
        first_fold = folds[0]
        if first_fold[0] == "x":
            fold_x(first_fold[1], field, size_x, size_y)
        else:
            fold_y(first_fold[1], field, size_x, size_y)

        count = count_stars(field)
        print(f'Part 1: {count}')

        # Part 2
        sx = size_x
        sy = size_y
        for fold in folds[1:]:
            if fold[0] == "x":
                sx = fold[1]
                fold_x(sx, field, size_x, size_y)
            else:
                sy = fold[1]
                fold_y(sy, field, size_x, size_y)

        print("Part 2:")
        print_field(field, sx, sy)


def fold_x(fx, field, size_x, size_y):
    for y in range(size_y):
        for x in range(fx):
            xx = 2 * fx - x
            if xx < size_x:
                field[y][x] += field[y][xx]
        for x in range(fx + 1, size_x):
            field[y][x] = 0

def fold_y(fy, field, size_x, size_y):
    for x in range(size_x):
        for y in range(fy):
            yy = 2 * fy - y
            if yy < size_y:
                field[y][x] += field[yy][x]
        for y in range(fy, size_y):
            field[y][x] = 0

def count_stars(field):
    count = 0
    for y in range(len(field)):
        for x in range(len(field[0])):
            count += min(1, field[y][x])
    return count

def print_field(field, size_x, size_y):
    for y in range(size_y):
        print("".join([ "#" if v > 0 else " " for v in field[y][:size_x] ]))

if __name__ == "__main__":
    main()