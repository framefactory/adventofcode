# https://adventofcode.com/2023/day/5


from pprint import pprint


with open("input.txt", "r") as file:
    line = file.readline().strip().split("seeds:")[1]
    seeds = [ int(n.strip()) for n in line.strip().split(" ") ]

    file.readline() # empty line
    mappings: list[dict[int, list[int]]] = []

    while True:
        line = file.readline().strip() # map title
        if not line:
            break

        mapping = {}
        while True:
            line = file.readline().strip()
            if not line:
                break
            rng = [ int(n.strip()) for n in line.split(" ") ]
            mapping[rng[1]] = [ rng[0], rng[2] ]
        mappings.append(mapping)


locations = []
for value in seeds:
    for mapping in mappings:
        keys = mapping.keys()
        done = False
        for src in sorted(keys):
            if value >= src and value < src + mapping[src][1]:
                value = value - src + mapping[src][0]
                break

    locations.append(value)

print("Part 1:", min(locations))

