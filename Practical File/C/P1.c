#include <stdio.h>

int main() {

    int num1 , num2 ;

    printf("\n\tEnter First Number: ");
    scanf("%d", &num1);

    printf("\n\tEnter Second Number: ");
    scanf("%d", &num2);

    printf("\n\tThe result of XOR operator is : %d", num1 ^ num2);

    return 0;
}