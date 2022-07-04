"""
Adjacent Clone Letters

Suppose you have a 2D array of letters. A letter is adjacent to another if it is positioned either at the top, bottom, left, right, upper left, upper right, lower left or lower right of the other.

Create a program that accepts the dimensions of a 2D array and fills that array with random letters.
Then search through the array for adjacent similar letters.
Indicate which letters have adjacent clones and enumerate them. 
   
For example:
Input: 5x4
Output:
  Array:
    A C T T  S
    R T N G T
    E E G G A
    U W P F A
  Results:
    T = 4 adjacent clones
    G = 3 adjacent clones
    E = 2 adjacent clones
    A = 2 adjacent clones

"""

matrix,matrix2=[],[]
n=int (input ("Enter the size:"))
print (n)
k=0
#For input of matrix
print ("Enter the matrix:")
for i in range (n):
    matrix.append ([])
    for j in range (n):
        matrix[i].append (input ("Enter a ["+str (i)+"]["+str (j)+"]"))
        print ()
for i in matrix:
    print (i)
for i in range (n):
    for j in range (n):
        matrix2.append([])
        matrix2 [k].append (matrix [i][j])
        matrix2 [k].append (i+j)
        k+=1
for i in matrix2:
    print (i)
k=[]
for i in matrix2:
    n=0
    a,b=i [1]+1,i [1]-1
    for j in matrix2:
        if (a in j or b in j) and j [0] == i [0]:
            k.append (i [0])
            n+=1
    print ("The total adjacent character of "+i [0]+" are:",n)
