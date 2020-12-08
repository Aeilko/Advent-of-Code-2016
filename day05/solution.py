from utils.file import read_file_content
from utils.crypto import md5


def solve_part1(inp: str) -> int:
    i = 0
    r = ""
    while True:
        txt = inp + str(i)
        hash = md5(txt)
        if hash[:5] == "00000":
            r += hash[5]
            if len(r) == 8:
                break
        i += 1

    return r


def solve_part2(inp: str) -> int:
    i = 0
    r = "gggggggg"
    while True:
        txt = inp + str(i)
        hash = md5(txt)
        if hash[:5] == "00000" and hash[5].isnumeric():
            j = int(hash[5])
            if 0 <= j <= 7:
                j = int(hash[5])
                if r[j] == 'g':
                    r = r[:j] + hash[6] + r[j+1:]
                    if 'g' not in r:
                        break
        i += 1

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
