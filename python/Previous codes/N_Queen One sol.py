from os import system

while (True):
    system('clear')

    def check(test, size, j):
        for i in range(1, j + 1):
            if test[j - i] == test[j] or test[j - i] == test[j] - i or test[
                    j - i] == test[j] + i:
                #  For in row                For Upper diagonal				For lower diagonal
                return 0
        return 1

    #input
    try:
        print("\tPls enter size", end=':')
        size = int(input())
    except:
        print("\tAs you don't enter any input so default input will be 4")
        size = 4

    #process
    matrix = [0 for i in range(size)]
    i, j = 0, 0

    #Make incomplete
    while size > j > -1:
        while matrix[j] < size:
            if check(matrix, size, j) == 1:
                j += 1
                break
            matrix[j] += 1
        else:
            matrix[j] = 0
            j -= 1
            matrix[j] += 1

    #Printing
    if j == size:
        print("\tOne Solution is:")
        for i in range(size):
            print(end="\n\t")
            for j in range(size):
                if i == matrix[j]:
                    print(end="|👸|")
                else:
                    print(end="|__|")
    else:
        print("\n\tNo solutions")

    print(end="\n\t")
    for i in range(size):
        print(f"({matrix[i]}:{i})", end=',')

    #End
    print(
        "\n\n\tthank you and try again with different size to see different results"
    )

    #repeate
    print(
        "\n\tIf you want to try again hit any character : (for quiet hit only enter)"
    )
    char = input()
    if char == '':
        print("\n\t Welcome back Again ")
        break
