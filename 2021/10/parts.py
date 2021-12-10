#!/usr/bin/python3
# https://adventofcode.com/2021/day/10

OPEN_TOKENS = "([{<"
CLOSE_TOKENS = ")]}>"
SCORES = [ 3, 57, 1197, 25137 ]

def main():
    with open("input.txt") as input_file:
        lines = [ line.strip() for line in input_file.readlines() if len(line.strip()) > 0 ]

    score = 0
    for line in lines:
        score += get_corruption_score(line)

    print(f'Part 1: {score}')

    inc_lines = [ line for line in lines if get_corruption_score(line) == 0 ]

    scores = []
    for line in inc_lines:
        scores.append(get_closing_score(line))

    scores.sort()
    score = scores[len(scores) // 2]

    print(f'Part 2: {score}')

def get_closing_score(line):
    stack = []
    for c in line:
        i = OPEN_TOKENS.find(c)
        if i >= 0:
            stack.append(i)
        else:
            stack.pop()

    score = 0
    remainder = ""
    while len(stack) > 0:
        i = stack.pop()
        remainder += CLOSE_TOKENS[i]
        score = score * 5 + i + 1  
    
    return score

def get_corruption_score(line):
    stack = []
    for c in line:
        i = OPEN_TOKENS.find(c)
        if i >= 0:
            stack.append(i)
        else:
            i = stack.pop() if len(stack) > 0 else -1
            j = CLOSE_TOKENS.find(c)
            if i != j:
                return SCORES[j]            
    
    return 0


main()