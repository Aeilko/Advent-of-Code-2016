from utils.file import read_file_content


def decompress(word: str, recursive=False) -> str:
    res = 0

    i = 0
    while i < len(word):
        if word[i] == "(":
            length_string = ""
            repeat_string = ""

            # Parse '(DxD)'
            i += 1
            while word[i] != 'x':
                length_string += word[i]
                i += 1
            i += 1
            while word[i] != ')':
                repeat_string += word[i]
                i += 1
            i += 1

            # Select substring and repeat it
            length = int(length_string)
            repeat = int(repeat_string)
            if recursive:
                res += decompress(word[i:i+length], True)*repeat
            else:
                res += length*repeat

            # Set index to after the substring
            i += length
        else:
            res += 1
            i += 1

    return res


def solve_part1(inp: str) -> int:
    lines = inp.split("\n")

    res = decompress(lines[0])

    return res


def solve_part2(inp: str) -> int:
    lines = inp.split("\n")

    res = decompress(lines[0], True)

    return res


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
