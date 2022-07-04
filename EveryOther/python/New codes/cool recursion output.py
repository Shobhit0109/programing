def fun(x,y):
    
    if not x: 
        print(f"{y}",end='');return y+1
    
    if not y: 
        return fun(x-1,1)
    
    else: 
        return fun(x-1,fun(x,y-1))
    
    
print(fun(3,3))