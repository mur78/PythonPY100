if __name__ == "__main__":
    surname_list = [  # список фамилий Санкт-Петербурга
        "Иванов",
        "Васильев",
        "Петров",
        "Смирнов",
        "Михайлов",
        "Фёдоров",
        "Соколов",
        "Яковлев",
        "Попов",
        "Андреев",
        "Алексеев",
        "Александров",
        "Лебедев",
        "Григорьев",
        "Степанов",
        "Семёнов",
        "Павлов",
        "Богданов",
        "Николаев",
        "Дмитриев",
        "Егоров",
        "Волков",
        "Кузнецов",
        "Никитин",
        "Соловьёв"
    ]
    # TODO распечатать фамилии и их номера

    for number, family in enumerate(surname_list, 1):
        print(number, family)