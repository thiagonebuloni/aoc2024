INPUT: str = "day03/input03.txt"
EXAMPLE: str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# first try = 31103311

for line in open(INPUT, "r"):
    inp = line

    # input = EXAMPLE

    index: int = 0
    result: int = 0
    for i in range(len(inp)):
        ind = inp.find("mul(347,382)")
        if ind != -1:
            print(ind, inp[ind : ind + 10])
            input()
        index = inp.find(
            "mul(",
            index,
        )
        if index == -1:
            break
        end_index = inp.find(")", index, index + 13)
        if end_index == -1:
            index = index + 13
            continue
        print(inp[index : end_index + 1])
        try:
            _, pre = inp[index : end_index + 1].split("(")
            a, b = pre.split(",")
        except ValueError:
            continue
        b = b.replace(")", "")
        mul = int(a) * int(b)
        print(f"{a} * {b} = {mul}")
        print(result + mul)

        result += mul
        index = end_index
    print(result)
