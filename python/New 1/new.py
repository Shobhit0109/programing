import os, sys
#import json, re, time, datetime, random, string, math, array, urllib, urllib2, urlparse, hashlib, hmac, binascii, base64 


def Main():
    index = lambda i,j,n : ((i)*(n)+(j))
    print(f"Your file name is: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print("You have arguments also !!")
    else: 
        print("No arguments!!")
    
    return

if __name__ == "__main__":
    Main()