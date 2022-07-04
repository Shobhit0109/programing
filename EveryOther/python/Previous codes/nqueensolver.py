def binary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       binary(n//2)
   print (n%2,end="")

# Take decimal number from user
dec = float(input("Enter a number : "))

print
print ("The binary representation of ",dec," is ",)
binary(dec)
