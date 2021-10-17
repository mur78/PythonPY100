# TODO
A = int(input('Введите число А: '))
B = int(input('Введите число B: '))
C = int(input('Введите число C: '))

result_1 = A <= 45 and B > 45 and C > 45
result_2 = A > 45 and B <= 45 and C > 45
result_3 = A > 45 and B > 45 and C <= 45

if result_1 or result_2 or result_3:
    print("Только 1 число меньше 45 - Истина")
else:
    print("Все числа больше 45 - Ложь")