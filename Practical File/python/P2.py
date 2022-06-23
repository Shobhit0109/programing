size = int(input("\n\tEnter size of lists:"))

list1 , list2 = [] , []

[ list1.append(int(input(f"\n\tEnter Element {i+1} of list 1  : "))) for i in range(size) ]

[ list2.append(int(input(f"\n\tEnter Element {i+1} of list 2  : "))) for i in range(size) ]

print()

for i in range(size):
    print(f"Element {i+1} of list 1 is : {list1[i]}")
    print(f"Element {size - i} of list 2 is : {list2[size - 1 - i]}")

print("\n\tThank you")