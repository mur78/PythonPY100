if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_n = [i for i, value in enumerate(list_) if list_[i] > list_[0]]
    print(len(list_n),list_n)
