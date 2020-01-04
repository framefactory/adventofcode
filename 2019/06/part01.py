#!/usr/bin/python3
# https://adventofcode.com/2019/day/6

class Planet:
    def __init__(self, parent):
        self.parent = parent
        self.links = [ parent ]

    def count(self):
        count = 0
        current = self
        while current.parent != None:
            count += 1
            current = current.parent
        return count

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
            parent = planets[parent_key] = Planet(None)

        if child_key in planets:
            child = planets[child_key].parent = parent
        else:
            child = planets[child_key] = Planet(parent)

        child.links.append(parent)
        parent.links.append(child)

    count = 0
    for key in planets:
        count += planets[key].count()

    print(count)

main()