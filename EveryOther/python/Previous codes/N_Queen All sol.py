from os import system

while (True):
    system('clear')
    #input
    try:
        print("\tPls enter size", end=':')
        size = int(input())
    except:
        print("\tAs you don't enter any input so default input will be 4")
        size = 4

    #process
    test, result = [0 for i in range(size)], []

    for t in range(size**size):
        #check test
        check = 1
        for j in range(size):
            for i in range(1, j + 1):
                if test[j - i] == test[j] or test[
                        j - i] == test[j] - i or test[j - i] == test[j] + i:
                    #  For in row                For Upper diagonal				For lower diagonal
                    check = 0
                    break
            if check == 0:
                break
        if check == 1:
            result.append(test[:])

        #Make test
        j = size - 1
        test[j] += 1
        while j > -1:
            if test[j] > size - 1:
                test[j] = 0
                test[j - 1] += 1
            j -= 1

    #Printing
    print(f"\tTotal matrix found = {len(result)}")
    print("\tAll Solutions are:")
    for t in result:
        print(end="\n\n\t")
        for i in range(size):
            for j in range(size):
                if i == t[j]:
                    print('|👸|', end='')
                else:
                    print('|__|', end='')
            print(end="\n\t")
        print({t[j]: j for j in range(size)}, end="\n\t")
    print(
        "\n\n\tthank you and try again with different size to see different results"
    )

    #repeate
    print(
        "\n\tIf you want to try again hit ang character : (for quiet hit only enter)"
    )
    char = input()
    if char == '':
        break

print("\n\t Welcome back Again ")
