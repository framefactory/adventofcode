#!/usr/bin/python

def main():
    input_file = open("dec03a_input.txt")
    data = input_file.read()
    limit = int(data)
    seq = [ 1, 1, 2, 4, 5, 10, 11 ]
    s = 3
    p = 7
    done = False

    def cell_value(p, i, s, t):
        q = p - 1 - 2 * (s - 1) - 2 * (s - 2) if t == 0 else p - 1 - s - 2 * (s - 1) - (s - 2)
        if i == 0:
            return seq[p - 1] + seq[p - 2] + seq[q] + seq[q + 1]
        elif i == s - 2:
            return seq[p - 1] + seq[q - 1] + seq[q]
        elif i == s - 1:
            return seq[p - 1] + seq[q - 1]
        else:
            return seq[p - 1] + seq[q - 1] + seq[q] + seq[q + 1]

    while not done:
        for i in range(0, s):
            seq.append(cell_value(p, i, s, 0))
            p += 1

            if seq[p-1] > limit:
                done = True
                break

        for i in range(0, s):
            seq.append(cell_value(p, i, s, 1))
            p += 1

            if seq[p-1] > limit:
                done = True
                break

        s += 1

        for i in range(0, s):
            seq.append(cell_value(p, i, s, 0))
            p += 1

            if seq[p-1] > limit:
                done = True
                break

        for i in range(0, s):
            seq.append(cell_value(p, i, s, 1))
            p += 1

            if seq[p-1] > limit:
                done = True
                break

        s += 1

    print (seq[p-2])

main()
