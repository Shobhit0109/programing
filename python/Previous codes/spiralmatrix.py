a=[]
b=1
d=int(input("Enter the size:\n"))
for i in range(d):	
	a.append([])
for i in range(d):
		for j in range(d):
				a[i].append(0)
def spiral(c):
	global a,b
	for i in range(d-c,c):
			a[d-c][i]=b
			b+=1
	for i in range(d-c+1,c):
			a[i][c-1]=b
			b+=1
	for i in range(c-2,d-c-1,-1):
			a[c-1][i]=b
			b+=1
	for i in range(c-2,d-c,-1):
			a[i][d-c]=b
			b+=1
	if b <=d**2:
		return(spiral(c-1))
spiral(d)
for i in enumerate(a):
	  print(i)
		
,