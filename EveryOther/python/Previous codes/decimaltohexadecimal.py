#decimal to hex
conv = [ '1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
num,p = int(input()),0
b = []
while num - int(num) != 0:
	num *= 16
	p += 1
	
while num != 0:
	b.append(conv[num % 16+1])
	num //= 16

if p != 0:
	b[-1-p:-1-p] = '.'
b = ''.join(b[:-1])

print(b)

#hex to decimal
conv = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
p = len(b.split()[0])
num = 0
for i in b:
	if i=='.':
		continue
	num += conv[i]*16**p
	p -= 1
