#!/usr/bin/python3
# https://adventofcode.com/2021/day/4


def main():
    with open("input.txt") as input_file:
        blocks = [ block.strip() for block in input_file.read().split("\n\n") if len(block.strip()) > 0 ]

    draws = [ int(n.strip()) for n in blocks[0].split(",") ]

    board_nums = [ [ [ int(n.strip()) for n in line.split(" ") if len(n.strip()) > 0 ] for line in block.split("\n") ] for block in blocks[1:] ]

    num_boards = len(board_nums)
    num_rows = len(board_nums[0])
    num_cols = len(board_nums[0][0])

    board_marks = [ [ [0] * num_cols for r in range(num_rows) ] for n in range(num_boards) ]
    board_won = [0] * num_boards
    first_win = False

    for i, d in enumerate(draws):
        for j, (bn, bm) in enumerate(zip(board_nums, board_marks)):
            for r in range(num_rows):
                for c in range(num_cols):
                    if d == bn[r][c]:
                        bm[r][c] = 1

            if check_win(bm, num_rows, num_cols):
                sum_unmarked = 0             
                for r in range(num_rows):
                    for c in range(num_cols):
                        if bm[r][c] == 0:
                            sum_unmarked += bn[r][c]

                board_won[j] = 1
                if sum(board_won) == num_boards:
                    print(f'Part 2: {sum_unmarked * d}')
                    return

                if not first_win:
                    first_win = True
                    print(f'Part 1: {sum_unmarked * d}')



def check_win(board, num_rows, num_cols):
    for r in range(num_rows):
        if sum(board[r]) == num_cols:
            return True

    for c in range(num_cols):
        score = 0
        for r in range(num_rows):
            score += board[r][c]
        if score == num_rows:
            return True

    return False



main()