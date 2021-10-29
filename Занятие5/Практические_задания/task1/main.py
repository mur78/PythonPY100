if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print()


table = [
    [i*j for j in range(1,10)]
    for i in range(1,10)
    ]

for row in range(len(table)):
    for col in range(len(table[row])):
        ceil = table[row][col]
        #print(table[row][col], end=" ")
        print(f"{ceil:>2}", end=" ")
    print()

