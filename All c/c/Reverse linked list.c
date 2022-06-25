#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int n;
    struct Node *next;
} node;

void make_list(node *L,int n) {

    int i;
    node* temp = L;

    scanf("%d",&temp->n);
    temp -> next = NULL;

    for(i=0;i<n-1;i++) {
        
        while (temp->next != NULL) 
            temp = temp->next;
            
        temp->next = (node *)malloc(sizeof(node));
        scanf("%d",&(temp->next->n));
        temp->next->next = NULL;

    }

}

void Free (node* l) {

    node* temp;

    while(l != NULL) {
        temp = l;
        l = l->next;
        free(temp);
    }
}

node *reverse_list(node *L) {

    node *rev,*temp;
    while(L->next != NULL) {
        rev = L->next;
        temp = rev->next;
        rev->next = L;
        L = temp; 
    }
    L->next = rev;
    rev = L;

    return rev;
}

int main() {

    node* L,*rev;
    int n,min;

    scanf("%d",&n);

    if(n>0) {
        L = (node *)malloc(sizeof(node));
        make_list(L,n);

        rev = reverse_list(L);

        while(rev != NULL) {
            printf("%d \n",rev-> n);
            rev = rev->next;
        }
    }
    Free(L);
    return 0;
}