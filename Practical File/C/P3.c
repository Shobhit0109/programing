#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    int n1, n2;

    srand(time(0));

    n2 = rand() % 100 + 1;

    printf("\n\tEnter number between 1 to 100: ");
    scanf("%d", &n1);

    printf((n1 == n2)?"\n\tCorrect":"\n\tWrong as the value of n2 is %d",n2);


    return 0;
}