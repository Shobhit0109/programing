#include <iostream>
#include <math.h>
using namespace std;

int main() {

    int *a , *b;

    a = new int [10000000];
    b = new int [10000000];

    printf("%d \n%d",a,b);
    
    delete a;
    delete b;

    return 0;
}