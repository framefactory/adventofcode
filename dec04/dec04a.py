#!/usr/bin/python

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
            w0 = phrase[i0]
            for i1 in range(i0 + 1, count):
                if w0 == phrase[i1]:
                    invalid = True
                    break
            
            if invalid:
                break

        if not invalid:
            valid += 1

    print(valid)

main()
