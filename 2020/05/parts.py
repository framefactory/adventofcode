#!/usr/bin/python3
# https://adventofcode.com/2020/day/5


def main():
    with open("input.txt") as input_file:
        content = input_file.read()
        
    lines = [ line.strip() for line in content.splitlines() if len(line) > 0 ]
    max_code = 0
    seats = [False] * 2048

    for line in lines:
        bin_code = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        seat_id = int(bin_code, 2)
        seats[seat_id] = True
        max_code = max(max_code, seat_id)

    print(f'Part 1: {max_code}')

    for i, seat in enumerate(seats):
        if not seat and i > 0 and i < 2047 and seats[i - 1] and seats[i + 1]:
            print(f'Part 2: {i}')
            break


main()