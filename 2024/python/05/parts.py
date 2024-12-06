# https://adventofcode.com/2024/day/5

from pprint import pprint
from functools import cmp_to_key

with open("input.txt", "r") as file:
    rules: dict[str, set] = {}
    while True:
        line = file.readline().strip()
        if not line:
            break
        pages = [ int(item) for item in line.split("|") ]
        rule = rules.get(pages[0], set())
        rule.add(pages[1])
        rules[pages[0]] = rule

    updates = []
    while True:
        line = file.readline()
        if not line:
            break
        updates.append([ int(item) for item in line.strip().split(",")])

score = 0
unordered = []
for update in updates:
    n = len(update)
    wrong_order = False
    for i in range(n):
        page = update[i]
        rule = rules.get(page, None)
        if rule:
            for j in range(i):
                if update[j] in rule:
                    wrong_order = True
                    break
        if wrong_order:
            break
    
    if wrong_order:
        unordered.append(update)
    else:
        score += update[n // 2]

print("Part 1:", score)

def compare(p0, p1):
    rule = rules.get(p0, None)
    if rule and p1 in rule:
        return 1
    rule = rules.get(p1, None)
    if rule and p0 in rule:
        return -1
    return 0

score = 0
for update in unordered:
    update = sorted(update, key=cmp_to_key(compare))
    score += update[len(update) // 2]

print("Part 2:", score)