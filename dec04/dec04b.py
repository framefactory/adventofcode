#!/usr/bin/python

def permutations(word):
    pool = tuple(word)
    n = len(pool)
    r = n
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield "".join(tuple(pool[i] for i in indices[:r]))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield "".join(tuple(pool[i] for i in indices[:r]))
                break
        else:
            return

def main():
    input_file = open("dec04a_input.txt")
    data = input_file.read()
    lines = data.split("\n")

    phrases = []
    for line in lines:
        phrase = line.split()
        if len(phrase) > 0:
            phrases.append(phrase)

    valid = 0
    for phrase in phrases:
        count = len(phrase)
        invalid = False

        for i0 in range(0, count - 1):
            perm_w0 = list(permutations(phrase[i0]))
            for i1 in range(i0 + 1, count):
                if phrase[i1] in perm_w0:
                    invalid = True
                    break
            
            if invalid:
                break

        if not invalid:
            valid += 1

    print(valid)

print(list(permutations("abcd")))
main()
