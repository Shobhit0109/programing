#include <stdio.h>

int main() {

    float a, b , c; 

    printf("\n\t Enter number a and b to find the Quotient a/b : ") ;
    scanf("%f%f", &a , &b );

    if (b == 0)
        printf("\n\t DIVISION BY 0 DETECTED, NOT POSSIBLE");
    else {
        c = a/b;
        printf("\n\t The quotient %f/%f is %f",a,b,c);
    }

    return 0;
}

