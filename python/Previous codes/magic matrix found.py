from time import process_time as p
a,b,c,d=[],int(input("Enter the length of square matrix you will enter:")),0,[]
print(b)
for i in range(b):
    a.append([])
    for j in range(b):
        a[i].append(int(input("Enter the value at a[{}][{}]:".format(i,j))))
        print(a[i][j])
print("a=",a)
for i in range(b):
  	c+=a[i][j]
d.append(c)
c=0
for i in range(b):
		c+=a[i][b-1-i]
d.append(c)
c=0
for i in range(b):
		for j in range(b):
				c+=a[i][j]
		d.append(c)
		c=0
for i in range(b):
		for j in range(b):
				c+=a[j][i]
		d.append(c)
		c=0
c=1
for i in range(len(d)-1):
		if d[i]!=d[i+1]:
				c=0
if c!=0:
		print("It is a magic square with some=",d [i])
else:
		print("It is not a magic square")
print("time=",p ())
