from utils.file import read_file_content


def move(x: int, y: int, direction: int, move: str) -> (int, int, int):
    m = move[0]
    steps = int(move[1:])
    if m == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction + 3) % 4

    if direction == 0:
        y += steps
    elif direction == 1:
        x += steps
    elif direction == 2:
        y -= steps
    elif direction == 3:
        x -= steps

    return (x, y, direction)


def solve_part1(inp: str) -> int:
    direction = 0
    (x, y) = (0, 0)

    ins = inp.split(", ")
    for i in ins:
        (x, y, direction) = move(x, y, direction, i)

    return abs(x)+abs(y)


def solve_part2(inp: str) -> int:
    direction = 0
    (x, y) = (0, 0)
    visited = set()

    ins = inp.split(", ")
    found = False
    for i in ins:
        m = i[0]
        steps = int(i[1:])
        if m == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4

        for i in range(steps):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1

            if (x, y) in visited:
                found = True
                break
            visited.add((x, y))

        if found:
            break

    return abs(x)+abs(y) if found else -1


def test_part1():
    inputs = read_file_content("inputs/test").strip().split("\n")
    answers = read_file_content("inputs/ans1").strip().split("\n")

    for i in range(len(inputs)):
        inp = inputs[i]
        answer = int(answers[i])
        result = solve_part1(inp)
        if result == answer:
            print("Test successful")
        else:
            print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    inputs = read_file_content("inputs/test").strip().split("\n")
    answers = read_file_content("inputs/ans2").strip().split("\n")

    for i in range(len(inputs)):
        inp = inputs[i]
        answer = int(answers[i])
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
