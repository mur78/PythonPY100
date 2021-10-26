if __name__ == "__main__":
    list_s = list(range(1,11,))
    first_index = 0
    first_value = list_s[0]
    max_index = 0
    max_value = list_s[max_index]

    for i, current_value in enumerate(list_s):
        if current_value >= max_value:
            max_value = current_value
            max_index = i

list_s[max_index], list_s[first_index] = list_s[first_index], list_s[max_index]
print(list_s)





