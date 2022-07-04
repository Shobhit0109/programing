//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
using namespace std;

#define f(i,n) for (int i = 0; i < (n); i++)
#define i(i,j,n) ((i)*(n) + (j))
#define endl ("\n")

int main(int argc,const char **argv) {

//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(0);/

//    #ifndef ONLINE_JUDGE

//        freopen("/home/shobhit/Documents/programing/All codes Execution files/Input Output/input.txt", "r", stdin);
//        freopen("/home/shobhit/Documents/programing/All codes Execution files/Input Output/output.txt", "w", stdout);

//    #endif

    cout << "\n\tYour file name :" << argv[0];
    if (argc > 1) cout << "\n\tYou have arguments also!!";
    else cout << "\n\tYou have no arguments!!";
    
    
    
 return 0;
}

//to run the executable file in gnome-terminal use : gnome-terminal -- bash -c './new-cpp;read line'
//for tilix : tilix -e 'command'