from helpers.file_reaper import file_reaper
from collections import Counter

INPUT: str = "day01/input01.txt"
EXAMPLE_INPUT: str = "day01/example_input01.txt"

array1: list = []
array2: list = []

for line in file_reaper(INPUT):
    a1, a2 = line.split()
    array1.append(int(a1))
    array2.append(int(a2))

cou = Counter(array2)

lista_results = []

for i in array1:
    lista_results.append(cou[i] * i)

print(sum(lista_results))
