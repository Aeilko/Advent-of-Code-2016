from utils.file import read_file_content


def get_counts(lines: str) -> dict:
    cols = len(lines[0])
    counts = [{} for _ in range(cols)]
    for line in lines:
        for i in range(len(line)):
            c = line[i]
            if c in counts[i]:
                counts[i][c] += 1
            else:
                counts[i][c] = 1
    return counts


def solve_part1(inp: str) -> str:
    lines = inp.split("\n")
    counts = get_counts(lines)

    r = ""
    for count in counts:
        maxChar = '.'
        maxCount = -1
        for c in count:
            if count[c] > maxCount:
                maxChar = c
                maxCount = count[c]
        r += maxChar
    return r


def solve_part2(inp: str) -> int:
    lines = inp.split("\n")
    counts = get_counts(lines)

    r = ""
    for count in counts:
        minChar = '.'
        minCount = 99999999
        for c in count:
            if count[c] < minCount:
                minChar = c
                minCount = count[c]
        r += minChar
    return r


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
