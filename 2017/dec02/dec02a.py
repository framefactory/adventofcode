#!/usr/bin/python

def main():
    input_file = open("dec02a_input.txt")
    data = input_file.read()
    lines = data.split("\n")
    rows = []

    for line in lines:
        row = [ int(chunk) for chunk in line.split() if chunk.isdigit() ]
        if len(row) > 0:
            rows.append(row)

    sum = 0
    for row in rows:
        nMin = min(row)
        nMax = max(row)
        sum += (nMax - nMin)

    print (sum)

    

main()
