#!/usr/bin/python
# http://adventofcode.com/2015/day/2

def main():
    input_file = open("dec02a_input.txt")
    data = input_file.read()
    presents = [ present for present in data.split("\n") if len(present) > 0 ]
    ribbon_needed = 0

    for present in presents:
        edges = [ int(edge) for edge in present.split("x") ]
        volume = edges[0] * edges[1] * edges[2]
        smallest = edges.index(min(edges))
        largest = edges.index(max(edges))
        medium = 3 - smallest - largest if smallest != largest else smallest
        ribbon_needed += 2 * (edges[smallest] + edges[medium]) + volume

    print(ribbon_needed)

main()
