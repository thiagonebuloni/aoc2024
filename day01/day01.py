from helpers.file_reaper import file_reaper

INPUT: str = "day01/input01.txt"
EXAMPLE_INPUT: str = "day01/example_input01.txt"

distances: list = []
array1: list = []
array2: list = []


for line in file_reaper(INPUT):
    a1, a2 = line.split()
    array1.append(int(a1))
    array2.append(int(a2))

array1.sort()
array2.sort()

for a1, a2 in zip(array1, array2):
    distances.append(abs(a1 - a2))

print(sum(distances))
