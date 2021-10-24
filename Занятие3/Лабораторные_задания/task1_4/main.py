def func_epc(n):
    sum_n = 0.0
    current_v = 1.0
    epsilon = 0.0001
    while True:
        if current_v > epsilon:
            current_v = 1 / (2 ** n)
            sum_n += current_v
        else:
            break
    return sum_n

if __name__ == "__main__":
    # Write your solution here
    v = float(input("Введите число n: "))
    print(func_epc(v))
