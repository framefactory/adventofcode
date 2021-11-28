#!/usr/bin/python3
# https://adventofcode.com/2020/day/6


def main():
    with open("input.txt") as input_file:
        content = input_file.read()
        
    entries = [ entry.strip() for entry in content.split("\n\n") if len(entry) > 0 ]

    sum = 0
    for entry in entries:
        questions = [0] * 26
        for c in entry:
            if c >= 'a' and c <= 'z':
                questions[ord(c) - ord('a')] = 1
        for q in questions:
            sum += q

    print(f'Part 1: {sum}')

    sum = 0
    for entry in entries:
        num_persons = len(entry.split())
        questions = [0] * 26
        for c in entry:
            if c >= 'a' and c <= 'z':
                questions[ord(c) - ord('a')] += 1
        for q in questions:
            sum += 1 if q == num_persons else 0

    print(f'Part 2: {sum}')


main()