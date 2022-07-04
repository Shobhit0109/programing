a,b,c,d=[],[],[],[]
m=9   
print("Enter the matrix:")
for i in range(m):
    a.append([])
    b.append([])
    c.append([])
    d.append([])
    for j in range(m):
        a[i].append(int(input()))

for i in range(m):
    for j in range(m):
        if a[i][j] not in b[i]:
            b[i].append(a[i][j])
        if a[j][i] not in c[i]:
            c[i].append(a[j][i])
        d[i].append(a[j][i])
try:
    if len(c)!=len(d) and len(a)!=len(b):
    		print(5/0)
      
    for k in range(0,m,3):      
        c=[]
        d=[]            
        for j in range(k,3):			    			
   		     for i in range(k,3):
    				    c.append(a[j][i])
    				    if a[j][i] not in d:
    						    d.append(a[j][i])
        if len(c)!=len(d):
        		print(5/0)
    print("It is a sudoku")
except ZeroDivisionError:
        print("It is not a sudoku")
raise ZeroDivisionError("You are a loser")
    
