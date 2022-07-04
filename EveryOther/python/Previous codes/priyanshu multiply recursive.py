def mul(a,b):
    if b== 0:
        return 0
    elif b % 2 == 0:
        return mul(2*a,b // 2)
    else :
        return a + mul(2*a,b//2)
        
print(mul(*[int(i) for i in input().split())
