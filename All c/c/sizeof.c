#include <stdio.h>
#include <stdlib.h>

int main() {

    int a[9],*b;
    printf("\n\t %ld and pointer %ld",sizeof(a),sizeof(b));

    b = (int*)malloc(9*sizeof(int));
    printf("\n\t %ld and pointer %ld",sizeof(a),sizeof(b));
    free(b);

    printf("\n\t array address - %p and pointer address - %p",&a,&b);

    printf("\n\t array element address - %p and pointer elelment address - %p",a,b);

//    free(b);
    
    return 0;
}