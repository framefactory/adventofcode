#!/usr/bin/python

def main():
    input_file = open("dec03a_input.txt")
    data = input_file.read()
    number = int(data)

    x = 0
    y = 0
    s = 0
    n = 1
    done = False

    while not done:
        for i in range(0, s):
            if n == number:
                done = True
                break

            x += 1
            n += 1

        for i in range(0, s):
            if n == number:
                done = True
                break

            y += 1
            n += 1

        for i in range(0, s + 1):
            if n == number:
                done = True
                break

            x -= 1
            n += 1

        for i in range(0, s + 1):
            if n == number:
                done = True
                break

            y -= 1
            n += 1 

        s += 2

    print (abs(x) + abs(y))

main()
