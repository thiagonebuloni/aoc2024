INPUT: str = "day02/input02.txt"
EXAMPLE_INPUT: str = "day02/example_input02.txt"
EXAMPLE_INPUT2: str = "day02/example_input_02-2.txt"


def is_ok(lista: list) -> bool:
    k = len(lista)
    ok: bool = True
    only_inc: bool = True
    only_dec: bool = True
    for j in range(k - 1):
        diff: int = lista[j + 1] - lista[j]
        if diff > 0:
            only_dec = False
        if diff < 0:
            only_inc = False
        if not (1 <= abs(diff) and abs(diff) <= 3):
            ok = False
            break
    return ok and (only_inc or only_dec)


def consider(i: int, a: list, any_ok: bool) -> bool:
    b = a[:]
    b.pop(i)
    if is_ok(b):
        any_ok = True
    return any_ok


def main():
    safe: int = 0
    for line_str in open(INPUT, "r"):
        report = list(map(lambda x: int(x), line_str.split()))

        k: int = len(report)
        any_ok: bool = False
        any_ok = consider(0, report, any_ok)
        for i in range(k - 1):
            diff: int = report[i + 1] - report[i]
            if abs(diff) < 1 or abs(diff) > 3:
                any_ok = consider(i, report, any_ok)
                any_ok = consider(i + 1, report, any_ok)
                break
            if i + 2 < k:
                diff2: int = report[i + 2] - report[i + 1]
                if (diff > 0) != (diff2 > 0):
                    any_ok = consider(i, report, any_ok)
                    any_ok = consider(i + 1, report, any_ok)
                    any_ok = consider(i + 2, report, any_ok)
        if any_ok:
            safe += 1
        print(report)
        print(any_ok)
    print(safe)


if __name__ == "__main__":
    main()


# safe += test([51, 47, 50, 48, 47, 45, 44, 47])
# safe += test([53, 54, 51, 52, 47, 45, 44, 43])
# safe += test([13, 9, 7, 6, 2, 1])

# safe += test([8, 6, 4, 4, 1])
# safe += test([8, 4, 4, 4, 1])
# safe += test([8, 6, 6, 4, 4])
# safe += test([1, 3, 2, 4, 5])
# safe += test([1, 3, 6, 7, 9])
# safe += test([17, 18, 19, 21, 22, 23, 27])
