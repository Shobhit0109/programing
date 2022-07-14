#include <bits/stdc++.h>
using namespace std;

int main() {

    FILE *file ;

    file = fopen("first file.txt","a+");

    if (file == NULL)
        printf("File not oppened");
    else {
        while (ftell(file) < 100) {

            cout << endl << ftell(file);
            fprintf(file,"\n\thello");
            fputs("\n\thello",file);
            cout << endl << ftell(file);
        }

        fclose(file);
    }
    cout << endl << __func__ ;
    cout << endl; 

    return 0;
}