# https://adventofcode.com/2023/day/3

def main():
    with open("input.txt", "r") as file:
        lines = [ line.strip() for line in file.readlines() if line ]

    w = len(lines[0])
    h = len(lines)

    def is_symbol(x, y):
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        return lines[y][x] != "." and not lines[y][x].isdigit()
    
    def check_number(x0, x1, yy):
        val = int(lines[yy][x0:x1])
        for y in range(yy - 1, yy + 2, 2):
            for x in range(x0 - 1, x1 + 1):
                if is_symbol(x, y):
                    return val
        if is_symbol(x0 - 1, yy) or is_symbol(x1, yy):
            return val
        
        return 0


    count = 0

    for y in range(h):
        in_digit = False
        for x in range(w):
            is_digit = lines[y][x].isdigit()
            if is_digit and not in_digit:
                x0 = x
                in_digit = True
            elif not is_digit and in_digit:
                x1 = x
                in_digit = False
                count += check_number(x0, x1, y)
            elif x == w - 1 and in_digit:
                x1 = w
                in_digit = False
                count += check_number(x0, x1, y)

    print("Part 1:", count)

    def is_gear(x, y):
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        return lines[y][x] == '*'

    def is_digit(x, y):
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        v = lines[y][x]
        return v.isdigit()
    
    def parse_number(x, y, nums):
        if not is_digit(x, y):
            return

        x0 = x
        while is_digit(x0 - 1, y):
            x0 -= 1
        x1 = x + 1
        while is_digit(x1, y):
            x1 += 1
        v = int(lines[y][x0:x1])
        for n in nums:
            if n[0] == x0 and n[1] == x1 and n[2] == y:
                return
        nums.append([x0, x1, y, v])
    
    count = 0
    for y in range(h):
        for x in range(w):
            if is_gear(x, y):
                nums = []
                for yy in range(y-1, y+2):
                    for xx in range(x-1, x+2):
                        parse_number(xx, yy, nums)

                if len(nums) == 2:
                    count += nums[0][3] * nums[1][3]

    print("Part 2:", count)



if __name__ == "__main__":
    main()