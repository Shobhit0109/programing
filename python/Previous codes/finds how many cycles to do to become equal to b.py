#from time import time
test = int(input())
cycle = -1
Cyc = []
num = 2

def make(a):
    large = 0
    for i in range(len(a)):
        value = 0
        for i in range(len(a)):
            value += int(a[i]) * (2**(n-i-1))
        if large < value:
                large = value
        a = a[1:]+a[0]
    return large

if 1 <= test <= 1000:
    for t in range(test):
        n,k = [int(i) for i in input().split()]
        if not 1 <= n <= 10**5 and 1 <= k<= 10**9:
            continue
        a = input()
        for i in a:
            if int(i) not in [0,1]:
                continue
        b = make(a)
        
        while num > 0:
            cycle += 1
            value = 0
            for i in range(len(a)):
                value += int(a[i]) * (2**(n-i-1))
            if value == b:
                num -= 1
                Cyc.append(cycle)

            a = a[1:] + a[0]
        print(Cyc[0]+(Cyc[1]-Cyc[0])*(k-1))