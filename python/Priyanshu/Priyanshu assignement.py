DATA = []

file = open("/home/shobhit/Documents/programing/python/Priyanshu/demofile.txt","r")

for exp in file:

    i = []
    for j in exp:
        if 'a' <= j <= 'z' or 'A' <= j <= 'Z' or '0' <= j <= '9' or j in '-+*%/=' :
            i.append(j)

    for j in i:
         if j in "123456789" and int(j) not in DATA:
            DATA.append(int(j))

    for j in range(2,len(i)):
        if i[j] not in "123456789-*+%/":
            for k in DATA:
                if type(k) == list and k[0] == i[j]:
                    i[j] = str(DATA[k[1]])
                    break
            else:
                print(i[j],j)
                raise ValueError
 
    c = eval(''.join(i[2:]))

    if c not in DATA:
        DATA.append(c)
        pos = len(DATA) - 1
    else:
        pos = DATA.index(c)

    for j in DATA:
        if type(j) == list:
            if j[0] == i[0]:
                j[1] = pos
                break
    else:
        DATA.append([i[0],pos])

file.close()
print(DATA)
print("\nVariable Values:")
for i in DATA:
    if type(i) == list:
        print('\t' + i[0] + f" = {DATA[i[1]]}")
    
print(end="\nGarbage Integers: ")
for i in DATA:
    if type(i) == list:
        DATA.remove(DATA[i[1]])
        DATA.remove(i)

print(*DATA,'\n')