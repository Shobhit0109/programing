#include <bits/stdc++.h>
using namespace std;


typedef struct List {
    char ch;
    int i,j;
    struct List *next;
} sol;


sol* addList(sol *head,int m,int n,char ch) { 
    if (head == 0) {
        head = new sol;
        head->i = m;
        head->j = n;
        head->ch = ch;
        head->next = 0;
    }
    else {
        sol* temp = head;
        while(temp -> next != 0) 
            temp = temp->next;
        temp = temp->next = new sol;
        temp->i = m;
        temp->j = n;
        temp->ch = ch;
        temp->next = 0;
    }
    return head;
}
void delList(sol* head) {
    if (head == 0)
        cout << "\n\tNo solution";
    else {
        while(head != 0) {
            sol* temp = head;
            head = head -> next;
            delete temp;
        }
    }
}
void printSol(sol* head,char ch) {
    if (head == 0) 
        cout << "\n\tNo solution";
    else {
        cout << "Here's your Solutions: \n\t";
        while(head != 0) {
            if (head -> ch == ch)
                printf("\t( %d , %d )",head->i,head->j);
            head = head->next;
        }
        cout << "\n";
    }
}

char findSol(sol* head,int m,int n) {
    while(head != NULL) {
        if(head->i == m && head->j == n)
            if (head->ch == 'O')
                return 'Y';
            else 
                return 'y';
        head = head->next;
    }
    return 'n';
}

void printChess(sol*head,int size) {

    cout << "\n\tYour Chess is: ";

    for (int i = 0; i < size; i++) {

        cout << "\n\t";
        for (int j = 0; j < size; j++) 
            
            if (findSol(head, i, j) == 'y') 
                cout << "|👸|";

            else if (findSol(head, i,j) == 'Y')
                cout << "|$$|";
            else
                cout << "|  |";
    }
    cout << '\n';
}

void Solution(int m,int n,int size) {

    int i,j;
    sol* head = 0;

    for(j = 0;j < size; j++) {

        if (j != n ) head = addList(head,m,j,'r');

        if (j != m) head = addList(head,j,n,'c');

        if (j != n && m - n + j >= 0 && m - n + j < size) head = addList(head,m - n + j,j,'m');

        if (j != n && m + n - j >= 0 && m + n - j < size) head = addList(head,m + n - j,j,'o');
    }

    cout << "\n\tRow possibilties are :  " ;
    printSol(head,'r');

    cout << "\n\tColumn possibilties are :  " ;
    printSol(head,'c');

    cout << "\n\tMain diagonal possibilties are :  " ;
    printSol(head,'m');

    cout << "\n\tOther diagonal possibilties are :  " ;
    printSol(head,'o');

    addList(head,m,n,'O');
    printChess(head,size);

    delList(head);
}

int main(void){

    int n,m,size;

    cout << "\n\tEnter size of matrix: ";
    cin >> size;

    cout << "\n\tEnter row number of queen: ";
    cin >> m;

    cout << "\n\tEnter coloumn number of queen: ";
    cin >> n;

    if (m >= 0 && m <= size && n >= 0 && n <= size)
        Solution(m-1,n-1,size);
    else
        cout << "\n\tWrong input";

    cout << "\n\tWelcome back again \n\n";

    return 0;
}