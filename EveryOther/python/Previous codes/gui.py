import turtle

print(dir(turtle))
print(turtle)
print(id(turtle))
print(type(turtle))

def func(**arg):
    print(arg)

def func(*arg):
    print(arg)

func()
func(1,2)