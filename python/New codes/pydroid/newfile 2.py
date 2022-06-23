def add(num):
	if num == 1: 
		return 1
	else:
		n -= 1
		return num + add(n-1)

n = 100
print(add(n))