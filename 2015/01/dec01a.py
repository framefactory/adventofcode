#!/usr/bin/python
# http://adventofcode.com/2015/day/1

def main():
    input_file = open("dec01a_input.txt")
    data = input_file.read()

    floor = 0

    for instruction in data:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1

    print (floor)

main()
