#!/usr/bin/python

def main():
    input_file = open("dec02a_input.txt")
    data = input_file.read()
    rows = [ sorted([ int(chunk) for chunk in line.split() if chunk.isdigit() ], reverse=True)
        for line in data.strip().split("\n") if line ]

    sum = 0
    for row in rows:
        count = len(row)
        for i in range(0, count):
            for j in range(i + 1, count):
                n0 = row[i]
                n1 = row[j]
                if n0 / n1 == int(n0 / n1):
                    sum += int(n0 / n1)

    print (sum)

    

main()
