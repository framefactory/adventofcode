#!/usr/bin/python3
# https://adventofcode.com/2021/day/12

from dataclasses import dataclass
from typing import List, Dict, Set

@dataclass
class Node:
    name: str
    edges: List['Node']
    is_small: bool

    def __repr__(self):
        return f'{self.name}{"[s]" if self.is_small else ""} ({", ".join([ e.name for e in self.edges.values() ])})'

def main():
    with open("input.txt") as input_file:
        lines = [ line.strip() for line in input_file.readlines() if len(line.strip()) > 0 ]

    nodes: Dict[str, Node] = {}

    for line in lines:
        edge: List[str] = line.split("-")
        node0 = nodes[edge[0]] if edge[0] in nodes else Node(edge[0], [], edge[0].islower())
        node1 = nodes[edge[1]] if edge[1] in nodes else Node(edge[1], [], edge[1].islower())
        if node1 not in node0.edges:
            node0.edges.append(node1)
        if node0 not in node1.edges:
            node1.edges.append(node0)
        nodes[edge[0]] = node0
        nodes[edge[1]] = node1

    for node in nodes.values():
        node.edges.sort(key=lambda node: node.name)

    paths1: Set[str] = set()
    search(nodes, paths1, [], nodes["start"], twice_node=None)
    print(f'Part 1: {len(paths1)}')

    paths2: Set[str] = set()
    for node in nodes.values():
        if node == "start" or node == "end":
            continue
        paths = set()
        search(nodes, paths, [], nodes["start"], twice_node=node)
        paths2 |= paths

    print(f'Part 2: {len(paths2)}')

def search(nodes: Dict[str, Node], paths: Set[str], path: List[Node], node: Node, twice_node: Node) -> str:
    path.append(node)

    if node.name == "end":
        paths.add(",".join([ n.name for n in path ]))
        return

    for edge in node.edges:
        if edge.name == "start":
            continue
        if edge.is_small and edge in path:
            if edge != twice_node or path.count(edge) > 1:
                continue
        
        search(nodes, paths, path.copy(), edge, twice_node)
    

if __name__ == "__main__":
    main()