#include<iostream>
using namespace std;

void print(int *a){
    int i;
    for(i=0;i<9;i++)
        cout << a[i] << ' ';
    cout << endl;
    return;
}
int main(){
    int a[9];
    unsigned i,j;

    for (i=0; i<9;i++) //defining array
        a[i]=i;
    print(a);

    for( i=0;i<9/2 ;i++){ //main code for reversing
        j = a[i];
        a[i] = a[8-i];
        a[8-i]=j;
    }
    print(a);

    //system("pause");
    return 0;
}
