"""
Summations Calculator

Create a program that takes 3 inputs, a lower bound, an upper bound and the expression. Calculate the sum of that range based on the given expression and output the result.

For Example:
Input: 2 4 *2
Output: 18 (2*2 + 3*2 + 4*2)

Input: 1 5 %2
Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)

"""
try:
    n1,n2,com=list (input ().split ())
    n1,n2=int (n1),int (n2)
    print ("Input:",n1,n2,com)
    sl=[]
    sm=0
    for i in range (n1,n2+1):
        sl.append (str (i)+com)
        sm+=eval (str (i)+com)
    print ("Output:",sm,"({})".format ("+".join (sl)))
except ValueError:
    print ("Please enter write input as in format \"(int) (int) (func)(int)\"")
    
finally:
    print ("That's all")