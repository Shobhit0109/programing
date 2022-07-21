# include <iostream>
using namespace std;

extern int i;

int main(void) {
    // void a; //can't make variable void
 //cout << i;
    int u=5,v=u; //how the hell this or int a[10] , *ptr = a; works
    cout << v << endl;
    void *a;
    a = new int[10];
    // cout << *a; //creates an error --- ‘void*’ is not a pointer-to-object type
    cout << a; //this works so i thought void can store addres but treats them as void type so they can't return value
    int *n;
    n= new int[10];
    cout << n;
    // delete a; //deleting ‘void*’ is undefined [-Wdelete-incomplete]
    delete n;
    n = (int *)a;
    delete n;

    unsigned int c;
    c = -1;
    printf("\n%u",c); //if value exceeds then it works like a circle
    // but
    printf("\n%d",c); //it will give -1 again
    return 0;
}
