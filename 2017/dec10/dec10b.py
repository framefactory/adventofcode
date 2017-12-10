#!/usr/bin/python
# http://adventofcode.com/2017/day/10

def main():
    input_file = open("dec10_input.txt")
    stream = input_file.read().strip()
    lengths = [ ord(char) for char in stream if char != "\n" ]
    lengths += [ 17, 31, 73, 47, 23 ]

    lst = list(range(0, 256))
    size = len(lst)
    
    pos = 0
    skip = 0

    for r in range(0, 64):
        for length in lengths:
            n = int(length / 2)
            for i in range(0, n):
                i0 = (pos + length - i - 1) % size
                i1 = (pos + i) % size
                lst[i0], lst[i1] = lst[i1], lst[i0]

            pos += length + skip
            skip += 1

    knot_hash = ""
    for i in range(0, 16):
        checksum = 0
        for j in range(0, 16):
            checksum ^= lst[i * 16 + j]
        
        knot_hash += "%x" % checksum

    print(knot_hash)

main()
