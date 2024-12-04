INPUT: str = "day02/input02.txt"
EXAMPLE_INPUT: str = "day02/example_input02.txt"

safe: int = 0

with open(INPUT, "r") as file:
    for line in file:
        line_int = list(map(lambda x: int(x), line.split()))

        print(line_int)

        if line_int[0] < line_int[1]:
            consistency = False
            for i in range(len(line_int) - 1):
                if (
                    line_int[i] < line_int[i + 1]
                    and abs(line_int[i] - line_int[i + 1]) <= 3
                ):
                    consistency = True
                else:
                    consistency = False
                    break
            if consistency:
                safe += 1
        elif line_int[0] > line_int[1]:
            for i in range(len(line_int) - 1):
                if (
                    line_int[i] > line_int[i + 1]
                    and abs(line_int[i] - line_int[i + 1]) <= 3
                ):
                    consistency = True
                else:
                    consistency = False
                    break
            if consistency:
                safe += 1
print(safe)
