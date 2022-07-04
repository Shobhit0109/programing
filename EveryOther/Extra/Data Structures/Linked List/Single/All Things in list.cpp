#include <bits/stdc++.h>
using namespace std;

class LinkedList {
        public: 
                int num_items;
                LinkedList *next = NULL;

                LinkedList* insert(LinkedList *,int);
                LinkedList* remove(LinkedList *,int);
                void print(LinkedList *);
                int size(LinkedList *);
};

LinkedList* LinkedList::insert(LinkedList *head,int size) { 

        if (head == NULL) {

                head = new LinkedList;
                cout << "\n\tEnter number of first element of linked list : ";
                cin >> head -> num_items;
                head -> next = NULL;

                cout << "\n\tElement added";
                return head;
        }

        int pos , i;
        cout << "\n\tEnter position to put your linked list element (0 to "<< size  << " ) : ";
        cin >> pos;

        if (pos < 0 || pos > size ) {
                cout << "\n\tEnter position between range";
                return head;
        }

        LinkedList* temp = head;
        if ( pos == 0 ) {
                temp = new LinkedList;
                
                cout << "\n\tEnter number of new element : ";
                cin >> temp-> num_items;

                temp -> next = head;

                cout << "\n\tElement added";
                return temp;
        }

        for ( i = 0; i < pos-1; i++ , temp = temp->next);
        LinkedList* add = new LinkedList;

        cout << "\n\tEnter number of new element : ";
        cin >> add-> num_items;

        add->next = temp-> next;
        temp -> next = add;

        cout << "\n\tElement added";
        return head;
}


LinkedList* LinkedList::remove(LinkedList *head,int size) { 

        if (head == NULL) {
                cout << "\n\tNo linked list to delete";
                return head;
        }

        int pos , i;
        cout << "\n\tEnter position to remove your linked list element (0 to "<< size - 1 << " ) : ";
        cin >> pos;

        if (pos < 0 || pos > size ) {
                cout << "\n\tEnter position between range";
                return head;
        }

        LinkedList* temp = head;
        if ( pos == 0 ) {
                temp = head -> next;
                delete head;
                cout << "\n\tElement deleted";
                return temp;
        }

        for ( i = 0; i < pos-1; i++ , temp = temp->next);
        LinkedList* del = temp -> next;

        temp -> next = temp->next->next;
        delete del;
        cout << "\n\tElement deleted";
        return head;
}

void LinkedList::print(LinkedList* head) { 

        if ( head == NULL ) { 
                cout << "\n\tNo linked list found";
                return;
        }
        cout << "\n\tYour linked list is : \n\t";
        while ( head->next != NULL ) { 
                cout << head -> num_items << "  ->   ";
                head = head -> next;
        }
        cout << head -> num_items;
}

int LinkedList::size(LinkedList* head) {
        int size = 0;
        for(;head != NULL;head = head->next,size++);
        return size;
}

int main(void) {

        cout << "\n\t********       Welcome        *************";
        int choice = 0;
        LinkedList* head = NULL , temp;

        for (;;) { 

                cout << "\n\tThe menu is:\n\t1. Add element at some position\n\t2. Delete element at some position\n\t3. Print the list\n\t4. Exit\n\t---> choice = ";
                cin >> choice;

                //system("clear");

                switch(choice) {
                        case 1: head = temp.insert(head,temp.size(head));
                                break;
                        case 2: head = temp.remove(head,temp.size(head)); 
                                break;
                        case 3: temp.print(head);
                                break;
                        case 4: cout << "\n\tThanks for coming.........\n\tWelcome back again\n\n";
                                while(head != NULL) {
                                        LinkedList* node = head;
                                        head = head->next;
                                        delete node;
                                }
                                exit(0);
                        default: cout << "\n\tInvalid choice pls enter from menu";
                }
        }
        return 0;
}