if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    n = sum(list_) / len(list_)
    print(n)
    list_s = [n - value for i, value in enumerate(list_)]
    print(list_s)


