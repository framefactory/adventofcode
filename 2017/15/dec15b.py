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
    cand_a = []
    cand_b = []
    num_cand_a = 0
    num_cand_b = 0

    while num_cand_a < 5000000 or num_cand_b < 5000000:
        gen_a = (gen_a * 16807) % 2147483647
        gen_b = (gen_b * 48271) % 2147483647

        if gen_a & 3 == 0:
            cand_a.append(gen_a)
            num_cand_a += 1
        if gen_b & 7 == 0:
            cand_b.append(gen_b)
            num_cand_b += 1

    matches = 0

    for i in range(5000000):
        if cand_a[i] % 65536 == cand_b[i] % 65536:
            matches += 1

    print(matches)

main()
