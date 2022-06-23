from random import randint

def Time (i):
    global a
    global check
    global num
    while True:
        check+=1
        h,c,d="",randint (0,len (a)-1),randint (0,len (a)-1)
        h+=(str (a [c])+str (a [d]))
        if int (h)<=i or check>84:
            a.remove (a [c])
            if d>c:
                d-=1
            elif d==c:
                break
            a.remove (a [d])
            break
    return h
    
    
a,check,num,c=[],0,0, []
[a.append (int (input("Enter a [{i}]:\n"))) for i in range (9)]
print ("The numbers are:")
print (a)
while check <= 84:
    b=a [:]
    num+=1
    h=Time (12)
    m=Time (60)
    s=Time (60)
    if check>84:
        if num==0:
            raise ValueError ("You entered wrong digits:")
        else:
            break
    if h+m+s not in c:
        print("The time is:"+h+":"+m+":"+s)
    c.append (h+m+s)
    a=b [:]