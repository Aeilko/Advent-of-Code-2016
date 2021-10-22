from utils.file import read_file_content


def display(field):
    screen = [None]*6
    for x in range(6):
        screen[x] = [False]*50

    for (x, y) in field:
        screen[y][x] = True

    for row in screen:
        s = "";
        for b in row:
            if b:
                s += "#"
            else:
                s += "."
        print(s)


def handle_input(lines):
    field = {}
    for line in lines:
        new_field = {}
        (cmd, param) = line.split(" ", 1)
        if cmd == "rect":
            new_field = field
            (width, height) = [int(x) for x in param.split("x")]
            # print("Rect (" + str(width) + ", " + str(height) + ")")
            for x in range(width):
                for y in range(height):
                    new_field[(x, y)] = True
        elif cmd == "rotate":
            (col, coords) = param.split(" ", 1)
            (index, value) = [int(x) for x in coords[2:].split(" by ")]
            # print("Rotate (" + col + ", " + str(index) + ", " + str(value) + ")")
            if col == "row":
                for (x, y) in field:
                    if y == index:
                        new_field[((x+value) % 50, y)] = True
                    else:
                        new_field[(x, y)] = True
            elif col == "column":
                for (x, y) in field:
                    if x == index:
                        new_field[(x, (y+value) % 6)] = True
                    else:
                        new_field[(x, y)] = True
        field = new_field
    return field


def solve_part1(inp: str) -> int:
    lines = inp.split("\n")

    field = handle_input(lines)

    return len(field)


def solve_part2(inp: str) -> int:
    lines = inp.split("\n")

    field = handle_input(lines)
    display(field)

    return -1


def test_part1():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

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
