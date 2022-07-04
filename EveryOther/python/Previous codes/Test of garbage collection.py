import tracemalloc as t  

"""
class LinkedList:
    def __init__(self,num):
        self.num=num
        
t.start()

for i in range(100000):
    first = LinkedList(i)
    print(i , t.get_traced_memory() )
    
t.stop()
"""

t.start()
a = 5
a = 0 #vs  del a
print(t.get_traced_memory())
t.stop()