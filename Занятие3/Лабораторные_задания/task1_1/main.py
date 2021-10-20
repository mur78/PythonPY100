def t_1_1():
    max_sum = 500
    current_sum = 0
    n = 1

    while True:
        # как то увеличиваем шаг
        current_value = n ** 2
        #current_sum += n ** 2
        #print(n, current_sum)

        if current_sum > max_sum:
            break
        else:
            current_sum += n ** 2
            print(n, current_sum)
            n += 1

    return n



if __name__ == "__main__":
    # Write your solution her
    print(t_1_1())

