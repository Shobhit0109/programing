#include <stdio.h>

#define f(i,n) for (int i = 0; i < n; i++)
#define i(i,j,n) ((i)*(n) + (j))
#define endl ("\n")

int main(int argc,const char **argv) {

//    #ifndef ONLINE_JUDGE

//        freopen("/home/shobhit/Documents/programing/All codes Execution files/Input Output/input.txt", "r", stdin);
//        freopen("/home/shobhit/Documents/programing/All codes Execution files/Input Output/output.txt", "w", stdout);

//    #endif

    printf ("\n\tYour file name : %s" , argv[0] );
    if (argc > 1) printf ("\n\tYou have arguments also!!");
    else printf ("\n\tYou have no arguments!!");

    

    

 return 0;
}

//to run the executable file in gnome-terminal use : gnome-terminal -- bash -c './new-c;read line'