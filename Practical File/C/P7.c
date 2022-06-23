#include <stdio.h>
#include <stdlib.h>

typedef struct node {

    int data;
    struct node *next;
} Node;

Node *first = NULL;
Node *last = NULL;

int main() {

    void Q_Display();
    void Q_Insert();
    void Q_Delete();

    int choice = 1;

    do {

        printf("\n\n\tQueue menu is:\n\t1. Add\n\t2. Delete\n\t3. Display\n\t4. Exit\n\n\t");
        scanf("%d",&choice);

        switch (choice) {

            case 1: Q_Insert();
                    break;

            case 2: Q_Delete();
                    break;

            case 3: Q_Display();
                    break;

            case 4: choice = 0;
                    break;
            default: printf("\n\tWrong choice please enter choice from menu");
        }
        
    }while(choice != 0);

    return 0;
}

void Q_Display() {

    if (first == NULL) 
        printf("\n\tNothing to print");
    else {

        int i = 0;
        Node *temp = first;

        printf("\n\tQueue is:\n");

        while( temp != NULL) {
            printf("\n\tData in %d Element is : %d",++i,temp -> data);
            temp = temp -> next;
        }
    }

}

void Q_Insert() {

    Node *temp = (Node*)malloc(sizeof(Node));

    printf("\n\tEnter Element data :");
    scanf("%d",&temp->data);

    temp -> next = NULL;

    if ( first == NULL) 
        first = last = temp;

    else {
        last -> next = temp;
        last = temp;
    }
}

void Q_Delete() {

    if (first == NULL) 
        printf("\n\t Queue is empty");
    else {
        Node *temp = first;
        first = first->next;
        free(temp);
        printf("Element from first deleted");
    }
}