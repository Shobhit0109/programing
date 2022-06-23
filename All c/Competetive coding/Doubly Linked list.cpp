//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

#define f(i,n) for (int i = 0; i < (n); i++)
#define i(i,j,n) ((i)*(n) + (j))

typedef struct Struct {
  int value;
  struct Struct *prev,*next;
} Dhruv;

int lengthDhruv(Dhruv* head) {
  int length = 0;
  while (head != 0) {
    head = head -> next;
    length ++;
  }
  return length;
}

void addDhruv(Dhruv** head,Dhruv** tail) {
  
  int input,pos;
  
  cout << "\n\tEnter the number to input:";
  cin >> input;

  cout << "\n\tEnter the position of number to input (in range 0 to " << lengthDhruv(*head) << "): ";
  cin >> pos;

  if (pos > lengthDhruv(*head)) 
    cout << "\n\tEnter length in size of list  !!returning ";

  else if (*head == 0) {
    cout << "\n\tFirst node entered";
    *head = *tail = new Dhruv;
    (*head) -> next = (*head) -> prev = 0;
    
  }
  
  else if (pos == 0) {
    cout << "\n\tNode entered";
    Dhruv* temp = new Dhruv;
    temp -> value = input;
    temp -> next = *head;
    (*head) -> prev = temp;
    *head = temp; 

  }
    
  else {
    Dhruv* temp = 0;
    for(temp = *head;--pos;temp = temp->next);
    temp -> next -> prev = new Dhruv;
    temp -> next -> prev -> value = input;
    temp -> next -> prev -> next = temp -> next;
    temp -> next -> prev -> prev = temp;
    temp -> next = temp -> next -> prev;
    cout << "\n\tNode entered";
  }
  

  return;
}

void printDhruv(Dhruv* head) {

    if (head == 0) {
        cout << "\n\tList is empty";
        return;
    }

  cout << "\n\tHere's your list:\t";
  while (head != 0) {
    cout << head -> value << " -> ";
    head = head -> next;
  }
  cout << '\n';
}

void deleteDhruv(Dhruv** head, Dhruv** tail) {

  int pos;
  
  cout << "\n\tEnter position to delete number (range 0 to " << lengthDhruv(*head) - 1 << "): ";
  cin >> pos;

  if (*head == 0) 
    cout << "\n\tNo linked list !!returning";

  else if (pos >= lengthDhruv(*head)) 
    cout << "\n\tEnter position in range !!returning";
    
  else if (pos == 0) {
    (*head) -> next -> prev = 0;
    Dhruv* temp = *head;
    *head = (*head) -> next;
    delete temp;
  }
  
  else if (pos == lengthDhruv(*head) - 1) {
    Dhruv* temp = (*tail);
    (*tail) -> prev -> next = 0;
    (*tail) = (*tail) -> prev;
    delete temp;
  }
  else {
    Dhruv* temp = 0;
    for(temp = *head;--pos;temp = temp->next);
    temp -> next -> prev = temp -> prev;
    temp -> prev -> next = temp -> next;
    delete temp;
  }
}

void deleteAllDhruv(Dhruv* head) {
  
  while(head != 0) {
    
    Dhruv* temp = head;
    head = head -> next;
    delete temp;
  }
  cout << "\n\tList deleted";
}

void fileWriteDhruv(Dhruv* head) {
  
  int choice = 0;

  cout << "\n\tEnter 1 to write to file or 2 to append: ";
  cin >> choice;

  FILE* fp = 0;
  switch (choice) {
    case 1:
      fp = fopen("/home/shobhit/Documents/programing/All codes Execution/Dhruv.txt","w");
      break;
    case 2:
      fp = fopen("/home/shobhit/Documents/programing/All codes Execution/Dhruv.txt","a");
      break;
    default:
      cout << "\n\tWrong input!! Returning";
      return;
  }

  if (fp == 0) {
    cout << "\n\tFile not found !!returning";
    return;
  }
  if (head == 0) {
    cout << "\n\tList is empty !!returning";
    return;
  }

  while (head != 0) {
    fprintf(fp,"%d\n",head -> value);
    head = head -> next;
  }

  fclose(fp);
  cout << "\n\tFile written";
}

void fileReadDhruv(Dhruv** head, Dhruv** tail) {
  
  FILE* fp = fopen("Dhruv.txt","r");
  if (fp == 0) {
    cout << "\n\tFile not found !!returning";
    return;
  }

  int choice = 0;
  cout << "\n\tEnter 0 to append the file contents to head or 1 to make a new list: ";
  cin >> choice;

  switch (choice) {
    case 0:
      while (fscanf(fp,"%d\n",&choice) != EOF) {
        if (*head == 0) {
          *head = *tail = new Dhruv;
          (*head) -> next = (*head) -> prev = 0;
        }
        else {
          (*tail) -> next = new Dhruv;
          (*tail) -> next -> prev = *tail;
          *tail = (*tail) -> next;
        }
        (*tail) -> value = choice;
      }
      cout << "\n\tFile read \n\tlist appended to head";
      break;
    case 1:
      deleteAllDhruv(*head);
      *head = *tail = 0;
      while (fscanf(fp,"%d\n",&choice) != EOF) {
        if (*head == 0) {
          *head = *tail = new Dhruv;
          (*head) -> next = (*head) -> prev = 0;
        }
        else {
          (*tail) -> next = new Dhruv;
          (*tail) -> next -> prev = *tail;
          *tail = (*tail) -> next;
        }
        (*tail) -> value = choice;
      }

      cout << "\n\tFile read\n\tNew list created";
      break;
    default:
      cout << "\n\tWrong input!! Returning";
  }
  
  fclose(fp);
}

int main(void) {

/*
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(0);
  
#ifndef ONLINE_JUDGE

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

#endif
*/
  Dhruv *head = 0 , *tail = 0;  
  for(;;) {
    int choice = 5;
    cout << "\n\tThe menu is:\n\t1. Add node\n\t2. Print list\n\t3. Delete node\n\t4. Delete all nodes\n\t5. Exit\n\t6. Clear screen\n\t7. Write to File\n\t8. Read from File\n\n\tEnter your choice: ";
    cin >> choice;

    switch (choice) {

      case 1:
        addDhruv(&head,&tail);
        break;
      case 2:
        printDhruv(head);
        break;
      case 3:
        deleteDhruv(&head,&tail);
        break;
      case 4:
        deleteAllDhruv(head);
        break;
      case 5:
        cout << "\n\tExiting!! Welcome again";
        return 0;
      case 6:
        fflush(stdin);
        system("clear");
        break;
      case 7:
        fileWriteDhruv(head);
        break;
      case 8:
        fileReadDhruv(&head,&tail);
        break;
      default:
        cout << "\n\tEnter valid choice !!returning";
    }
  } 
}