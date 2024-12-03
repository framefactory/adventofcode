# https://adventofcode.com/2024/day/3

from pprint import pprint
import re

def main():
    with open("input.txt", "r") as file:
        lines = [ line for line in file.readlines() if line ]

    text = "".join(lines)
    valid_mul = r"mul\((\d{1,3},\d{1,3})\)"
    valid_do = r"do\(\)"
    valid_dont = r"don\'t\(\)"

    dos = [ [ match.start(), "do" ] for match in re.finditer(valid_do, text) ]
    donts = [ [ match.start(), "dont" ] for match in re.finditer(valid_dont, text) ]
    muls =[ [ match.start(), match.group(1).split(",") ] for match in re.finditer(valid_mul, text) ]
    instr = sorted(dos + donts + muls, key=lambda x: x[0])

    total = sum([ int(m[1][0]) * int(m[1][1]) for m in muls ])

    print("Part 1:", total)

    total = 0
    enabled = True
    for i in instr:
        if i[1] == "do":
            enabled = True
        elif i[1] == "dont":
            enabled = False
        elif enabled:
            total += int(i[1][0]) * int(i[1][1])

    print("Part 2:", total)

if __name__ == "__main__":
    main()