# https://adventofcode.com/2023/day/4

from pprint import pprint


def main():
    with open("input.txt", "r") as file:
        lines = [ line.strip() for line in file.readlines() if line ]

    cards = []
    for line in lines:
        parts = line.split(":")
        p = parts[0].split(" ")
        id = int(p[-1])
        nums = [ [ int(n.strip()) for n in part.strip().split(" ") if n.strip() ] for part in parts[1].split("|") ]
        cards.append([ id, set(nums[0]), nums[1] ])

    count = 0

    for card in cards:
        score = 0
        wins = card[1]
        for have in card[2]:
            if have in wins:
                score = score * 2 if score > 0 else 1
        count += score

    print("Part 1:", count)

    def process_card(i):
        count = 1
        score = 0
        wins = cards[i][1]
        for have in cards[i][2]:
            if have in wins:
                score +=1
                count += process_card(i + score)
        return count
    
    count = 0

    for i in range(len(cards)):
        count += process_card(i)

    print("Part 2:", count)


if __name__ == "__main__":
    main()