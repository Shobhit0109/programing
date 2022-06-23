#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[]) {
 	int ptr[2];
 	int *p = ptr+1;
 	cout << p-ptr;
 		return 0;
}