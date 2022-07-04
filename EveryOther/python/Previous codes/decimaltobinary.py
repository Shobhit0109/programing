#dec to oct
num,p = int(input()),0
b = []
while num - int(num) != 0:
	num *= 2
	p += 1
	
while num != 0:
	b.append(str(num % 2+1))
	num //= 2

if p != 0:
	b[-1-p:-1-p] = '.'
b = ''.join(b[:-1])

print(b)

#oct to dec

p = len(b.split()[0])
num = 0
for i in b:
	if i=='.':
		continue
	num += int(i)*2**p
	p -= 1
print(num)
