#include <stdio.h>

int main() {

    int num , rsh , lsh;

    printf("\n\tEnter number : ");
    scanf("%d", &num);

    rsh = num >> 1;
    lsh = num << 1;

    printf("\n\tThe number %d after right shift by 1 is %d",num,rsh);

    printf("\n\tThe number %d after left shift by 1 is %d",num,lsh);

    return 0;
}