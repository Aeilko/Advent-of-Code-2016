from utils.file import read_file_content


def is_abba(inp: str) -> bool:
    l = len(inp)
    r = False
    for i in range(l-3):
        if inp[i] == inp[i+3] and inp[i+1] == inp[i+2] and inp[i] != inp[i+1]:
            r = True
            break
    return r


def find_abas(inp: str) -> set:
    r = set()
    l = len(inp)
    for i in range(l-2):
        if inp[i] == inp[i+2] and inp[i] != inp[i+1]:
            r.add(inp[i:i+3])
    return r


# There is probably a regex solution, might want to look into that
def solve_part1(inp: str) -> int:
    lines = inp.split("\n")
    r = 0
    for line in lines:
        line = line.replace("]", "[")
        # ALl uneven groups are within hypernets
        groups = line.split("[")
        has_abba = False
        for i in range(len(groups)):
            abba = is_abba(groups[i])
            if abba:
                # print(groups[i])
                if i%2 == 0:
                    has_abba = True
                else:
                    has_abba = False
                    break
        if has_abba:
            r += 1
    return r


def solve_part2(inp: str) -> int:
    lines = inp.split("\n")
    r = 0
    for line in lines:
        line = line.replace("]", "[")
        # ALl uneven groups are within hypernets
        groups = line.split("[")

        abas = set()
        babs = set()
        for i in range(len(groups)):
            items = find_abas(groups[i])
            if i % 2 == 0:
                abas.update(items)
            else:
                bab_items = set()
                for it in items:
                    bab_items.add(it[1] + it[0] + it[1])
                babs.update(bab_items)

            if len(abas.intersection(babs)) > 0:
                r += 1
                break

    return r


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
