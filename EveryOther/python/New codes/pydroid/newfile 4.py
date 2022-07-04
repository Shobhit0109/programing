#all python variables are pointers to values
a = [6,6]

b = a

b +=  [3,6] #also change values in a

print(id(b)==id(a)) #true

b = b + [1] #no change in a 

print(id(b)==id(a)) #false

#so python ke andr operators alg tarike se kaam krte hai