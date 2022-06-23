with open("/home/shobhit/Documents/programing/All codes Execution files/pip.txt",'r') as file:
	temp = 'pip install --upgrade '
	for i in file.read().split()[4::2]:
		temp += i+' '
with open("/home/shobhit/Documents/programing/All codes Execution files/pip.txt",'w') as file:
	file.write(temp)
