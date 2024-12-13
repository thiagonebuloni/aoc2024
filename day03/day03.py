import re

INPUT: str = "day03/input03.txt"
EXAMPLE: str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# COMPARE_INPUT: str = "day03/input_test.txt"
# first try = 31103311

result = 0
for line in open(COMPARE_INPUT, "r"):
    res = re.findall("mul\([0-99]+,[0-99]+\)", line)
    for i in res:
        r = re.findall("[0-99]+,[0-99]+", i)
        num1, num2 = r[0].split(",")
        result += int(num1) * int(num2)

print(result)
