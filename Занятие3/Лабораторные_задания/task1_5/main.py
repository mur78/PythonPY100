def cont_val():
    list_= []
    n = int(input("Введите первое число: "))

    #sum_n = n
    #while True:
        #if n != 0:
            #n = int(input("Введите следующее число: "))
            #sum_n += n
            #list_.append(n)

        #else:
            #break
    #print(list_)
    #return sum_n


def cont_val():
    list_ = []
    sum_n = 0
    while True:
        n = int(input("Введите следующее число: "))
        if n == 0:
            break

        sum_n += n
        list_.append(n)

    print(list_)
    return sum_n


if __name__ == "__main__":
    # Write your solution here
    print(cont_val())

