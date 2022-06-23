from pickle import dump,load 

file = open("Hello.bin","wb")

a = [10,78,8]

dump(file,a)