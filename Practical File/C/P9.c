#include <stdio.h>
#include <stdlib.h>

typedef struct node {

    char name[20] , city[10] , state[10];
    size_t zip;
    struct node *next;

} list;

list *first = NULL;
list *last = NULL;

int size = 0;

int main() {

    void Q_Insert();
    void Q_Delete();

    int choice = 1;

    do {

        printf("\n\n\tMenu is:\n\t1. Add Address\n\t2. Delete Address\n\t3. Exit\n\n\t");
        scanf("%d",&choice);

        switch (choice) {

            case 1: Q_Insert();
                    break;

            case 2: Q_Delete();
                    break;

            case 3: choice = 0;
                    printf("\n\tWelcome back again ...");
                    break;
            default: printf("\n\tWrong choice please enter choice from menu");
        }
        
    }while(choice != 0);

    return 0;
}

void Q_Insert() {

    size += 1;

    list *temp = (list*)malloc(sizeof(list));

    printf("\n\tEnter Address details");

    printf("\n\tEnter name :");
    scanf("%s",temp->name);

    printf("\n\tEnter city :");
    scanf("%s",temp->city);

    printf("\n\tEnter state :");
    scanf("%s",temp->state);

    printf("\n\tEnter zip code:");
    scanf("%zu",&temp->zip);

    temp->next = NULL;

    if ( first == NULL) 
        first = last = temp;

    else {
        last -> next = temp;
        last = temp;
    }
    printf("\n\tAddress added");
}
void Q_Delete() {

    int num  , i = 1;

    printf("\n\tEnter address number to be deleted:");
    scanf("%d",&num);

    if (num > size || num == 0) {
        printf("\n\tAddress doesn't exist");
        return;
    }

    list* temp = first;

    if (num == 1) {
        if (size == 1) {
            first = last = NULL;
            free(temp);
        }
        else {
            first = first -> next ;
            free(temp);
        }
    }
    else 
        for(;;) {
            if(++i == num) {
                list *t = temp->next->next;
                free(temp->next);
                temp->next = t;
                break;
            }   temp = temp->next;
        }
    printf("\n\tAddress deleted");
    size -= 1;
}