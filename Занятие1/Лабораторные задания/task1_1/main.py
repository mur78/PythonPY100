DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("Введите год рождения: ")) # TODO запросить у пользователя год рождения
current_year = int(input("Введите текущий год: "))# TODO запросить у пользователя текущий год

days = ((current_year - start_year) * DAYS_OF_YEAR)

print(days)


# TODO посчитать и распечатать количество прожитых дней
