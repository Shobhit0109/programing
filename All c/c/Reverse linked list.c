#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int n;
    struct Node *next;
} node;

void make_list(node *L,int n) {

    int i;
    node* temp = L;

    printf("\n\tEnter the first elements of the list: ");
    scanf("%d",&temp->n);
    temp -> next = NULL;

    for(i=0;i<n-1;i++) {
        
        while (temp->next != NULL) 
            temp = temp->next;
            
        temp->next = (node *)malloc(sizeof(node));
        printf("\n\tEnter the value of node %d: ",i+2);
        scanf("%d",&(temp->next->n));
        temp->next->next = NULL;
    }
}

void Free (node* l) {

    while(l != NULL) {
        node* temp = l;
        l = l->next;
        free(temp);
    }
}

node *reverse_list(node *L,int n) {
    for (int i=0;i < n-1;i++) {
        node* temp = L,*next = L -> next;
        for (int j = 0; j < n-i-1;j++,temp = temp->next);
        L -> next = temp -> next;
        temp -> next = L;
        L = next;
    }
    return L;
}

int main() {

    int n;
    printf("\n\tEnter the number of nodes: ");
    scanf("%d",&n);

    if(n>0) {
        node *list , *temp;
        list = (node *)malloc(sizeof(node));
        make_list(list,n);

        temp = list = reverse_list(list,n);

        n = 0;
        printf("\n\tThe reverse list is: \n");

        while(list != NULL) {
            printf("\n\tThe %d element of reversed list is: %d",++n,list-> n);
            list = list->next;
        }
        Free(temp);
    }
    return 0;
}