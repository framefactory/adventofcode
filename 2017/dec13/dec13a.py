#!/usr/bin/python
# http://adventofcode.com/2017/day/13

from functools import reduce

class Layer:
    def __init__(self, line):
        parts = line.split(":")
        self.depth = int(parts[0])
        self.range = int(parts[1])

    def score(self):
        s = self.depth % ((self.range - 1) * 2)
        return self.depth * self.range if s == 0 else 0

def main():
    input_file = open("dec13_test.txt")
    stream = input_file.read()
    layers = [ Layer(line) for line in stream.split("\n") if line ]
    score = reduce(lambda score, layer: score + layer.score(), layers, 0)
    print(score)

main()
