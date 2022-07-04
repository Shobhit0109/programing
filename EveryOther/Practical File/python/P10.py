queue = []

def push(queue):
    queue.append(int(input("\n\tEnter number : ")))
    print("\tElement added")

def pull(queue):
    if queue == []:
        print("\tQueue is empty")
        return []
    
    print(f"\tElement removed is: {queue[0]}")
    return queue[1:]

def show(queue):
    if queue == []:
        print("\tNothing to Show")
        return

    for i in range(len(queue)):
        print(f"Element {i+1} of Queue is : {queue[i]}")

while(True):

    choice = int(input("\n\tQueue Menu is:\n\t1. Add number\n\t2. Remove number\n\t3. Show numbers in queue\n\t4. Exit\n\n\t"))

    if choice == 1:
        print()
        push(queue)

    elif choice == 2:
        print()
        queue = pull(queue)

    elif choice == 3:
        print()
        show(queue)

    elif choice == 4:
        print("\n\n\tWelcome back again __EXIT__")
        exit(0)

    else:
        print("\n\t Please Enter Choice from menu")




        