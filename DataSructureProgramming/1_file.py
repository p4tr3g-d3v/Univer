
def rezultat(a, b, c, p):
    result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return result


def polu_per(a, b, c):
    result = (a + b + c) / 2
    return result


def geron():
    int_A = int(input("Введите сторону А = "))
    int_B = int(input("Введите сторону B = "))
    int_C = int(input("Введие сторону C = "))
    int_P = polu_per(int_A, int_B, int_C)
    int_S = rezultat(int_A, int_B, int_C, int_P)
    print(int_S)
    return


def always_uns():
    int_A = int(input("First number: "))
    if int_A > 0:
        int_B = int_A
        print(int_B)
    else:
        int_B = -int_A
        print(int_B)
    return


def kvur():
    int_A = int(input("input А = "))
    i = int(input("input B = "))
    int_B = i
    int_C = int(input("input C = "))
    int_D = int_B ** 2 - 4 * int_A * int_C
    if int_D < 0:
        y = "Нет решения"
        print(y)
    else:
        x1 = (-int_B + int_D ** 0.5) / 2 * int_A
        x2 = (-int_B - int_D ** 0.5) / 2 * int_A
        y = "Есть решение"
        print(y)
        print("X1 = %.2f" % x1)
        print("X2 = %.2f" % x2)
    return


def func_res_one(x):
    result = (2 * x ** 3 + 1) / x - 5
    return result


def func_res_two(x):
    result = 3 * x ** 2 - 2
    return result


def func_res():
    int_x = int(input("Input X: "))
    if int_x < 4:
        res = func_res_one(int_x)
        print(res)
    else:
        res = func_res_two(int_x)
        print(res)
    return


def main():
    while True:
        print("\n\nExit:0\nGeron:1\nAlways unsigned:2\nKVUR:3\nfuncRes:4")
        state = int(input("Type need number: "))
        switcher = {
            0: main,
            1: geron,
            2: always_uns,
            3: kvur,
            4: func_res
        }
        if state == 0:
            break
        func = switcher.get(state, lambda: "Invalid number")
        func()
    return


if __name__:
    main()
