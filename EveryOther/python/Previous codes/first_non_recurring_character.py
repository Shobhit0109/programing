string = input()

def non(index):
	global string
	i = 0
	while i < len(string):
		if index != i and string[i] == string[index]:
			return False
		return True
		
for i in string:
	if(non(string.index(i))):
		print(i)
		break
		
else:
	print("None")