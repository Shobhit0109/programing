import os, sys
#import json, re, time, datetime, random, string, math, array, urllib, urllib2, urlparse, hashlib, hmac, binascii, base64 


def Main():
    index = lambda i,j,n : ((i)*(n)+(j))
    print(f"Your file name is: {sys.argv[0].split('/')[-1]}")
    if len(sys.argv) > 1:
        print("You have arguments also !!")
    else: 
        print("No arguments!!",end="\n\n")
        
        
    s = list(" hey i  Am yj -Brither")
    
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            s[i] = chr(ord(s[i]) + 32)
            
    print(''.join(s))
    
    return

if __name__ == "__main__":
    Main()
    