#include <stdio.h> 
#include <iostream>
#include <cstring>
#include <unistd.h>
#include <stdlib.h>
#include <cmath>
using namespace std;

/*
enum hey {yo=-1,f=0};
*/
/*
union
*/

int main(int argc,char** argv) {
/*
    int i;
    int t = &i; //can be done but can't deassign int
*/
/*
    int a=2 , b=1,c=2;
    switch(a) {
        case b:
            printf("\n\tYou are in b");
            break;
        case c:
            printf("\n\tYou are in c");
        default:
            printf("\n\tYou are in default");
    }
*/
/*
    char a[] = "Hello";
    printf("%p\n",a);
    printf("%d\n",a);
    printf("%s\n",a);
*/
/*
    int a = 0;
    int p[5];
    printf("%p\n",p);
    printf("%d\n",p);
*/
/*
    int i,j;
    printf("%d %d\n",i);
    printf("%d\n",i,j);
*/

/*
    const char *x = new char[5];
    //*(x+3) = 50; //error
    //char *c = x+3; //error

    printf("\n\t%s %p",x,x);
    delete x;
    printf("\n\t%s %p",x,x); //same adddress after delete

    int y = 5;
    const int *p = &y;
    p = 0; //no error
    //*p = 6; //error 

    int * const q = &y;
    // q = 0; //error
    *q = 9; //no error that means 
    /*
        const int *p; is an const pointer of constant int
        while
        int *const p; is an const ptr of int
    * /
    // but these are same
    const int a = 0,b = 0;
    int const c = 0,b = 0;
*/

/*
    const int c = 0;
    int *x = &c; //error
*/
/*
    int x=9;
    const int * y=&x;
    x = 5;
    printf("%d %d",x,*y);
*/
/*
    const int * x; //const pointer to int // const int * == int const *
    int * const y; //pointer to const int 
*/
/*
    const int *p;
    int *q = p; //error
*/
/*
    int *p = new int[1];
    *p = 4;
    const int *q = p;
  //  *q = 3; error
    *p = 4;
    printf("%d",*p);
*/
/*
    int *ptr;
    void *pt = ptr; //can store but can't print values out of it means values not accessible values
*/
/*
    int x; // define x
    int y; // define y

   // ptr is a constant pointer to an integer that can be modified     
   // through ptr, but ptr always points to the same memory location
     int * const ptr = &x;                                               

     *ptr = 7; // allowed: *ptr is not const
     ptr = &y; // error: ptr is const; cannot assign new address
*/
/*
    int n;
    int *a = &n;
    //char *b = a; //error
    void *c = a; //only void can store address but can't accessible elements
    char *b = c; //that's how store int poiinter address in char pointer
    //every pointer has same bytes if  64-system than 64 and vice-versa for 32
  
    //int vgrh bs isliye taki +1 krne pr vo utna size ya bits cover kre
*/
/*
  int h;
  printf("hello\n");
  scanf("%d hello %d",&h,&h);
  printf("\n%d",h);
  scanf("%f hello");  it somehow takes input two times
  printf("yo ");

  int *a=0;
   scanf("%d",a);  //terminated by signal SIGSEGV (Address boundary error) ---- usually when try to access memory not accessible to you
    printf("%d",a);   //raise warning bcz pointer is given instead of int except we use
   printf("%p",(void*)a);  //output nil

   char c[30];
    scanf("%s",c);
    printf(c);
*/
/*
	unsigned int aCount = 0;
	unsigned int bCount = 0;
	unsigned int cCount = 0;
	unsigned int dCount = 0;
	unsigned int fCount = 0;
	
	puts("\n\tEnter the letter grades:");
	puts("\n\tEnter the EOF character to end input.");
	int grade; //one grade
	
	//loop until user types types end-of-file key sequence
	while ((grade = getchar()) != EOF) {
		
		// determine which grade was input
		switch (grade) { //switch nested in while
		
			case 'A': //grade was uppercase A
			case 'a': // or loweercase a 
				++aCount;
				break;
			case 'B': //grade was uppercase B
			case 'b': // or loweercase b
				++bCount;
				break;
			case 'C': //grade was uppercase C
			case 'c': // or loweercase c
				++cCount;
				break;
			case 'D': //grade was uppercase D
			case 'd': // or loweercase d
				++dCount;
				break;
			case 'F': //printf("%s","\n\tIncorrect letter grade entered.");
				puts("\n\tEnter a New grade."); //grade was uppercase F
			case 'f': // or lowercase f
				++fCount;
				break;
			default : // catch all othwr characters
				printf("%s","\n\tIncorrect letter grade entered.");
				puts("\n\tEnter a New grade.");
				break; // optional; will exit switch anyway
		}
	}//end while
	
	//output summary of results
	puts("\n\t Totals for each letter grade are:");
	printf("\n\tA: %u",aCount);
	printf("\n\tB: %u",bCount);
	printf("\n\tC: %u",cCount);
	printf("\n\tD: %u",dCount);
	printf("\n\tF: %u",fCount);
*/
/*
    char buffer[500];
    strcpy(buffer , argv[1]);
*/

/*
     int a,b,c;
     cin >> a >> b >> c; //5 8 8 and 5 enter 6 enter 8 both works
     cin >> a;
     cin >> b; // In them also works
     cin >> c;
     char a[10];
*/
/*
	for (int i = 0; i < 30; i++)
	{
		int j;
		system("clear");
		for (j = 0; j < i; j++)
			cout << " _";
		cout << "\n\t\t\thuy\n";
		for (j = 0; j < i; j++)
			cout << " _";
		cout << endl;
		sleep(0);
	}
*/
/*
    int i,j;
    i = (j = 9); // = returns value also
    cout << i << j;
*/

/*
    char buffer[500];
    //strcpy(buffer , argv[1]);
    for(int i = 2;i <= 70 ;i++)
        cout << argv[i] << '\n';
*/
    return 0;
}