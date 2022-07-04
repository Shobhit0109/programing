x={0:"000",1:"001",2:"010",3:"011",4:"100",5:"101",6:"110",7:"111"}
y=input("Enter the octal number:\n")
for i in y:
	if i=='.':
		print(i,end="")
	else:
		print(x[int(i)],end="")

y=ord (y)
