def sum_student():
    a = float(input("Введите стипендию: ")) #стипендия
    b = float(input("Введите расходы: ")) #расходы
    sum_ = 0
    for i in range(1,11):
        sum_ += b * 0.03 + b - a
        total = sum_/10 + a
    return total

if __name__ == "__main__":
    # Write your solution here
    print(sum_student())

