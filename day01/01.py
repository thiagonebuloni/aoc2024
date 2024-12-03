INPUT: str = "day01/input.txt"
EXAMPLE_INPUT: str = "day01/example_input.txt"


def solve(array1: str, array2: str):
    distances: list = []

    array_sorted1 = sorted(list(array1))
    array_sorted2 = sorted(list(array2))
    print(array_sorted1)
    print(array_sorted2)

    for num1, num2 in zip(array_sorted1, array_sorted2):
        distances.append(abs(int(num1) - int(num2)))
        print(abs(int(num1) - int(num2)))

    print()
    print(sum(distances))
    # input()
    return sum(distances)


distances: list = []
array1: list = []
array2: list = []
with open(INPUT, "r") as file:
    for line in file:
        a1, a2 = line.split()
        array1.append(int(a1))
        array2.append(int(a2))

    array1.sort()
    array2.sort()

    for a1, a2 in zip(array1, array2):
        distances.append(abs(a1 - a2))

    print(sum(distances))
