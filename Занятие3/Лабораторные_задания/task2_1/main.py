def task(str1, str2, k):
    if str1[:k] == str2[:k]:  # TODO проверка совпадения строк
        print('Да')
    else:
        print("Нет")


if __name__ == "__main__":
    print(task('123', '12345', 2))
