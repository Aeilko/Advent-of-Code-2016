import re

from utils.file import read_file_content
from utils.string import count_char_occurances


def sort_dict(d: dict):
    return sorted(d.items(), key=lambda x: (-x[1], x[0]))


def decrypt(cipher: str, shift: int):
    shift = shift % 26
    plain = ""
    for c in cipher:
        if c == '-':
            plain += ' '
        else:
            plain += chr(((ord(c)-ord('a')+shift) % 26)+ord('a'))
    return plain


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    r = 0
    for line in inp:
        (name, settings) = line.rsplit("-", 1)
        (settings, sid, check) = re.search("((\d+)\[([\w]{5})\])", settings).groups()

        occs = count_char_occurances(name)
        del occs['-']
        sorted_occs = sort_dict(occs)

        checksum = ""
        for i in range(5):
            checksum += sorted_occs[i][0]

        if checksum == check:
            r += int(sid)

    return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    for line in inp:
        (name, settings) = line.rsplit("-", 1)
        (settings, sid, check) = re.search("((\d+)\[([\w]{5})\])", settings).groups()
        plain = decrypt(name, int(sid))

        if plain == "northpole object storage":
            return int(sid)

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
