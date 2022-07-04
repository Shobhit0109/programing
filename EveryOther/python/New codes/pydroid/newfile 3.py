def calc(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[len(s)-i-1]) * 2 ** i
    return sum

num = int(input())

s = ""

while num != 0:
    s += str(num % 2)
    num //= 2
    
s += "0"
s= s[::-1]

xor = []

for i in range(len(s)):
    for j in range(i,len(s)):
        xor.append(calc(s[i:j]))
        
ans = xor[0]

for i in xor[1:]:
    ans ^= i

print(ans)