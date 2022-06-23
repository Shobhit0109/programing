"""
Minimal Pairs Product Sum

Write a function that receives an array of integers and returns the minimal sum of the array (sum of products of each two adjacent numbers).

For Example: 
Without sorting the array [40,25,10,5,1], the sum is:
(40*25) + (25*10) + (10*5) + (5*1) = 1305

The challenge is to find the best possible sort of the array elements, to have the minimal sum result.

The expected output for the array [40,25,10,5,1]  is 225.

"""
from itertools import permutations as perm

def arrsum (a):
    sum=0
    for i in range (0,len(a)-1):
        sum+=(a [i] * a [i+1])
    return sum
    
def prod (arr):
    Str=[]
    for i in range (len (arr)-1):
        Str.append("({}*{})".format (arr [i],arr [i+1]))
    Str="+".join (Str)
    return Str

arr=[]
n=int (input ("Enter the limit:"))
print (n)
#Alt:arr=list (map (int,input.split ()))
for i in range (n):
    arr.append (int (input ()))
print (arr)

alt=list (perm (arr))
    
sum=list (map (arrsum,alt))
Min=sum [0]
num=0
for i in range (len (sum)):
    if Min>sum [i]:
        num=i
        Min=sum [i]
print ("The array is:",alt [num])
print ("The sum is:",sum [num])
print ("The function is:",prod (alt[num]))
