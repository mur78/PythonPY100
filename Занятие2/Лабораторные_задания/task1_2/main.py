# TODO

A = int(input("Введите чило А: "))
B = int(input("Введите чило B: "))

result = A % 2 == 1 and B % 2 == 1
if result:
    print("Числа A и B нечетные")
