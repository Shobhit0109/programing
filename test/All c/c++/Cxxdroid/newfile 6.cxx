
#include <stdio.h>
void TOH(int,char,char,char);

int main()
{
    int num;
    printf("Enter no of discs:");
    scanf("%d",&num);
    TOH(num,'A','B','C');

    return 0;
}
void TOH(int x,char s,char aux,char d)
{
   if (x==1)
   {
       printf("In if block*********\n");
       printf("Move disc %d from %c to %c\n",x,s,d);
       return;
   }
   printf("Out of if block*****\n");
   TOH(x-1,s,d,aux);
   printf("Move disc %d from %c to %c\n",x,s,d);
   TOH(x-1,aux,s,d);
}