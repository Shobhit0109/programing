#include <iostream>
#include <stdio.h>
using namespace std;

int main () {

    int a = 5;
    cout << a++ << a++ << ++a << endl;

    a = 5;
    printf("%d%d%d",a++,a++,++a);

    return 0;
}