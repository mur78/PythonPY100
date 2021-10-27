def list_avg():
    n = int(input("Введите число n: "))
    list_s = list(range(n))
    # list_n = []
    # for i, value in enumerate(list_s):
    z = sum(list_s) / len(list_s)
    print(z)
    list_n = [i for i in list_s if i >= z]
    return list_n



if __name__ == "__main__":
    # Write your solution here
    print(list_avg())

