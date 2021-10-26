def mult_value():
    n = int(input("Введите число: "))
    d = 2
    f_ = []

    #m = n
    while d * d <= n:
        if n % d == 0:
            f_.append(d)
            n //= d
        else:
            d += 1
    f_.append(n)  # Добавим последнеё простое число
    return f_

if __name__ == "__main__":
    # Write your solution here
    print(mult_value())  # Выводим исходное число и все простые множители.
