from collections import Counter

INPUT: str = "day01/input.txt"
EXAMPLE_INPUT: str = "day01/example_input.txt"

array1: list = []
array2: list = []

with open(INPUT, "r") as file:
    for line in file:
        a1, a2 = line.split()
        array1.append(int(a1))
        array2.append(int(a2))

    cou = Counter(array2)

    lista_results = []

    for i in array1:
        lista_results.append(cou[i] * i)

print(sum(lista_results))
