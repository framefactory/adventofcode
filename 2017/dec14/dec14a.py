#!/usr/bin/python
# http://adventofcode.com/2017/day/14

from functools import reduce

def knot_hash(text):
    ascii = [ ord(char) for char in text ]
    ascii += [ 17, 31, 73, 47, 23 ]

    lst = list(range(0, 256))
    size = len(lst)
    pos = 0
    skip = 0

    for r in range(0, 64):
        for ch in ascii:
            n = int(ch / 2)
            for i in range(0, n):
                i0 = (pos + ch - i - 1) % size
                i1 = (pos + i) % size
                lst[i0], lst[i1] = lst[i1], lst[i0]

            pos += ch + skip
            skip += 1

    hash = []
    for i in range(0, 16):
        checksum = 0
        for j in range(0, 16):
            checksum ^= lst[i * 16 + j]
        
        hash.append(checksum)
    
    return hash

def to_binary(hash_sequence):
    return reduce(lambda s, v: s + "{0:0>8b}".format(v), hash_sequence, "")

def main():
    input_file = open("dec14_input.txt")
    key_string = input_file.read().strip()
    #key_string = "flqrgnkx"

    field = [ to_binary(knot_hash(key_string + "-" + str(i))) for i in range(128) ]
    count = reduce(lambda c, line: c + reduce(lambda c, ch: c + 1 if ch == "1" else c, line, 0), field, 0)
    print(count)

main()
