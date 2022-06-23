string = input("\n\tEnter Required String : ")

if len(string) == 0:
    print("\n\tInput string must contain at least 1 character")
    exit(0)

def Rev(string):
    if len(string) == 1:
        return string
    else:
        return Rev(string[1:]) + string[0]


print("\t" + Rev(string))


