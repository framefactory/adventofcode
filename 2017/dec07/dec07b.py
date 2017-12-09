#!/usr/bin/python
# http://adventofcode.com/2017/day/7

import re

def main():
    input_file = open("dec07a_input.txt")
    data = input_file.read()
    lines = [ line for line in data.split("\n") if len(line) > 0 ]
    nodes = {}

    for line in lines:
        name = re.search("(\w+)", line).group(1)
        weight = int(re.search("\s\((\d+)\)", line).group(1))
        children = re.search("-\>\W(.+)", line)
        children = children.group(1).split(", ") if children != None else []
        nodes[name] = { "name": name, "weight": weight, "children": children }

    inner_nodes = []
    root_name = ""

    for name, node in nodes.items():
        inner_nodes += node["children"]

    for name in nodes:
        if name not in inner_nodes:
            root_name = name

    get_weight(nodes, nodes[root_name])


def get_weight(nodes, node):
    weight = node["weight"]

    children = node["children"]
    if not children:
        return weight

    weights = [ get_weight(nodes, nodes[child_name]) for child_name in children ]
    min_weight = min(weights)
    max_weight = max(weights)

    if min_weight != max_weight:
        min_count = weights.count(min_weight)
        max_count = weights.count(max_weight)
        index = 0

        if min_count < max_count:
            diff = max_weight - min_weight
            index = weights.index(min_weight)
        else:
            diff = min_weight - max_weight
            index = weights.index(max_weight)
        
        print(nodes[children[index]]["weight"] + diff)
        exit(0)
    
    return weight + sum(weights)   


main()
