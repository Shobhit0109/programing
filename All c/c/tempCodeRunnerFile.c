#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int n;
    struct Node *next;
} node;

void make_list(node *L,int n) {

    int i;
    node* temp = L;

    for(i=0;i<n;i++) {
        
        while (temp->next != NULL) 
            temp = temp->next;
            
        temp->next = (node *)malloc(sizeof(node));
        scanf("%d",&(temp->next->n));
        temp->next->next = NULL;

    }

}
int min_list(node *l) {
    
    int min;
    node *temp = l;

    min = temp -> n;
    while(temp != NULL) {
        if(min > temp->n)
            min = temp->n;
        temp = temp->next; 
    }
    return min;
}
void Free (node* l) {

    node* temp;

    while(l != NULL) {
        temp = l;
        l = l->next;
        free(temp);
    }
}
/*
node *reverse_list(node *L) {

    node *rev,*temp;
    while(L != NULL) {
        rev = L;
        
    }
    return rev;
}
*/
int main() {

    node* L,*rev;
    int n,min;

    L = (node *)malloc(sizeof(node));

    scanf("%d",&n);

    make_list(L,n);

    min = min_list(L);
    printf("Minimum number is: %d",min);

/*
    rev = reverse_list(L);

    while(rev != NULL) {
        printf("%d \n",rev-> n);
        rev = rev->next;
    }
*/
    Free(L);
    return 0;
}