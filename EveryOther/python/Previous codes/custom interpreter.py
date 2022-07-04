def check (stri):
    strj=""
    stri=stri.split (' ')
    for i in stri:
        if not i=="print":
            strj+=i;
    return strj
    


code=input ("Ener code in single line\nThe code is:\n").split (';')
print ("\n".join (code))
for i in code:
    if '=' in i:
        exec (i)
print ("The output is:")
for i in code: 
    if "print" in i:
        string=""
        string+=check (i)
        exec ("print ("+string+")")
