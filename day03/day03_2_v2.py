import re

INPUT: str = "day03/input03.txt"
EXAMPLE: str = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)
# first try = 31103311

result = 0
new_line = ""
rights = []
for line in open(INPUT, "r"):
    line = EXAMPLE
    first_dont = line.find("don't()")
    rights.append(line[:first_dont])
    dos = line[first_dont:].split("do()")
    for i in range(len(dos)):
        if i % 2 != 0:
            rights.append(dos[i].split("don't()")[0])

print("+++++++++++++++++++++++")
print(rights)
print("+++++++++++++++++++++++")

res = []

for i in rights:
    res.extend(re.findall("mul\([0-99]+,[0-99]+\)", i))
for i in res:
    r = re.findall("[0-99]+,[0-99]+", i)
    num1, num2 = r[0].split(",")
    result += int(num1) * int(num2)

print(result)
