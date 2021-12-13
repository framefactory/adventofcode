#!/usr/bin/python3
# https://adventofcode.com/2021/day/11


def main():
    with open("input.txt") as input_file:
        levels = [[0]*12] + [ [0] + [ int(c) for c in line.strip() ] + [0] for line in input_file.readlines() if len(line.strip()) > 0 ] + [[0]*12]

    flash_count = 0
    for i in range(100):
        flashes, _ = step(levels)
        flash_count += flashes

    print(f'Part 1: {flash_count}')

    with open("input.txt") as input_file:
        levels = [[0]*12] + [ [0] + [ int(c) for c in line.strip() ] + [0] for line in input_file.readlines() if len(line.strip()) > 0 ] + [[0]*12]

    step_index = 0
    while True:
        step_index += 1
        _, synced = step(levels)
        if synced:
            print(f'Part 2: {step_index}')
            break

def step(levels):
    flash_count = 0

    for y in range(1, 11):
        for x in range(1, 11):
            levels[y][x] += 1
    
    for y in range(1, 11):
        for x in range(1, 11):
            if levels[y][x] > 9:
                flash_count += flash(levels, y, x)

    sync_count = 0
    for y in range(1, 11):
        for x in range(1, 11):
            if levels[y][x] == -1:
                levels[y][x] = 0
                sync_count += 1

    return flash_count, sync_count == 100

def flash(levels, y, x):
    flash_count = 1
    levels[y][x] = -1
    for yy in range(y-1, y+2):
        for xx in range(x-1, x+2):
            if levels[yy][xx] >= 0:
                levels[yy][xx] += 1

    for yy in range(y-1, y+2):
        for xx in range(x-1, x+2):
            if xx > 0 and xx < 11 and yy > 0 and yy < 11 and levels[yy][xx] > 9:
                flash_count += flash(levels, yy, xx)

    return flash_count


if __name__ == "__main__":
    main()