#!/usr/bin/python

def main():
    input_file = open("dec01a_input.txt")
    data = input_file.read()

    numbers = []
    for c in data:
        if c.isdigit():
            numbers.append(int(c))

    count = len(numbers)
    offset = int(count / 2)

    finished = False
    pos = 0
    sum = 0

    for pos in range(0, offset):
        v0 = numbers[pos]
        v1 = numbers[(pos + offset) % count]
        if v0 == v1:
            sum += v0 + v1

    print (sum)

main()
