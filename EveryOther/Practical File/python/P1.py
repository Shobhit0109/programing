string = input("\n\tEnter String:")

Lc , Uc , D , ss = 0 , 0 , 0 , 0

for i in string:

    if i.islower():
        Lc += 1

    elif i.isupper():
        Uc += 1
    
    elif i.isdigit():
        D += 1

    else:
        ss += 1

print(f"""\n string is: {string}
\tLower case letters are: {Lc}
\tUpper case letters are: {Uc}
\tDigits are: {D}
\tSpeical characters are: {ss}""")


