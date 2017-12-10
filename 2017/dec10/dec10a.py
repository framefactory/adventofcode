#!/usr/bin/python
# http://adventofcode.com/2017/day/10

def main():
    input_file = open("dec10_input.txt")
    stream = input_file.read()
    lengths = [ int(part) for part in stream.split(",") if part.isdigit() ]
    
    lst = list(range(0, 256))
    size = len(lst)
    
    pos = 0
    skip = 0

    for length in lengths:
        n = int(length / 2)
        for i in range(0, n):
            i0 = (pos + length - i - 1) % size
            i1 = (pos + i) % size
            lst[i0], lst[i1] = lst[i1], lst[i0]

        pos += length + skip
        skip += 1

    print(lst[0] * lst[1])

main()
