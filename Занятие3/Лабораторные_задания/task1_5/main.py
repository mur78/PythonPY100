def cont_val():
    n = int(input("Введите первое число: "))
    sum_n = n
    while True:
        if n != 0:
            n = int(input("Введите следующее число: "))
            sum_n += n
        else:
            break
            total = sum_n
    return sum_n



if __name__ == "__main__":
    # Write your solution here
    print(cont_val())
