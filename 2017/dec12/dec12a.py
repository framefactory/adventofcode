#!/usr/bin/python
# http://adventofcode.com/2017/day/12

import functools

graph = None

class Vertex:
    def __init__(self, line):
        parts = line.split("<->")
        self.index = int(parts[0])
        self.adj_list = [ int(v) for v in parts[1].split(",") if v ]
        self.visited = 0

def depth_first_visit(i):
    v = graph[i]
    if v.visited:
        return

    v.visited = True
    for j in v.adj_list:
        depth_first_visit(j)

def main():
    input_file = open("dec12_input.txt")
    stream = input_file.read()
    vertices = [ Vertex(line) for line in stream.split("\n") if line ]
    max_index = functools.reduce(lambda max_index, v: max(max_index, v.index), vertices, 0)

    global graph
    graph = [ None for i in range(max_index + 1) ]
    for v in vertices:
        graph[v.index] = v

    depth_first_visit(0)
    count = functools.reduce(lambda count, v: count + 1 if v and v.visited else count, graph, 0)
    print(count)

main()
