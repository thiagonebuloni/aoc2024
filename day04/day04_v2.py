from pathlib import Path

pwd = Path(__file__).parent

INPUT: Path = pwd / "input04.txt"
EXAMPLE: Path = pwd / "example_input04.txt"


file = INPUT.open("r")
lines = file.readlines()
count = 0
directions = {}


def check_horizontal_right(lines, count, line, row) -> int:
    if "XMAS" in lines[line][row : row + 4]:
        count += 1
        print(f"horizontal right: {count}")
    return count


def check_horizontal_left(lines, count, line, row) -> int:
    if "SAMX" in lines[line][row : row + 4]:
        count += 1
        print(f"horizontal left: {count}")
    return count


def check_vertical_down(lines, count, line, row) -> int:
    if (
        "X" in lines[line][row]
        and "M" in lines[line + 1][row]
        and "A" in lines[line + 2][row]
        and "S" in lines[line + 3][row]
    ):
        count += 1
        print(f"vertical down: {count}")
    return count


def check_vertical_up(lines, count, line, row) -> int:
    if (
        "S" in lines[line][row]
        and "A" in lines[line + 1][row]
        and "M" in lines[line + 2][row]
        and "X" in lines[line + 3][row]
    ):
        count += 1
        print(line, row)
        print(line + 1, row)
        print(line + 2, row)
        print(line + 3, row)
        print(f"vertical up: {count}")
    return count


def check_diagonal_down_right(lines, count, line, row) -> int:
    try:
        if (
            "X" in lines[line][row]
            and "M" in lines[line + 1][row + 1]
            and "A" in lines[line + 2][row + 2]
            and "S" in lines[line + 3][row + 3]
        ):
            count += 1
            print(f"diagonal down right: {count}")
    except IndexError:
        return count
    return count


def check_diagonal_down_left(lines, count, line, row) -> int:
    try:
        if (
            "X" in lines[line][row]
            and "M" in lines[line + 1][row - 1]
            and "A" in lines[line + 2][row - 2]
            and "S" in lines[line + 3][row - 3]
        ):
            count += 1
            print(f"diagonal down left: {count}")
    except IndexError:
        return count
    return count


def check_diagonal_up_right(lines, count, line, row) -> int:
    try:
        if (
            "S" in lines[line][row]
            and "A" in lines[line + 1][row + 1]
            and "M" in lines[line + 2][row + 2]
            and "X" in lines[line + 3][row + 3]
        ):
            count += 1
            print(f"diagonal up right: {count}")
    except IndexError:
        return count
    return count


def check_diagonal_up_left(lines, count, line, row) -> int:
    try:
        if (
            # line > 3
            # and row > 3
            "S" in lines[line][row]
            and "A" in lines[line + 1][row - 1]
            and "M" in lines[line + 2][row - 2]
            and "X" in lines[line + 3][row - 3]
        ):
            count += 1
            print(f"diagonal up left: {count}")
    except IndexError:
        return count
    return count


for line in range(len(lines)):
    for row in range(len(lines)):
        count = check_horizontal_right(lines, count, line, row)
        count = check_horizontal_left(lines, count, line, row)

for line in range(len(lines) - 3):
    for row in range(len(lines)):
        count = check_vertical_down(lines, count, line, row)
        count = check_vertical_up(lines, count, line, row)

for line in range(len(lines) - 3):
    for row in range(len(lines) - 3):
        count = check_diagonal_down_right(lines, count, line, row)
        count = check_diagonal_up_right(lines, count, line, row)

for line in range(len(lines) - 3):
    for row in range(len(lines)):
        count = check_diagonal_down_left(lines, count, line, row)
        count = check_diagonal_up_left(lines, count, line, row)


print(count)
