try:
	ai = [int(i) for i in input().split()]
	k = int(input())
except:
	ai = [1,2,3,4,5,6,7,8,9,0]
	k = 6
	
comb = ai[:]
	
def sum(a):
	sum = 0
	for i in a:
		sum += i
	return sum
	
def Remove(a):
	a = a[::-1]
	a.remove(a[0])
	a = a[::-1]
	return a


print("Subsets are:")
while True:
	if comb == []:
		print("No subset available")
		break
	if k == sum(comb):
		print(*comb,sep = '+')
		break
	else:
		comb = Remove(comb)
		index = len(comb)
		for i in range(index,len(ai)):
			comb.append(ai[i])
			if k == sum(comb):
				print(*comb,sep = '+')
				break
			comb = Remove(comb)