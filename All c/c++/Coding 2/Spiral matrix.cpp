#include <iostream>
#include <cstdio>
using namespace std;

#define f(i,n) for (int i = 0; i < (n); i++)
#define i(i,j,n) ((i)*(n) + (j))
#define endl ("\n")

int main(void) {

    int n = 4;
    cout << "\n\tEnter the size of Matrix : ";
    cin >> n;

    int a[n*n] , k = 1 , u = 0, v = 0 , m = 0;

    f(i,n*n)
        a[i] = i+1;

    cout << "\n\tThe Matrix is : \n";
    f(i,n) {
        cout << "\n\t";
        f(j,n) {
            if (a[i(i,j,n)] < 10)
                cout << " ";
            cout << a[i(i,j,n)] << " ";
        }
    }

    cout << "\n\n\tSpiral Matrix :\t";

    f(i,n*n) {

        cout << a[i(u,v,n)] << " ";
        a[i(u,v,n)] = i+1;

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

        if (u == m && v == n-m-1)
            k = 2;
        else if (u == n-m-1 && v == n-m-1)
            k = 3;
        else if (u == n-m-1 && v == m) {
            k = 4;
            m ++;
        }
        else if (u == m && v == m-1)
            k = 1;
    }


    cout << "\n\tThe Matrix is : \n";
    f(i,n) {
        cout << "\n\t";
        f(j,n) {
            if (a[i(i,j,n)] < 10)
                cout << " ";
            cout << a[i(i,j,n)] << " ";
        }
    }
    
 return 0;
}