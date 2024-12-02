# https://adventofcode.com/2024/day/2


sign = lambda x: x and (1, -1)[x < 0]


def test_report(report):
    dir = 0
    not_safe = False
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if (dir and sign(diff) != dir) or abs(diff) < 1 or abs(diff) > 3:
            not_safe = True
            break
        dir = sign(diff)

    return not not_safe


def main():
    with open("input.txt", "r") as file:
        lines = [ line for line in file.readlines() if line ]

    reports = [ [ int(n) for n in line.split(" ") ] for line in lines ]
    
    safe_count = 0
    for report in reports:
        if test_report(report):
            safe_count += 1

    print("Part 1:", safe_count)

    safe_count = 0
    for report in reports:
        if (test_report(report)):
            safe_count += 1
        else:
            for i in range(len(report)):
                rep = [ l for j, l in enumerate(report) if i != j ]
                if (test_report(rep)):
                    safe_count += 1
                    break

    print("Part 2:", safe_count)

if __name__ == "__main__":
    main()