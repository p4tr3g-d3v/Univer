def one():
    list_a = [0, 0, 10, 10]
    list_b = [0, 5, 20, 10]
    list_c = [0, 0, 0, 0]
    i = 0
    while i < 4:
        list_c[i] = list_a[i]
        list_a[i] = list_b[i]
        list_b[i] = list_c[i]
        print('A =', list_a[i])
        print('B =', list_b[i])
        print("---------")
        i = i + 1


def two():
    list_a = [3, 0, 6, 9]
    list_b = [4, 3, 8, 12]
    list_y = [0, 0, 0, 0]
    list_p = [0, 0, 0, 0]
    i = 0
    while i < 4:
        list_y[i] = ((list_a[i] ** 2) + (list_b[i]) ** 2) ** 0.5
        list_p[i] = list_p[i] + list_a[i] + list_b[i]
        print("P = ", list_p[i])
        i = i + 1


def three():
    int_p = 1
    int_i = 1
    while True:
        int_p = int_p * int_i
        int_i = int_i + 1
        print("P = ", int_p)
        if int_p >= 30:
            break
    return


def main():
    state = int(input("Type need number: "))
    switcher = {
        1: one,
        2: two,
        3: three,
    }
    func = switcher.get(state, lambda: "Invalid number")
    return func()


if __name__:
    main()
