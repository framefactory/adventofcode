#!/usr/bin/python3
# https://adventofcode.com/2021/day/8

from functools import reduce

def main():
    with open("input.txt") as input_file:
        displays = [ "".join(line.strip().split(" |")) for line in input_file.readlines() if len(line.strip()) > 0 ]
        displays = [ [ digit.strip() for digit in disp.split(" ") ] for disp in displays ]
        num_displays = len(displays)

        count = 0   
        for display in displays:
            for digit in display[10:]:
                n = len(digit)
                if n == 2 or n == 3 or n == 4 or n == 7:
                    count += 1

        print(f'Part 1: {count}')

        count = 0
        for display in displays:
            count += solve(display)

        print(f'Part 2: {count}')

def solve(digits):
    da = sorted(digits[:10], key=len)
    res = [""] * 10
    res[1] = da[0]
    res[4] = da[2]
    res[7] = da[1]
    res[8] = da[9]
    da_235 = [da[3], da[4], da[5]]
    da_069 = [da[6], da[7], da[8]]
    res[3] = first_match(da_235, lambda e: is_contained(res[1], e))
    res[6] = first_match(da_069, lambda e: not is_contained(res[1], e))
    res[5] = first_match(da_235, lambda e: e != res[3] and is_contained(e, res[6]))
    res[2] = first_match(da_235, lambda e: e != res[3] and e != res[5])
    res[9] = first_match(da_069, lambda e: e != res[6] and is_contained(res[5], e))
    res[0] = first_match(da_069, lambda e: e != res[6] and e != res[9])

    num = 0
    for di, d in enumerate(digits[10:]):
        for i in range(10):
            if is_equal(d, res[i]):
                num += i * (10 ** (3 - di))
                break

    #print(res, num)
    
    return num


def first_match(list, func):
    for e in list:
        if func(e):
            return e 

def is_equal(da, db):
    return len(da) == len(db) and num_shared(da, db) == len(da)

def is_contained(da, db):
    return num_shared(da, db) == len(da)

def shared(da, db):
    return "".join([ sa for sa in da if sa in db ])

def num_shared(da, db):
    return len(shared(da, db))

main()