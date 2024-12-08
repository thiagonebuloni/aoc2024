def direction_decision(report: list) -> int:
    direction_stack: int = 0

    for i in range(len(report) - 1):
        if report[i] - report[i + 1] < 0:
            direction_stack += 1
        elif report[i] - report[i + 1] > 0:
            direction_stack -= 1

    print("\n", report)
    if direction_stack > 0:
        print("Incremental ", end="")
    else:
        print("Decremental ", end="")
    return direction_stack


def increasing(report: list) -> bool:
    r_copy = report[:]
    again = 0
    for num in range(3):
        for i in range(len(r_copy) - 1):
            if abs(r_copy[i] - r_copy[i + 1]) > 3 or r_copy[i] - r_copy[i + 1] >= 0:
                if again == 0:
                    r_copy.remove(r_copy[i])
                    again += 1
                    break
                elif again == 1:
                    r_copy = report[:]
                    r_copy.remove(r_copy[i + 2])
                    again += 1
                    break
                else:
                    return False

    return True


def decreasing(report: list) -> bool:
    r_copy = report[:]
    again = 0
    for num in range(3):
        for i in range(len(r_copy) - 1):
            if abs(r_copy[i] - r_copy[i + 1]) > 3 or r_copy[i] - r_copy[i + 1] <= 0:
                if again == 0:
                    r_copy.remove(r_copy[i])
                    again += 1
                    break
                elif again == 1:
                    r_copy = report[:]
                    r_copy.remove(r_copy[i + 2])
                    again += 1
                    break
                else:
                    return False

    return True


def test(report) -> int:
    direction = direction_decision(report)

    # testar diferença absoluta entre len(report) e direction
    # diferença de 1 == nenhuma alternância
    # diferença de 3 == 1 alternância
    # diferença de 2 == 1 número repetido
    # diferença de 5 == 2 alternância

    difference = abs(len(report) - direction)

    if difference > 3:
        print(False)
        return 0

    if direction > 0:
        result = increasing(report)
        print(result)
    else:
        result = decreasing(report)
        print(result)

    if result:
        return 1

    return 0


def main():
    INPUT: str = "day02/input02.txt"
    EXAMPLE_INPUT: str = "day02/example_input02.txt"
    EXAMPLE_INPUT2: str = "day02/example_input_02-2.txt"

    safe = 0

    for line_str in open(INPUT, "r"):
        report = list(map(lambda x: int(x), line_str.split()))

        safe += test(report)

    # safe += test([51, 47, 50, 48, 47, 45, 44, 47])
    # safe += test([53, 54, 51, 52, 47, 45, 44, 43])
    # safe += test([13, 9, 7, 6, 2, 1])

    # safe += test([8, 6, 4, 4, 1])
    # safe += test([8, 4, 4, 4, 1])
    # safe += test([8, 6, 6, 4, 4])
    # safe += test([1, 3, 2, 4, 5])
    # safe += test([1, 3, 6, 7, 9])
    # safe += test([17, 18, 19, 21, 22, 23, 27])

    print(safe)

    # se (i < i + 1) pilha -1
    # se (i > i + 1) pilha +1


if __name__ == "__main__":
    main()
