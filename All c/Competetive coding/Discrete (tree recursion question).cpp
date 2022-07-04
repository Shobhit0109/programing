//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
using namespace std;

#define f(i,n) for (int i = 0; i < (n); i++)
#define i(i,j,n) ((i)*(n) + (j))
#define endl ("\n")

void makePattern(int num) {

    if (num == 0) 
        return;
    
    makePattern(num - 1);
    cout << num ;
    makePattern(num - 1);

    //in its dry run explained by discrete sir - every makepattern is a tree like system so in this function every nodehas 3  branches and each branch has a node and so on and so forth
    // like in 121 - 
    //      2
    //     /|\
    //    1   1
    //    |   |

    // and so on and so forth
    // 121 3 121

    // so this prblm solved by recursion bcz every case can be divided into sub cases and so on and so forth
    // like
    //     3
    //    /|\
    //   2   2
    //  /|\ /|\
    // 1  1 1  1
    // |  | |  |

    // so this is a tree like system

    // middle bar shows printing now downmost mai left to write print hoga for every branch
    // so for this case 1->2->1 -> 3 -> 1->2->1 
}
int main(void)/*(int argc,char **argv)*/ {

    int num = 4;

    /**
     * @brief @Question
     * Making  pattern like that :
     *      121
     *     1213121
     * 12131214213121
     * 
     */
    while(num) {

        cout << "\n\t" << num << " :\t";
        makePattern(num--);
    }
    
 return 0;
}