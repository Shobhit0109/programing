# think of linked list in lists in python like [[],[]] isme andr wale hr ek new element and data ussi mai store kr skte hai

"""

#their is only one prblm with my list type linked list if the addrres of every new node is just like an long 1d array than prblm of mememory occurs 
#like in c for impememnting same it can make an array of nodes nd store in it then for every new node i can use reallocfunc but if memory is not available in linear order than program fails which don't happen in original method of linked list
#just checking does in python this works

a = [12,2,2,[],[],"hey","hey","1",["hey"],[]] #so every new node gets a diff address

for i in a:
    print(id(i),'\t',id(a))

a[4].append(1)
print(a)

#but in c i don't know how can i implement this method

"""


from os import system

def Add(linked_list):
    try:
        if len(linked_list) == 0:
            linked_list.append([input("\n\tEnter first element name: "),input("\n\tEnter first roll no.: ")])
            return

        ele = int(input("\n\tEnter element where to add: ")) - 1

        if 0 <= ele < len(linked_list):
            linked_list.insert(ele,[input("\n\tEnter name: "),input("\n\tEnter roll number: ")])

        else :
            print("\n\tPlease enter element index under range next time")
    except:
        print("\n\tPlease do again som error happen")
        return

def Remove(linked_list):

    if len(linked_list) == 0:
        print("\n\tNo elements to remove")
        return

    try :
        ele = int(input("\n\tEnter element number to remove: ")) - 1
    except:
        print("\n\tPlease do again some error happen")
        return

    if 0 <= ele < len(linked_list):
        return linked_list[:ele-1] + linked_list[ele + 1 :]
       
    else :
        print("\n\tPlease enter element index under range next time")
        return linked_list

def Print(linked_list):

    if len(linked_list) == 0:
        print("\n\tNo element in linked list")
        return

    print("\n\tYour list is:")
    for i in range(len(linked_list)):
        print(f"\n\t {i+1} name is : {linked_list[i][0]} \t and roll no. is :{linked_list[i][1]}")

def Add_toFile(linked_list):

    if linked_list == []:
        print("\n\tNo data to input")
        return 

    f = open("linkedList.txt","a")
    for i in linked_list:
        f.writelines(i[0]+'\n')
        f.writelines(i[1]+'\n')
    f.close()

    print("\n\tYour linked list is saved in file")

def Read_fromFile(linked_list):

    f = open("linkedList.txt", "r")

    test = []
    for i in f:            
        test.append(i.split('\n')[0])
        if len(test) == 2:
            linked_list.append(test)
            test = []
    f.close()

    Print(linked_list)

def ClearFile():

    f = open("linkedList.txt","w")
    f.close()

    print("\n\tFile cleared")
    return



linked_list = []

while(True):

    try :
        system('clear')

        temp = input("\n\t Menu is :\n\t 1 : add element to linked list \n\t 2 : remove element from linked list \n\t 3 : to print from linked list \n\t 4 : Empty list \n\t 5 : to reverse linked list\n\t 6 : To add to file \n\t 7 : to read from file \n\t 8 : Empty the file \n\n\tAnything else for exit : ")

        system('clear')
        if temp == '':
            raise ValueError

    except :
        print("\n\tno input so exit")
        temp = ''

    if temp == '1':   
        Add(linked_list)

    elif temp == '2':
        linked_list = Remove(linked_list)

    elif temp == '3':
        Print(linked_list)

    elif temp == '4' :
        print("\n\tYour linked list is emptied")
        linked_list = []

    elif temp == '5':
        linked_list = linked_list[::-1]
        print("\n\tYour linked list is reversed")

    elif temp == '6':
        Add_toFile(linked_list)

    elif temp == '7':
        Read_fromFile(linked_list)

    elif temp == '8':
        ClearFile()

    else :
        break
  
    temp = input("\n\tPlease hit enter to continue:")


print("\n\tPlease Welcome again.")