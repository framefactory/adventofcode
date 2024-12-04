# https://adventofcode.com/2024/day/4


def main():
    with open("input.txt", "r") as file:
        lines = [ line.strip() for line in file.readlines() if line ]

    w = len(lines[0])
    h = len(lines)

    def search(word, sx, sy, dx, dy, i=0):
        if lines[sy][sx] != word[i]:
            return 0

        i += 1
        sx += dx
        sy += dy

        if i == len(word):
            return 1

        if sx < 0 or sx >= w or sy < 0 or sy >= h:
            return 0

        return search(word, sx, sy, dx, dy, i)

    word = "XMAS"
    count = 0

    for y in range(h):
        for x in range(w):
            count += search(word, x, y,  1,  0)
            count += search(word, x, y,  1,  1)
            count += search(word, x, y,  0,  1)
            count += search(word, x, y, -1,  1)
            count += search(word, x, y, -1,  0)
            count += search(word, x, y, -1, -1)
            count += search(word, x, y,  0, -1)
            count += search(word, x, y,  1, -1)

    print("Part 1:", count)

    w1 = "MAS"
    w2 = "SAM"
    count = 0

    for y in range(h):
        for x in range(w):
            if search(w1, x, y, 1, 1) or search(w2, x, y, 1, 1):
                if search(w1, x, y+2, 1, -1) or search(w2, x, y+2, 1, -1):
                    count += 1

    print("Part 2:", count)



if __name__ == "__main__":
    main()