def poliand():
    n = int(input("Введите число: "))
    s = str(n)
    reverse_s = ''.join(s[::-1])
    if s == reverse_s:
        print("Палиндром")
    else:
        print("Нет")

if __name__ == "__main__":
    # Write your solution here
    poliand()

