from utils.file import read_file_content


def move(x: int, y: int, ins: str, btns: list) -> (int, int):
    for c in ins:
        if c == 'U' and y > 0 and btns[y-1][x]:
            y -= 1
        elif c == 'D' and y < len(btns)-1 and btns[y+1][x]:
            y += 1
        elif c == 'L' and x > 0 and btns[y][x-1]:
            x -= 1
        elif c == 'R' and x < len(btns[0])-1 and btns[y][x+1]:
            x += 1
    return (x, y)


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    btns = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    (x, y) = (1, 1)
    code = ""
    for line in inp:
        (x, y) = move(x, y, line, btns)
        code += str(btns[y][x])
    return code


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    btns = [[False, False, 1, False, False], [False, 2, 3, 4, False], [5, 6, 7, 8, 9], [False, 'A', 'B', 'C', False], [False, False, 'D', False, False]]
    (x, y) = (0, 2)
    code = ""
    for line in inp:
        (x, y) = move(x, y, line, btns)
        code += str(btns[y][x])
    return code


def test_part1():
    inp = read_file_content("inputs/test")
    answer = read_file_content("inputs/ans1")

    result = solve_part1(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    inp = read_file_content("inputs/test")
    answer = read_file_content("inputs/ans2")

    result = solve_part2(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':

    inp = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(inp)))

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2(inp)))
