# https://adventofcode.com/2024/day/9

from dataclasses import dataclass
from pprint import pprint
import copy

@dataclass
class Chunk:
    id: int
    length: int

FREE = -1

with open("input.txt", "r") as file:
    line = file.readline().strip()

fs: list[Chunk] = []

for i in range(0, len(line), 2):
    length = int(line[i])
    if length > 0:
        file = Chunk(i // 2, length)
        fs.append(file)

    if i + 1 < len(line):
        length = int(line[i+1])
        if length > 0:
            fs.append(Chunk(FREE, length))

fs_copy = copy.deepcopy(fs)

done = False
while not done:
    while fs[-1].id == FREE:
        fs.pop(-1)
    
    for i in range(0, len(fs) - 1):
        if fs[i].id == FREE and fs[i+1].id != FREE:
            used = fs[-1].length
            free = fs[i].length
            fs[i].id = fs[-1].id
            if free >= used:
                fs[i].length = used
                fs.pop(-1)
                if free - used > 0:
                    fs.insert(i+1, Chunk(FREE, free - used))
            else:
                fs[-1].length -= free
            break

        elif i == len(fs) - 2:
            done = True

pos = 0
sum = 0
for i in range(len(fs)):
    for j in range(fs[i].length):
        sum += fs[i].id * pos
        pos += 1

print("Part 1:", sum)

fs = fs_copy
files = [ f for f in fs if f.id != FREE ]
files.sort(key=lambda file: file.id, reverse=True)

done = False
for j in range(len(files)):
    # merge free blocks
    i = 0
    while i < len(fs) - 1:
        if fs[i].id == FREE and fs[i+1].id == FREE:
            fs[i].length += fs[i+1].length
            fs.pop(i+1)
        else:
            i += 1

    file = files[j]
    used = file.length

    for i in range(len(fs)):
        if fs[i] == file:
            break

        free = fs[i].length
        if fs[i].id == FREE and free >= used:
            fs[i].id = file.id
            fs[i].length = used
            file.id = FREE
            if free - used > 0:
                fs.insert(i+1, Chunk(FREE, free - used))
            break

pos = 0
sum = 0
for i in range(len(fs)):
    if fs[i].id == FREE:
        pos += fs[i].length
    else:
        for j in range(fs[i].length):
            sum += fs[i].id * pos
            pos += 1

print("Part 2:", sum)