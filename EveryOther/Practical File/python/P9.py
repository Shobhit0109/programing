lines = []

print("\n\tEnter lines: \n")

while True :
    string = input("\t")

    if string == '':
        break

    lines.append(string)

print("\n\tThe lines you entered are:\n")
for i in lines:
    print('\t' + i)

print()


