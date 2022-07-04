from time import process_time as p
from time import time as t
t1=t()
print(type(p),type(t))
print(p,t)
print(p(),t()-t1)
