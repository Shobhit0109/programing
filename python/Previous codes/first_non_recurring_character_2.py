string = input()
st = list( string[:] )

for i in string:	
	if i in st:
		st.remove(i)
	else:
		continue
		
	if i not in st:
		print(i)
		break
	while i in st:
		st.remove(i)
		
else:
	print("None")