num,factors = [int(i) for i in input().split()],[]
res,f = 1,2

def check(num ,f):
    for i in num:
        if i%f == 0:
            return 1
    return 0
def allone(num):
    for i in num:
        if i != 1:
            return 0
    return 1

while True:
    while check(num,f):
        num = [i//f if i%f == 0 else i for i in num]
        factors.append(f)
    f += 1
    if  allone(num):
        break
            
for i in factors:
    res *= i

print(f"The LCM is : {res}")

