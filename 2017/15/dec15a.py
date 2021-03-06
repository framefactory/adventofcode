#!/usr/bin/python
# http://adventofcode.com/2017/day/15

from functools import reduce
import re

def main():
    input_file = open("dec15_input.txt")
    stream = input_file.read()
    seeds = [ int(part) for part in re.findall("\d+", stream) ]
    #seeds = [ 65, 8921 ]

    gen_a = seeds[0]
    gen_b = seeds[1]
    matches = 0

    for i in range(40000000):
        gen_a = (gen_a * 16807) % 2147483647
        gen_b = (gen_b * 48271) % 2147483647
        
        if gen_a % 65536 == gen_b % 65536:
            matches += 1

    print(matches)

main()
