#include <stdio.h>

int main() {

    int a,b;

    do {
        scanf("%d %d",&a,&b);
        printf("\n\t1\n");
        fflush(stdin);

    }while(a==b);

    return 0;
}