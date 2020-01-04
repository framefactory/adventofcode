#!/usr/bin/python
# http://adventofcode.com/2017/day/7

import re

def main():
    input_file = open("dec07a_input.txt")
    data = input_file.read()
    lines = [ line for line in data.split("\n") if line ]

    names = [ re.search("(\w+)", line).group(1) for line in lines ]
    weights = [ int(re.search("\s\((\d+)\)", line).group(1)) for line in lines ]
    childrens = [ re.search("-\>\W(.+)", line) for line in lines ]
    childrens = [ children.group(1).split(", ") if children != None else [] for children in childrens ]

    inner_nodes = []
    for children in childrens:
        inner_nodes += children

    for name in names:
        if name not in inner_nodes:
            print(name)
    

main()
