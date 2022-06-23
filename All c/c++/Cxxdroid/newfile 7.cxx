#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[])
{
	int *p = new int[10];
	p[0]=1;
	delete p;
	cout << p[0];
	return 0;
}