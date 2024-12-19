from pathlib import Path

pwd = Path(__file__).parent

INPUT: Path = pwd / "input04.txt"
EXAMPLE: Path = pwd / "example_input04.txt"

file = EXAMPLE.open("r")
lines = file.readlines()
count = 0
directions = {}

# horizontal
word = "XMAS"
for line in lines:
    step = 0
    for row in line:
        if row == word[step]:
            if step == 3:
                step = 0
                count += 1
                print(f" horizontal: {count}")
                break
            step += 1

            # input()
    print()
directions["horizontal"] = count

# horizontal backwards
word = "SAMX"
for line in lines:
    step = 0
    for row in line:
        if row == word[step]:
            if step == 3:
                step = 0
                count += 1
                print(f" hor backwards: {count}")
                break
            step += 1

            # input()
    print()
directions["horizontal back"] = count - directions["horizontal"]
print(directions)

# vertical
print("VERTICAL")
word = "XMAS"
len_l = len(lines)
for i in range(len_l):
    step = 0
    for j in range(len_l):
        if lines[j][i] == word[step]:
            print(lines[j][i], end="")
            if step == 3:
                step = 0
                count += 1
                print(f" vertical: {count}")
                break
            step += 1
    print()
directions["vertical"] = (
    count - directions["horizontal back"] - directions["horizontal"]
)
print(directions)

# vertical backwards
print("VER BACKWARDS")
word = "SAMX"
len_l = len(lines)
for i in range(len_l):
    step = 0
    for j in range(len_l):
        if lines[j][i] == word[step]:
            print(lines[j][i], end="")
            if step == 3:
                step = 0
                count += 1
                print(f" vertical: {count}")
                break
            step += 1
    print()
directions["vertical back"] = (
    count
    - directions["horizontal back"]
    - directions["horizontal"]
    - directions["vertical"]
)
print(directions)

# diagonal P D
print("DIAGONAL P D")
word = "XMAS"
len_l = len(lines)
i = 0
j = 0
while i < len_l:
    step = 0
    while j < len_l:
        if lines[i][j + 1] == word[step]:
            print(lines[i][j + 1], i, j + 1, end=" ")
            i += 1
            if step == 3:
                step = 0
                count += 1
                print(f" vertical: {count}")
                break
            step += 1

        j += 1

    i += 1

    print("---", end="")
    print()
print("len_l")
print(lines[0][4], lines[1][5])

directions["diagonal p d"] = (
    count
    - directions["horizontal back"]
    - directions["horizontal"]
    - directions["vertical"]
    - directions["vertical back"]
)
print(directions)


# diagonal P D back
print("DIAGONAL P D BACK ")
word = "SAMX"
len_l = len(lines)
for a in range(len_l):
    i = 0
    j = 0
    while i < len_l:
        step = 0
        while j < len_l:
            if lines[i][j + 1] == word[step]:
                print(lines[i][j + 1], i, j + 1, end=" ")
                i += 1
                if step == 3:
                    step = 0
                    count += 1
                    print(f" vertical: {count}")
                    break
                step += 1

            j += 1

        j = 0
        i += 1

    print("---", end="")
    print()
print("len_l")
print(lines[0][4], lines[1][5])

directions["diagonal p d back"] = (
    count
    - directions["diagonal p d"]
    - directions["horizontal back"]
    - directions["horizontal"]
    - directions["vertical"]
    - directions["vertical back"]
)
print(directions)


# # diagonal P E
# print("DIAGONAL P E")
# word = "XMAS"
# len_l = len(lines)
# i = 0
# j = len_l - 1
# while i < len_l:
#     step = 0
#     while j > 0:
#         if lines[i][j + 1] == word[step]:
#             print(lines[i][j - 1], i, j - 1, end=" ")
#             j -= 1
#             if step == 3:
#                 step = 0
#                 count += 1
#                 print(f" vertical: {count}")
#                 break
#             step += 1

#         j -= 1

#     i += 1

#     print("---", end="")
#     print()
# print("len_l")
# print(lines[3][9], lines[4][8])

# directions["diagonal p e"] = (
#     count
#     - directions["horizontal back"]
#     - directions["horizontal"]
#     - directions["vertical"]
#     - directions["vertical back"]
#     - directions["diagonal p d"]
#     - directions["diagonal p d back"]
# )
# print(directions)
# print(count)


# # diagonal P E BACK
# print("DIAGONAL P E BACK")
# word = "SAMX"
# len_l = len(lines)
# i = 0
# j = len_l - 1
# while i < len_l:
#     step = 0
#     while j > 0:
#         if lines[i][j + 1] == word[step]:
#             print(lines[i][j - 1], i, j - 1, end=" ")
#             j -= 1
#             if step == 3:
#                 step = 0
#                 count += 1
#                 print(f" vertical: {count}")
#                 break
#             step += 1

#         j -= 1

#     i += 1

#     print("---", end="")
#     print()
# print("len_l")
# print(lines[3][9], lines[4][8])

# directions["diagonal p e back"] = (
#     count
#     - directions["diagonal p e"]
#     - directions["horizontal back"]
#     - directions["horizontal"]
#     - directions["vertical"]
#     - directions["vertical back"]
#     - directions["diagonal p d back"]
#     - directions["diagonal p d"]
# )
# print(directions)
print(count)
