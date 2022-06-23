#decimal to hex
num,p = int(input()),0
b = []
while num - int(num) != 0:
	num *= 8
	p += 1
	
while num != 0:
	b.append(conv[num % 8+1])
	num //= 8

if p != 0:
	b[-1-p:-1-p] = '.'
b = ''.join(b[:-1])

print(b)
#octal to decimal 

p = len(b.split()[0])
num = 0
for i in b:
	if i=='.':
		continue
	num += int(i)*8**p
	p -= 1
print(num)
