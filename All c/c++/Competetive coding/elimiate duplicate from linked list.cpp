#include <bits/stdc++.h>
using namespace std;

typedef struct Num {
        int num;
        struct Num* next;
} List;

void printList(List* head) {

        while (head != NULL) {
                cout << head -> num << " ";
                head = head ->next;
        }
        cout << "\n";
}
List* copyList(List* head) {

        List * temp = new List;
        temp -> next = NULL;
        temp -> num = head -> num;

        List* New = temp;

        while(head->next != NULL) {

                head = head->next;
                temp -> next = new List;
                temp = temp -> next;
                temp -> next = NULL;
                temp -> num = head -> num;
        }
        return New;
}
void eliminateDup(List* head) {
        while (head->next != NULL) {
                if (head->num == head->next->num) {
                        List* temp = head->next;
                        head->next = head -> next-> next;
                        delete temp;
                }
                else 
                        head = head -> next;
        }
}

void eliminateDup_rec(List* head) {

        if (head->next == NULL) 
                return;
        
        if (head -> num == head -> next -> num) { 
                List * temp =  head->next;
                head -> next = head->next->next;
                delete temp;
                eliminateDup_rec(head);
                return;
        }
        eliminateDup_rec(head->next);
}

void eliminateDup_2pointers(List* head) {

        List *a = head ; 

        for(;;) {
                List *b = a -> next;

                if (b == NULL) 
                        break;

                if (a-> num == b-> num) {
                        a-> next = b-> next;
                        delete b;
                }
                else 
                        a = b;
        }
}

int main(void){

        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        List *head = new List , *temp;
        head->next = NULL;
        cin >> head->num ;

        temp = head;


        if (head->num == -1) {
                delete head;
                cout << "No list";
                exit(0);
        }

        while (temp -> num != -1) {
                
                temp -> next = new List;
                temp = temp -> next;
                temp -> next = NULL;
                cin >> temp -> num;     
        }
        
        temp = head;
        while(temp->next->next != NULL) 
                temp = temp -> next;
        delete temp->next;
        temp->next = NULL;
        
        temp = copyList(head);
        
        eliminateDup(head);
        printList(head);

        head = copyList(temp);

        eliminateDup_rec(temp);
        printList(temp);

        eliminateDup_2pointers(head);
        printList(head);

        return 0;
}

/*
link : https://www.codingninjas.com/codestudio/library/how-to-remove-duplicates-from-the-sorted-linked-list

In this blog, we will learn how we can remove duplicates from a sorted linked list. So let's suppose we have a linked list sorted in increasing order, and it may or may not contain some duplicate nodes. Now we need to remove all the duplicate nodes from this link list. For example-

Given linked list- 1 2 2 2 3 4 5 

After removing duplicates from the sorted linked list- 1 2 3 4 5 

There are numerous approaches to doing the above task, as we can travel through the linked list by comparing the current node with its next node and removing the next node if it is equal. Or we can also use a two-pointer approach where the first pointer helps us traverse through the linked list, and the second pointer only points to the distinct nodes in the list. Another approach could be to use an unordered map to store all the nodes, and as maps don't allow duplicates, thus we will get rid of all the duplicates. So let's see all of these methods one by one; start with the simple traversal-based approach.

Recommended: Before stepping on to the solution, try it by yourself on CodeStudio.

Approach 1: Naive 
The naive approach to solve this problem is to iterate through the linked list and keep comparing the current node with its next node, and if they are the same, delete the next node and move to the next node. Finally, print the linked list. This approach can be implemented using recursion, so let's go through both implementations one by one.

Algorithm
Take the linked list from user input-
Iterate through the linked list and compare the current node with the next node-
If they are equal, delete the next node after storing the pointer to the next node of the next node. Then link the current node with the next to the next node.
If not, then continue traversing the linked list.
Finally, print the linked list.
Implementation
#include <bits/stdc++.h>
using namespace std;
//Structure for a node in the linked list.
struct node
{
    int data;
    struct node *next;
};
//Function to remove duplicates.
void removeduplicates(node* head)
{
    //Pointer to traverse the linked list.
    node* curr=head;
    //pointer to store the next to the next pointer of the current 
    //node.
    node* nextofcurr;
    //For empty linked list.
    if(curr==nullptr)
    {
        return;
    }
    //Traversing through the linked list.
    while(curr->next!=nullptr)
    {
        //When the next node is a duplicate of the current node.
        if(curr->data==curr->next->data)
        {
            //Store the next of the next node.
            nextofcurr=curr->next->next;
            //Delete the next node
            free(curr->next);
            //Assign the next node to the iterator.
            curr->next=nextofcurr;
        }
        //When the next node is not a duplicate of the current
        //node.
        else
        {
            curr=curr->next;
        }
    }
}
//Function to push nodes into the list.
void push(struct node** headr, int new_val)
{
    //Creatng a new node.
    struct node* new_node= new node();
    //Putting the value in the node.
    new_node->data= new_val;
    //Linking the node to the list.
    new_node->next=(*headr);
    //Shifting the head pointer to the new node.
    *headr= new_node;
}
//Driver function.
int main()
{
    //Creating an empty list.
    struct node* head=nullptr;
    //Enter no  of nodes in the node.
    int size;
    cout<<"Enter the number of nodes in the list- ";
    cin>>size;
    //Pushing the nodes in it.
    cout<<"Enter the nodes in the list- ";
    for(int i=0;i<size;i++)
    {
        int a;
        cin>>a;
        push(&head,a);
    }
    //To remove duplicates from the sorted linked list.
    removeduplicates(head);
    //Printing the linked list.    
    while(head!=nullptr)
    {
        cout<<head->data<<" ";
        head=head->next;
    }
    return 0;
}
Input

7
5 4 3 2 2 2 1
Output

Enter the number of nodes in the list- 
Enter the nodes in the list-
1 2 3 4 5 
Complexity Analysis
The time complexity of this approach is- O(N), where N is the number of nodes in the linked list.

The space complexity of this approach is- O(1). 

Recursive implementation of the above approach
#include <bits/stdc++.h>
using namespace std;
//Structure for a node in linked list.
struct node
{
    int data;
    struct node *next;
};
//Function to remove duplicates.
void removeduplicates(node* head)
{
    //To store the duplicate nodes which will be deleted.
    node* todelete;
    //For empty linked list.
    if(head==nullptr)
    {
        return;
    }
    //Traversing through the linked list.
    if(head->next!=nullptr)
    {
        //When the next node is a duplicate of the current node.
        if(head->data==head->next->data)
        {
            //For removing the duplicate node.
            todelete=head->next;
            //Moving the current node to the next to the next node.
            head->next=head->next->next;
            //Delete the duplicate node
            free(todelete);
            //Recursive call to the fucntion with the next node.
            removeduplicates(head);
        }
        else
        {
            //When the next node is not a duplicate of the
            //current node.
            removeduplicates(head->next);
        }
    }
}
//Function to push nodes into the list.
void push(struct node** headr, int new_val)
{
    //Creatng a new node.
    struct node* new_node= new node();
    //Putting the value in the node.
    new_node->data= new_val;
    //Linking the node to the list.
    new_node->next=(*headr);
    //Shifting the head pointer to the new node.
    *headr= new_node;
}
//Driver function.
int main()
{
    //Creating an empty list.
    struct node* head=nullptr;
    //Enter no  of nodes in the node.
    int size;
    cout<<"Enter the number of nodes in the list- ";
    cin>>size;
    //Pushing the nodes in it.
    cout<<"Enter the nodes in the list- ";
    for(int i=0;i<size;i++)
    {
        int a;
        cin>>a;
        push(&head,a);
    }
    //To remove duplicates from the sorted linked list.
    removeduplicates(head);
    //Printing the linked list.    
    while(head!=nullptr)
    {
        cout<<head->data<<" ";
        head=head->next;
    }
    return 0;
}
Input

7
5 4 3 2 2 2 1
Output

Enter the number of nodes in the list- 
Enter the nodes in the list-
1 2 3 4 5 
Complexity Analysis
The time complexity of this approach is- O(N)

The space complexity of this approach is- O(N)

Approach 2: Using Two Pointers
This approach uses two-pointers to remove duplicates from the sorted linked list. The first pointer iterates through the whole list. And the second pointer moves over only those nodes which are distinct. While iterating through the list, whenever the first pointer encounter duplicate nodes, it skips them, and when it encounters a distinct node, it moves the second pointer from the last distinct node to this new node.

Algorithm
Take the linked list from user input-
Declare two-pointers and initialize them with the head of the linked list
Iterate through the list using the first pointer-
If it encounters a node that duplicates its previous, it does nothing, and if the node is distinct, it moves the second pointer to that node.
Print the linked list.
Implementation
#include <bits/stdc++.h>
using namespace std;
//Structure for a node in linked list.
struct node
{
    int data;
    struct node *next;
};
//Function to remove duplicates.
void removeduplicates(node* head)
{
    //Two reference pointers, one for iterating through the linked 
    //list, another for pointing to first occurence of every 
    //distinct node.
    node *ptr1 =head;
    node *ptr2=head;
    //Traversing through the list.
    while(ptr1!=nullptr)
    {
        //Comparing the current node with the next node.
        if(ptr1->data!=ptr2->data)
        {
            //If a new node is found, skip the duplicates.
            ptr2->next=ptr1;
            ptr2=ptr1;
        }
        //Move the iterator to the next node.
        ptr1=ptr1->next;
    }
    //When the last node has duplicates.
    if(ptr2!=ptr1)
    {
        ptr2->next=nullptr;
    }
}
//Function to push nodes into the list.
void push(struct node** headr, int new_val)
{
    //Creatng a new node.
    struct node* new_node= new node();
    //Putting the value in the node.
    new_node->data= new_val;
    //Linking the node to the list.
    new_node->next=(*headr);
    //Shifting the head pointer to the new node.
    *headr= new_node;
}
//Driver function.
int main()
{
    //Creating an empty list.
    struct node* head=nullptr;
    //Enter no  of nodes in the node.
    int size;
    cout<<"Enter the number of nodes in the list- ";
    cin>>size;
    //Pushing the nodes in it.
    cout<<"Enter the nodes in the list- ";
    for(int i=0;i<size;i++)
    {
        int a;
        cin>>a;
        push(&head,a);
    }
    //To remove duplicates from the sorted linked list.
    removeduplicates(head);
    //Printing the linked list.    
    while(head!=nullptr)
    {
        cout<<head->data<<" ";
        head=head->next;
    }
    return 0;
}
Input

7
5 4 3 2 2 2 1
Output

Enter the number of nodes in the list- 
Enter the nodes in the list-
1 2 3 4 5 
Complexity Analysis
The time complexity of this approach is- O(N)

The space complexity of this approach is- O(1)

Approach 3: Using Maps
Another approach to solving this problem is using maps. We traverse through the linked list and check if the node has already occurred or node. If it has not occurred, we print it and mark it as visited on the map. And skip it if it is already visited.

Algorithm
Take the linked list from user input-
Create a map that takes node data and boolean variables as key-value pairs.
Traverse through the linked list, and if a node appears for the first time or not-
If Yes, print it and mark it as visited on the map.
Else move on to the next node.
Implementation
#include <bits/stdc++.h>
using namespace std;
//Structure for a node in the linked list.
struct node
{
    int data;
    struct node *next;
};
//Function to remove duplicates.
void removeduplicates(node* head)
{
    //Map to store the distinct values.
    unordered_map<int, bool> distinctnodes;
    //To traverse through the nodes.
    node* curr=head;
    while(curr)
    {
        //If the current nodes is its first occurence.
        if(distinctnodes.find(curr->data)==distinctnodes.end())
        {
            cout<<curr->data<<" ";
        }
        //Marked the node as visited.
        distinctnodes[curr->data]=true;
        curr=curr->next;
    }
}
//Function to push nodes into the list.
void push(struct node** headr, int new_val)
{
    //Creatng a new node.
    struct node* new_node= new node();
    //Putting the value in the node.
    new_node->data= new_val;
    //Linking the node to the list.
    new_node->next=(*headr);
    //Shifting the head pointer to the new node.
    *headr= new_node;
}
//Driver function.
int main()
{
    //Creating an empty list.
    struct node* head=nullptr;
    //Enter no  of nodes in the node.
    int size;
    cout<<"Enter the number of nodes in the list- ";
    cin>>size;
    //Pushing the nodes in it.
    cout<<"Enter the nodes in the list- ";
    for(int i=0;i<size;i++)
    {
        int a;
        cin>>a;
        push(&head,a);
    }
    //To remove duplicates from the sorted linked list.
    removeduplicates(head);
}
Input

7
5 4 3 2 2 2 1
Output

Enter the number of nodes in the list- 
Enter the nodes in the list-
1 2 3 4 5 
Complexity Analysis
The time complexity of this approach is- O(N)

The space complexity of this approach is- O(1)

Frequently Asked Questions
What are the types of the linked list?
The linked list is generally of four types-   
- Singly-linked list 
- Doubly linked list
- Circular linked list
- Doubly circular linked list
 

What is the difference between array and linked lists?
The array is a contiguous block of elements of similar data types. In contrast, a linked list is a collection of objects called nodes. These nodes contain data and pointers to the next nodes in the linked list. These nodes are not necessarily stored in contiguous memory blocks.
 

What is random access to elements? Is it possible in a linked list?
Random access of elements refers to a condition when we can access any element in a collection of elements directly in one step, i.e., in O(1) time. It is possible in an array but not in linked lists.
 

What is the time complexity of insert operation on unordered maps in C++ STL?
The insert operation on unordered maps in C++ STL is constant O(1) in average cases and linear O(N) in worst cases.
 

What is the difference between a node in a singly linked list and a doubly-linked list?
A node in a singly linked list only contains data and the pointer to the next node, whereas a doubly-linked list contains data and pointers to the next and previous nodes.

*/