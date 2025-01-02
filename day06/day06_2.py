from pathlib import Path
from typing import Counter


directions: dict[str, tuple[int, int]] = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def read_file(file_path: Path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


def finds_guards_initial_position(lines: list[str]) -> tuple[int, int]:
    for i, line in enumerate(lines):
        if "^" in line:
            j = line.find("^")
            # breakpoint()
            if j != -1:
                return (i, j)
    return (-1, -1)


def move_guard(
    i, j, a, b, lines, visited_positions: list[list[str]]
) -> tuple[int, int]:
    global positions
    while a + i >= 0 and b + j >= 0 and a + i < len(lines[0]) and b + j < len(lines):
        try:
            if lines[i + a][j + b] != "#":
                i += a
                j += b
                not_visited_before: bool = visit_positions(visited_positions, i, j)
                if not_visited_before:
                    positions += 1
                # print(i, j)
            else:
                return (i, j)
        except IndexError:
            raise IndexError

    return (-1, -1)


def visit_positions(visited_positions: list[list[str]], i: int, j: int) -> bool:
    if visited_positions[i][j] != "X":
        visited_positions[i][j] = "X"
        return True
    return False


def change_guards_direction(
    directions: dict[str, tuple[int, int]], guard
) -> tuple[str, tuple[int, int]]:
    next_returns = False
    for k, v in directions.items():
        if next_returns:
            return (k, v)
        if k == guard:
            next_returns = True

    return ("^", directions["^"])


def print_grid(lines: list) -> None:
    import os

    os.system("clear")
    for line in lines:
        for l in line:
            print(l, end="")
        print()
    # input()


def main():
    pwd = Path(__file__).parent
    file_path_example = pwd / "example_input6.txt"
    file_path_input = pwd / "input6.txt"
    file_path_input_carolinta = pwd / "input_carolinta.txt"
    lines = read_file(file_path_input)
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    visited_positions = [list(x) for x in lines]

    guard = "^"
    global positions
    positions = 0

    # indexes
    i, j = finds_guards_initial_position(lines)

    a, b = directions[lines[i][j]]
    inside_room: bool = True
    height = len(lines[0])
    width = len(lines)

    while inside_room:
        try:
            (i, j) = move_guard(i, j, a, b, lines, visited_positions)
            # print_grid(visited_positions)
            # print(i, j)
            # input()
            if i == -1 and j == -1:
                inside_room = False
        except IndexError:
            inside_room = False
            break

        guard, (a, b) = change_guards_direction(directions, guard)

    # print(positions)

    soma = 0
    for i in visited_positions:
        soma += i.count("X")
    print(soma)


if __name__ == "__main__":
    main()
