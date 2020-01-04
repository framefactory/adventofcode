#!/usr/bin/python3
# https://adventofcode.com/2019/day/4#part2

def test(x):
    s = str(x)
    cc0 = 0
    same = 0
    count = 0

    for c in s:
        cc = ord(c)
        if cc < cc0:
            return 0

        if cc == cc0:
            count += 1
        else:
            if count == 1:
                same = 1
            count = 0

        cc0 = cc

    if count == 1:
        same = 1

    return same

def main():
    count = 0
    for x in range(234208, 765869 + 1):
        count += test(x)

    print(count)


main()