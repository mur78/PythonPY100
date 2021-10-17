# Напишите ваше решение
# Напишите ваше решение
speed = float(input('Задайте скорость передачи данных: '))
time = float(input('Время скачивания: '))
coast = float(input('Цена за 1 ГБ: '))
size = (time * speed) # Б за время
size_gb = size // (1024 * 1024)
coast_gb = (size_gb * coast)
print(size_gb)
print(coast_gb)
