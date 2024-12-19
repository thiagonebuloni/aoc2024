from pathlib import Path

pwd = Path(__file__).parent

INPUT: Path = pwd / "input04.txt"
EXAMPLE: Path = pwd / "example_input04.txt"


file = INPUT.open("r")
lines = file.readlines()
count = 0
directions = {}


def check(lines, line, row) -> bool:
    partial = False
    possibilities = ["SAM", "MAS"]
    try:
        word1 = lines[line - 1][row - 1] + lines[line][row] + lines[line + 1][row + 1]
        word2 = lines[line - 1][row + 1] + lines[line][row] + lines[line + 1][row - 1]

        if word1 in possibilities and word2 in possibilities:
            partial = True
        else:
            partial = False

    except IndexError:
        return partial

    return partial


def na_tela(lines, line, row):
    print()
    print(lines[line - 1][row - 1], " ", lines[line - 1][row + 1], "  ")
    print(" ", lines[line][row], "  ")
    print(lines[line + 1][row - 1], " ", lines[line + 1][row + 1])


for line in range(1, len(lines) - 1):
    for row in range(1, len(lines) - 1):
        if lines[line][row] == "A":
            partial = check(lines, line, row)
            if partial:
                na_tela(lines, line, row)
                count += 1


print(count)
