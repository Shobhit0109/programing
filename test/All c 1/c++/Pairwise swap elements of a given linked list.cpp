#include <bits/stdc++.h>
using namespace std;

typedef struct node {
    int n;
    struct node *next;
} Node;

Node * head = 0, *tem = 0;

void Node_make (int i) {
    if (head == 0) {
        head = new Node;
        head->n=i;
        head->next=0;
    }
    else {
        Node * temp= head;
        while (temp -> next != 0) 
            temp = temp -> next;
        temp->next = new Node;
        temp->next->n = i;
        temp->next->next = 0;
    }
}

void Node_print() {
    
    if(head == 0) 
        cout << "\n\tNo tem to print";
    
    else {
        cout << "\n\tYour tem is:\n\t";
        Node* temp = head;
        while(temp != 0) {
            cout << temp -> n << " ";
            temp = temp -> next;
        }
        cout << "\n";
    }
}

void Node_rev () {
    
    Node *temp = head;
    
    while(temp != 0) {
        if(temp->next != 0) {
            if(tem == 0) 
                tem = temp->next;                                
            else {
                Node * t = tem;
                while(t->next != 0)
                    t = t->next;
                t->next = temp->next;
            }
            Node* t = temp->next->next;
            temp->next->next = temp;
            temp->next = 0;
            temp = t;        
        }
            
        else {
            if(tem == 0)
                tem = temp;
            else {
                Node * t = tem;
                while(t->next != 0)
                    t = t->next;
                t->next = temp;
            }
            break;
        }
    }
    head = tem;
}
void Node_rev_vibhanshu () {
    
    Node * temp = head;
    while(temp-> next != 0) {
    
	    int n = temp->n;
        temp -> n = temp->next->n;
        temp->next->n = n;
        temp = temp->next->next ;
    }
}

void Node_rev_gurpreet () {

    Node * a, * b, * c ,* temp = head;
    int i = 1;
    
    head = temp-> next;
    do {
    
        a = temp;
        b = temp-> next;
        c = temp-> next-> next;
        
        if(i>0) {        
            a-> next = c;
            b-> next = a;
        }
        else if (c != 0) {
            a-> next = c;
            temp = b;
        }
        i *= -1;

    } while(c != 0);
}

int main() {

    for(int i = 0; i < 5 ; i++)
        Node_make(1+i); 
    cout << "\n--------------------------------";
    Node_print();
        
    Node_rev();
    cout << "\n--------------------------------";
    Node_print ();
    
    Node_rev_vibhanshu();
    cout << "\n--------------------------------";
    Node_print();
    
    Node_rev_gurpreet();
    cout << "\n--------------------------------";
    Node_print ();

    return 0;
}

/*
link : https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-tem/
Given a singly linked tem, write a function to swap elements pairwise. 

Input : 1->2->3->4->5->6->NULL 
Output : 2->1->4->3->6->5->NULL

Input : 1->2->3->4->5->NULL 
Output : 2->1->4->3->5->NULL

Input : 1->NULL 
Output : 1->NULL 
 

For example, if the linked tem is 1->2->3->4->5 then the function should change it to 2->1->4->3->5, and if the linked tem is then the function should change it to.  

*/
