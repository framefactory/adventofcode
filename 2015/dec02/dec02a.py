#!/usr/bin/python
# http://adventofcode.com/2015/day/2

def main():
    input_file = open("dec02a_input.txt")
    data = input_file.read()
    presents = [ present for present in data.split("\n") if len(present) > 0 ]
    paper_needed = 0

    for present in presents:
        edges = [ int(edge) for edge in present.split("x") ]
        areas = [ edges[0] * edges[1], edges[0] * edges[2], edges[1] * edges[2] ]
        smallest_area = min(areas)
        paper_needed += 2 * (areas[0] + areas[1] + areas[2]) + smallest_area 

    print(paper_needed)

main()
