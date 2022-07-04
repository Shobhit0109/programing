"""
Garland Words

A Garland word is one that starts and ends with the same N letters in the same order, for some N greater than 0, but less than the length of the word. N is called the garland word's degree. 

For instance, "onion" is a garland word of degree 2, because its first 2 letters "on" are the same as its last 2 letters: onion.

Write an program, that will take a word as input and output whether it's a garland word along with the corresponding degree.

"""
from math import ceil
from time import process_time as time

st=input ("Enter the word:")
print (st)
n=0
print("Garland word is:",end="")
for i in range (len (st)//2):
    if st [i]==st [i+ceil (len (st)/2)]:
        n+=1
        print (st [i],end="")
    else:
        break
print ()
print ("Total garland degree is:"+str (n)+"\nTotal time taken:"+str (time ()))
