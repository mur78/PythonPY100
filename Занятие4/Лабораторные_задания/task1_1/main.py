def sum_n_m():
    n = int(input("Введите число n: "))
    m = int(input("Введите число m: "))

    z = [i ** 2 for i in range(n,m+1) if i >= 0]
    return z

if __name__ == "__main__":
    # Write your solution here
    print(sum_n_m())
