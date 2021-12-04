#!/usr/bin/python3
# https://adventofcode.com/2021/day/3

from functools import reduce

def main():
    with open("input.txt") as input_file:
        lines = [ line.strip() for line in input_file.readlines() if len(line.strip()) > 0 ]

    num_lines = len(lines)
    num_bits = len(lines[0])

    gamma = "".join([ ('1' if sum([ 1 for line in lines if line[i] == '1' ]) >= num_lines * 0.5 else '0') for i in range(num_bits) ])
    epsilon = "".join([ '1' if x == '0' else '0' for x in gamma ])

    product = int(gamma, 2) * int(epsilon, 2)
    print(f'Part 1: {product}')

    gamma_lines_left = lines.copy()
    for i in range(num_lines):
        gamma = '1' if sum([ 1 for line in gamma_lines_left if line[i] == '1' ]) >= len(gamma_lines_left) * 0.5 else '0'
        gamma_lines_left = [ line for line in gamma_lines_left if line[i] == gamma ]
        if len(gamma_lines_left) < 2:
            break

    eps_lines_left = lines.copy()
    for i in range(num_lines):
        epsilon = '1' if sum([ 1 for line in eps_lines_left if line[i] == '1' ]) < len(eps_lines_left) * 0.5 else '0'
        eps_lines_left = [ line for line in eps_lines_left if line[i] == epsilon ]
        if len(eps_lines_left) < 2:
            break

    product = int(gamma_lines_left[0], 2) * int(eps_lines_left[0], 2)
    print(f'Part 2: {product}')


main()