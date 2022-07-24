#include <iostream>
#include <cstdio>
using namespace std;

#define f(i,a,n) for (int i = a; i < (n); i++)
#define i(i,j,n) ((i)*(n) + (j))
#define endl ("\n")

void printSubByRec(const int *a,const int n) {
    if (n == 1) {
        cout << *a << " ";
        return;
    }
    
}

int main(void) {

    // int size;
    // cout << "\n\tEnter the number of elements : ";
    // cin >> size;

    // int arr[size];
    // f(i,size) {
    //     cout << "\n\tEnter the element " << i+1 << " : ";
    //     cin >> arr[i];
    // }

    int size = 3,arr[3] = {15,20,12};
    printSubByRec(arr, size);

 return 0;
}
