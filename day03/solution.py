from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    r = 0
    for line in inp:
        line = line.split(" ")
        nums = []
        for char in line:
            if char != '':
                nums.append(int(char))

        if nums[0]+nums[1] > nums[2] and nums[0]+nums[2] > nums[1] and nums[1] + nums[2] > nums[0]:
            r += 1

    return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    r = 0
    data = [[], [], []]
    for i in range(len(inp)+1):

        if i % 3 == 0 and i != 0:
            for j in range(3):
                if data[j][0]+data[j][1] > data[j][2] and data[j][0] + data[j][2] > data[j][1] and data[j][1] + data[j][2] > data[j][0]:
                    r += 1
            data = [[], [], []]

        if i == len(inp):
            break

        line = inp[i].split(" ")
        j = 0
        for char in line:
            if char != '':
                data[j].append(int(char))
                j += 1
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
