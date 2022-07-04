def makeIndex(index,com):

        index[-1] += 1

        for i in range(len(index)):
                for j in range(i+1,len(index)):
                        if index[i] == index[j]:
                                index[j] += 1

        i = len(index) - 1
        while (i > 0):
                if index[i] >= len(com):
                        index[i] = 0
                        index[i-1] += 1
                        i += 1
                i -= 1
        return

def checkCan(com,res):
        for i in range(1,len(com)+1):
                index = [0 for j in range(i)]

                while index[0] < len(com):

                        string = ""
                        for i in index:
                                string += com[i]
                        
                        if string == res:
                                return 1
                        
                        makeIndex(index,com)    
                                     
        return 0

def Main():
        try:
                com = input().split()
                if com == []:
                        raise ValueError

                res = input()
                if res == '':
                        raise ValueError
        except: 
                com = 'fly on a new case'.split()
                res = 'yup'

        if checkCan(com,res):
                print("YES")
        else:
                print("NO")
        return


if __name__ == "__main__":
        Main()

"""
link : https://www.tutorialspoint.com/check-if-given-string-can-be-formed-by-concatenating-string-elements-of-list-in-python

 Check if given string can be formed by concatenating string elements of list in Python

We sometimes need to check if a required string can be formed from many number of strings that are present in a list. It also should not matter in what order the strings are present in the list which have to be joined to get the required string.

With permutations
From itertools we can use the permutations function which will give us the possible combinations of the strings in the list in various order. As soon as a given combination matches the required string, we conclude that the string can be formed.

Example:

from itertools import permutations

chk_str = 'balloon'
Alist = ['fly','on', 'o', 'hot', 'ball', 'air']

def findstring(strchk, biglist):
   for i in range(2, len(biglist) + 1):
      for perm in permutations(biglist, i):
         if ''.join(perm) == strchk:
         return True
   return False

# Using the function
if(findstring(chk_str,Alist)):
   print("String can be formed.")
else:
   print("String can not be formed.")

Output
Running the above code gives us the following result −

String can be formed.
With Regular Expressions
The re module provides the compile function which will create the possible strings by specifying the regular expression pattern. Then it will be compared with the string to be checked. If the result is not none then we can conclude the string can be formed.

Example
 
 import re

chk_str = 'balloon'
Alist = ['fly','on', 'o', 'hot', 'ball', 'air']

def findstring(strchk, biglist):
   r = re.compile("(?:" + "|".join(biglist) + ")*$")
   if r.match(strchk) != None:
      return True
   return False

# Using the function
if(findstring(chk_str,Alist)):
   print("String can be formed.")
else:
   print("String can not be formed.")
Output
Running the above code gives us the following result −

String can be formed.


"""