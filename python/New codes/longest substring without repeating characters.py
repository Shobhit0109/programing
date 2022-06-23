from time import time,process_time 

def Input():
   try :
      string = input("\n\tEnter Your String : ")
      print()
      if string == "" : 
         raise ValueError
      
   except:
      print( end = "\n\tPlease enter a string running code with default value : \"abcabccab\"\n")
      string = "abcabccabd"
      
   return string

def ProcessMine(string):
           
   result = [0,'']
   for i in range(len(string)):
      for j in range(i,len(string)):
                 
         temp = string[i:j+1]
         
         if len(temp) > result[0] and len( list(temp)) == len( set(temp)):
                    
            result[0] = len(temp)
            result[1] = temp
            
   return result
            
def ProcessYoutube(string):
   #From: https://youtu.be/1TO7MdxC4oM
   temp, result = "" , [0,'']
   
   
   for i in string:
      if i in temp:
         if len(temp) > result[0]: 
            result[0] = len(temp)
            result[1] = temp
            
         temp = temp[temp.index(i)+1:]
      temp = ''.join([temp,i])
         
   if len(temp) > result[0]:
      result[0] = len(temp)
      result[1] = temp
   
   return result
         
def Main():
   t, p = time, process_time
   string = Input()
   for process in [ProcessMine,ProcessYoutube]:
      start = [t(),p()]
      result = process(string)
      print(end=f"\n\tLargest Substring is : \"{result[1]}\" and length of this substring is : {result[0]}\n and time taken is : {(t()-start[0])} || {(p() - start[1])} in seconds\n")
   print()
   
if __name__=='__main__':
   Main()
   
"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""