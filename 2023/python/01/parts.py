# https://adventofcode.com/2023/day/1

from pprint import pprint


_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def main():
    with open("input.txt") as file:
        lines = [ line.strip() for line in file.readlines() if line ]

    digits = [ [int(c) for c  in line if c >= '0' and c <= '9' ] for line in lines ]
    values = [ d[0] * 10 + d[-1] for d in digits if d ]
    total = sum(values)

    print("Part 1:", total)


    digits = []
    for line in lines:
        d = []
        for i in range(len(line)):
            if line[i] >= '0' and line[i] <= '9':
                d.append(int(line[i]))
            else:
                for k in _digits.keys():
                    if line[i:].startswith(k):
                        d.append(_digits[k])

        digits.append(d)

    values = [ d[0] * 10 + d[-1] for d in digits ]
    total = sum(values)

    print("Part 2:", total)

if __name__ == "__main__":
    main()