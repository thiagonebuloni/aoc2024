import re

INPUT: str = "day03/input03.txt"
EXAMPLE: str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# first try = 31103311

result = 0
new_line = ""
donts = []
dos = []
for line in open(INPUT, "r"):
    dont = re.search(r"don't\(\)", line)
    pause = dont.span()[1] - 7
    play = 0
    new_line += line[:pause]
    while len(line[play:pause]):
        do = re.search(r"do\(\)", line[pause:])
        play = do.span()[1]

        dont = re.search(r"don't\(\)", line[play:])
        pause = dont.span()[1] - 7
        new_line += line[play:pause]


print(new_line)

res = re.findall(r"mul\([0-99]+,[0-99]+\)", new_line)
# print(res)
# re.finditer(r"mul\([0-99]+,[0-99]+\)", new_line)

for i in res:
    r = re.findall("[0-99]+,[0-99]+", i)
    num1, num2 = r[0].split(",")
    result += int(num1) * int(num2)


print(result)
