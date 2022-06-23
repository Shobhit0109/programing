num = input()

#First Method for python
print(num[::-1])

#Second Method for c
num,a = int(num),0
while num > 0:
    a = a*10 + num%10
    num = num//10
    
print(a)