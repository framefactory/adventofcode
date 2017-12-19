#!/usr/bin/python
# http://adventofcode.com/2017/day/13

from functools import reduce

class Layer:
    def __init__(self, line):
        parts = line.split(":")
        self.depth = int(parts[0])
        self.range = int(parts[1])

    def safe_pass(self, delay):
        s = (self.depth + delay) % ((self.range - 1) * 2)
        return s > 0

def main():
    input_file = open("dec13_input.txt")
    stream = input_file.read()
    layers = [ Layer(line) for line in stream.split("\n") if line ]
    
    delay = 0
    failed = True

    while failed:
        delay += 1
        failed = False

        for layer in layers:
            if not layer.safe_pass(delay):
                failed = True
                break

    print(delay)

main()
