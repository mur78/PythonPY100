def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * (factorial(n-1))

if __name__ == "__main__":
    # Write your solution here
    z = float(input("Введите значение n: "))
    print(factorial(z))
