if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_n = [i for i in list_ if i % 2 == 1]
    list_ch = [i for i in list_ if i % 2 == 0]
    print(list_ch)
    print(list_n)
    z_n = len(list_n)
    z_ch = len(list_ch)

    if z_n > z_ch:
        print("Нечетных больше")
    elif z_n < z_ch:
        print("Четных больше")
    elif z_n == z_ch:
        print("Числа равны")


