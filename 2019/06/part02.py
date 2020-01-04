#!/usr/bin/python3
# https://adventofcode.com/2019/day/6#part2

class Planet:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.links = [ parent ]

    def count(self):
        count = 0
        current = self
        while current.parent != None:
            count += 1
            current = current.parent
        return count

    def get_chain(self):
        chain = []
        current = self
        while current.parent != None:
            chain.append(current.parent)
            current = current.parent
        return chain

def main():
    lines = open("input.txt").readlines()
    planets = {}

    for line in lines:
        keys = [ key.strip() for key in line.split(")") ]    
        parent_key, child_key = keys

        parent = None
        child = None

        if parent_key in planets:
            parent = planets[parent_key]
        else:
            parent = planets[parent_key] = Planet(parent_key, None)

        if child_key in planets:
            child = planets[child_key].parent = parent
        else:
            child = planets[child_key] = Planet(child_key, parent)

        child.links.append(parent)
        parent.links.append(child)

    san_chain = planets["SAN"].get_chain()
    you_chain = planets["YOU"].get_chain()

    for si in range(0, len(san_chain)):
        for yi in range(0, len(you_chain)):
            if san_chain[si] == you_chain[yi]:
                print(si + yi)
                return

main()