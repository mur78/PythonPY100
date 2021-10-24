def student_month():
    s = float(input("Введите сумму накоплений: "))
    a = float(input("Введите размер стипендии: "))
    b = float(input("Введите расходы на проживание: "))
    sum_n = 0
    month_n = 0

    while sum_n >= 0:
            sum_n += s + a - b * 0.05 - b
            month_n += 1
    return month_n


if __name__ == "__main__":
    # Write your solution here
    print(student_month())
