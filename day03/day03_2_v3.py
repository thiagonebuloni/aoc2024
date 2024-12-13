import re

INPUT: str = "day03/input03.txt"
EXAMPLE: str = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def is_a_digit(cut: str) -> int:
    if "," in cut:
        a, b, *_ = cut.split(",")
        b = b.split(")")[0]
        if a.isdigit() and b.isdigit():
            return int(a) * int(b)

    return 0


result = 0

with open(INPUT, "r") as file:
    line = file.readline()

for i in range(len(line)):
    enable = True
    if "don't()" in line[i : i + 8]:
        enable = False
    if "do()" in line[i : i + 5]:
        enable = True
    if enable and line[i] == "m":
        if line[i + 1] == "u" and line[i + 2] == "l" and line[i + 3] == "(":
            # x = line[i + 4 : i + 11].find(")")
            # if x == -1
            possible = line[i + 4 : i + 11]
            result += is_a_digit(possible)


res = []

# for i in rights:
#     res.extend(re.findall("mul\([0-99]+,[0-99]+\)", i))
# for i in res:
#     r = re.findall("[0-99]+,[0-99]+", i)
#     num1, num2 = r[0].split(",")
#     result += int(num1) * int(num2)


print(result)
