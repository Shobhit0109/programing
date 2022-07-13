#include <iostream>
#include <cstdio>
using namespace std;

#define f(i,n) for (int i = 0; i < (n); i++)
#define i(i,j,n) ((i)*(n) + (j))
#define endl ("\n")

int main(void) {

    int n = 4;
    cout << "\n\tEnter the size of Matrix : ";
    //cin >> n;

    int a[n*n] , k = 1 , u = 0, v = 0;

    f(i,n*n)
        a[i] = i+1;

    cout << "\n\tThe Matrix is : \n";
    f(i,n) {
        cout << "\n\t";
        f(j,n)
            cout << a[i(i,j,n)] << " ";
    }

    cout << "\n\n\tSpiral Matrix :\n";

    f(i,3*n) {

        //cout << a[i(u,v,n)] << " ";
        cout << u << " " << v << " " << n-i/n-1 << " " << i << " " << a[i(u,v,n)] << "\n";

        switch (k) {
            case 1:
                v++;
                break;
            case 2:
                u++;
                break;
            case 3:
                v--;
                break;
            case 4:
                u--;
                break;
        }

        if (u == i/n && v == n-i/n-1)
            k = 2;
        else if (u == n-i/n-1 && v == n-i/n-1)
            k = 3;
        else if (u == n-i/n-1 && v == i/n)
            k = 4;
        else if (u == i/n + 1 && v == i/n)
            k = 1;

    }
 return 0;
}