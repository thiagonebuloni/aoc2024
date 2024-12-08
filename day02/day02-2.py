# from helpers.file_reaper import file_reaper

INPUT: str = "day02/input02.txt"
EXAMPLE_INPUT: str = "day02/example_input02.txt"
EXAMPLE_INPUT2: str = "day02/example_input_02-2.txt"


def check(gt_lt: str, line: list, value: int) -> bool:
    line.remove(value)
    # print(f"Removido {value}")
    if ">" in gt_lt:
        for i in range(len(line) - 1):
            if line[i] - line[i + 1] >= 0 or abs(line[i] - line[i + 1]) > 3:
                return False
    else:
        for i in range(len(line) - 1):
            if line[i] - line[i + 1] <= 0 or abs(line[i] - line[i + 1]) > 3:
                return False
    return True


def main():
    # for line_str in file_reaper(EXAMPLE_INPUT):
    safe = 0
    for line_str in open(INPUT, "r"):
        line = list(map(lambda x: int(x), line_str.split()))

        # print(line)

        difference = line[0] - line[1]
        is_ascending = difference < 0

        fail = False
        if is_ascending:
            for i in range(len(line) - 1):
                try:
                    if (
                        line[i] - line[i + 1] >= 0 and line[i + 1] - line[i + 2] >= 0
                    ) or abs(line[i] - line[i + 1]) > 3:
                        linec = line[:]
                        if not check(">", linec, linec[i]):
                            linec = line[:]
                            if not check(">", linec, linec[i + 1]):
                                print("unsafe")
                                fail = True
                                break
                except IndexError:
                    print(line)
                    print(line[i], line[i + 1])
                    # input()
            if not fail:
                safe += 1
        else:
            for i in range(len(line) - 1):
                if (
                    line[i] - line[i + 1] <= 0 and line[i + 1] - line[i + 2] <= 0
                ) or abs(line[i] - line[i + 1]) > 3:
                    linec = line[:]
                    if not check("<", linec, linec[i]):
                        linec = line[:]
                        if not check("<", linec, linec[i + 1]):
                            fail = True
                            print("unsafe")
                            break
            if not fail:
                safe += 1

    print(safe)


if __name__ == "__main__":
    main()
