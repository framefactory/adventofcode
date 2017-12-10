#!/usr/bin/python

def main():
    input_file = open("dec02a_input.txt")
    data = input_file.read()
    rows = [ [ int(chunk) for chunk in line.split() if chunk.isdigit() ] for line in data.split("\n") if line ]

    sum = 0
    for row in rows:
        nMin = min(row)
        nMax = max(row)
        sum += (nMax - nMin)

    print (sum)

main()
