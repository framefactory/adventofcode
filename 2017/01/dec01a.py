#!/usr/bin/python

def main():
    input_file = open("dec01a_input.txt")
    data = input_file.read()
    numbers = [ int(part) for part in data if part.isdigit() ] 
    size = len(numbers)

    finished = False
    pos = 0
    sum = 0

    while not finished:
        v0 = numbers[pos]
        s = 0

        while True:
            pos += 1
            if pos >= size:
                pos = 0
                finished = True

            v1 = numbers[pos]

            if v0 == v1:
                s += v1
            else:
                break

        sum += s

    print (sum)

main()
