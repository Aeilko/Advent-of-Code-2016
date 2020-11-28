
TEST1 = [None]*3
ANS1 = [None]*3
TEST1[0] = "R2, L3"
ANS1[0] = 5
TEST1[1] = "R2, R2, R2"
ANS1[1] = 2
TEST1[2] = "R5, L5, R5, R3"
ANS1[2] = 12

INPUT1 = "R2, L3, R2, R4, L2, L1, R2, R4, R1, L4, L5, R5, R5, R2, R2, R1, L2, L3, L2, L1, R3, L5, R187, R1, R4, L1, R5, L3, L4, R50, L4, R2, R70, L3, L2, R4, R3, R194, L3, L4, L4, L3, L4, R4, R5, L1, L5, L4, R1, L2, R4, L5, L3, R4, L5, L5, R5, R3, R5, L2, L4, R4, L1, R3, R1, L1, L2, R2, R2, L3, R3, R2, R5, R2, R5, L3, R2, L5, R1, R2, R2, L4, L5, L1, L4, R4, R3, R1, R2, L1, L2, R4, R5, L2, R3, L4, L5, L5, L4, R4, L2, R1, R1, L2, L3, L2, R2, L4, R3, R2, L1, L3, L2, L4, L4, R2, L3, L3, R2, L4, L3, R4, R3, L2, L1, L4, R4, R2, L4, L4, L5, L1, R2, L5, L2, L3, R2, L2"

TEST2 = ["R8, R4, R4, R8"]
ANS2 = [4]

INPUT2 = "R2, L3, R2, R4, L2, L1, R2, R4, R1, L4, L5, R5, R5, R2, R2, R1, L2, L3, L2, L1, R3, L5, R187, R1, R4, L1, R5, L3, L4, R50, L4, R2, R70, L3, L2, R4, R3, R194, L3, L4, L4, L3, L4, R4, R5, L1, L5, L4, R1, L2, R4, L5, L3, R4, L5, L5, R5, R3, R5, L2, L4, R4, L1, R3, R1, L1, L2, R2, R2, L3, R3, R2, R5, R2, R5, L3, R2, L5, R1, R2, R2, L4, L5, L1, L4, R4, R3, R1, R2, L1, L2, R4, R5, L2, R3, L4, L5, L5, L4, R4, L2, R1, R1, L2, L3, L2, R2, L4, R3, R2, L1, L3, L2, L4, L4, R2, L3, L3, R2, L4, L3, R4, R3, L2, L1, L4, R4, R2, L4, L4, L5, L1, R2, L5, L2, L3, R2, L2"

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


def solve_part1(input: str) -> int:
    direction = 0
    (x, y) = (0, 0)

    ins = input.split(", ")
    for i in ins:
        (x, y, direction) = move(x, y, direction, i)

    return abs(x)+abs(y)


def solve_part2(input: str) -> int:
    direction = 0
    (x, y) = (0, 0)
    visited = set()

    ins = input.split(", ")
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

    return abs(x)+abs(y)


def test_part1():
    for i in range(len(TEST1)):
        r = solve_part1(TEST1[i])
        if r != ANS1[i]:
            print("ERROR ON TEST '" + str(i) + "':\t\t" + str(r) + "\t\t" + str(ANS1[i]))
        else:
            print("Test '" + str(i) + "': ok")


def test_part2():
    for i in range(len(TEST2)):
        r = solve_part2(TEST2[i])
        if r != ANS2[i]:
            print("ERROR ON TEST '" + str(i) + "':\t\t" + str(r) + "\t\t" + str(ANS2[i]))
        else:
            print("Test '" + str(i) + "': ok")


if __name__ == '__main__':
    test_part1()

    print("\nPart 1 result:\t" + str(solve_part1(INPUT1)))

    print()
    test_part2()

    print("\nPart 2 result:\t" + str(solve_part2(INPUT2)))
