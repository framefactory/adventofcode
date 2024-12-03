# https://adventofcode.com/2023/day/2

from pprint import pprint
import re

_re_id = r"Game (\d+):"

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    games = []
    for line in lines:
        match = re.search(_re_id, line)
        if not match:
            continue

        id = int(match.group(1))
        draws = line.split(": ")[1].split("; ")
        draws = [ [ c.strip().split(" ") for c in draw.split(", ") ] for draw in draws ]
        draws = [ { c[1]: int(c[0]) for c in draw } for draw in draws ]
        
        games.append([id, draws])

    total1 = 0
    total2 = 0
    for game in games:
        possible = True
        r_max = 0
        g_max = 0
        b_max = 0
        for draw in game[1]:
            r = draw.get("red", 0)
            r_max = max(r_max, r)
            g = draw.get("green", 0)
            g_max = max(g_max, g)
            b = draw.get("blue", 0)
            b_max = max(b_max, b)
            
            if r > 12 or g > 13 or b > 14:
                possible = False

        if possible:
            total1 += game[0]

        total2 += r_max * g_max * b_max

    print("Part 1:", total1)
    print("Part 2:", total2)


if __name__ == "__main__":
    main()