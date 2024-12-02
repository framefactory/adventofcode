# https://adventofcode.com/2024/day/1


def main():
    with open("input.txt", "r") as file:
        lines = [ line.strip() for line in file.readlines() if line ]
    
    lines = [ line.split("   ") for line in lines ]
    lines = [ sorted([ int(line[i]) for line in lines ]) for i in [0, 1] ]
    total = sum([ abs(line[1] - line[0]) for line in zip(lines[0], lines[1]) ])
    print("Part 1:", total)

    scores = [ n0 * len([ n1 for n1 in lines[1] if n1 == n0 ]) for n0 in lines[0] ]
    score = sum(scores)
    print("Part 2:", score)


if __name__ == "__main__":
    main()