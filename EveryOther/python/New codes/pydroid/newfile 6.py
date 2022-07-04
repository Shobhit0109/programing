def foo():
	def bar():
		global x
		x = 25 
	x = 20
	print(x)
	bar()
	print(x)
foo()
print(x)