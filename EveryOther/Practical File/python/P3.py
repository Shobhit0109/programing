size = int(input("\n\tEnter size of lists:"))

list1 , list2 = [] , []

dic = {}

[ list1.append(int(input(f"\n\tEnter Element {i+1} of list 1  : "))) for i in range(size) ]

[ list2.append(int(input(f"\n\tEnter Element {i+1} of list 2  : "))) for i in range(size) ]

#list1 , list2 = [1,7,3,4,6], [4,6,8,5,6]

for i in range(size):
    dic[list1[i]] = list2[i]

print("\n\tYour required dictionary is: ",dic)