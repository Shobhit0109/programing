#include <iostream>
#include <stdio.h>

int main(int argc, char *argv[])
{
	float a=1.1;
	
	if (a==1.1f) printf("1");
	
	float b=0;
	
	if (b==0) printf("1");
	
	if (b==0.0) printf("1");
	
	printf("%lf",1.1);
	return 0;
}