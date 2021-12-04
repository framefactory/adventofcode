#!/usr/bin/python3
# https://adventofcode.com/2021/day/2

def main():
    with open("input.txt") as input_file:
        lines = [ line.strip() for line in input_file.readlines() if len(line.strip()) > 0 ]
        commands = [ line.split() for line in lines ]

        pos = 0
        depth = 0
        for command in commands:
            token = command[0]
            value = int(command[1])
            if token == "forward":
                pos += value
            elif token == "up":
                depth -= value
            elif token == "down":
                depth += value

        print(f'Part 1: pos = {pos}, depth = {depth}, result = {pos * depth}')

        pos = 0
        depth = 0
        aim = 0

        for command in commands:
            token = command[0]
            value = int(command[1])
            if token == "forward":
                pos += value
                depth += aim * value
            elif token == "up":
                aim -= value
            elif token == "down":
                aim += value

        print(f'Part 2: pos = {pos}, depth = {depth}, result = {pos * depth}')
                

main()