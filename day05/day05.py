from pathlib import Path


def read_input(file_path: Path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


def validate(updates: list, page_ordering_set: list) -> list:
    for i in range(len(updates) - 1):
        j = i + 1
        while j < len(updates):
            if (updates[j], updates[i]) in page_ordering_set:
                print(updates[j], updates[i])
                return []
            j += 1
    return updates


def main():
    pwd = Path(__file__).parent
    file_path_input = pwd / "input05.txt"
    file_path_example = pwd / "example_input05.txt"

    file = read_input(file_path_input)

    page_ordering_set = []
    updates = []
    for line in file:
        if "|" in line:
            sets = tuple(line.split("|"))
            page_ordering_set.append(sets)

        elif line != "":
            updates.append(line.split(","))

    corrects_list = []
    for up in updates:
        answer = validate(up, page_ordering_set)
        if answer != []:
            corrects_list.append(answer)
    print(corrects_list)

    result = 0
    for c in corrects_list:
        middle_idx = len(c) // 2
        result += int(c[middle_idx])

    print(result)


if __name__ == "__main__":
    main()
