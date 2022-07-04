a = []
b = []
c = "Hello"
d = "Hello"
e = 5
f = 5

print(id(a) == id(b) , id(c) == id(d), id(e) == id(f))
#list are mutable
#python varaible memory are actually their values memory except same lists can have different memories

def a(ls = []): #a list is created during intilaizarion of funct that's why same memory
    ls.append(4)
    return ls

print() 

for i in range(7):
    print(id(a()))

print()