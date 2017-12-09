#!/usr/bin/python

def main():
    input_file = open("dec02a_input.txt")
    data = input_file.read()
    lines = data.split("\n")
    rows = []

    for line in lines:
        row = [ int(chunk) for chunk in line.split() if chunk.isdigit() ]
        if len(row) > 0:
            row.sort(reverse=True)
            rows.append(row)

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
