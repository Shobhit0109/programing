#include <stdio.h>  
#include <iostream>
using namespace std;

int main(){  
   FILE *fp;  
  
   fp = fopen("myfile.txt","w+");  
   
    cout << (long long int)fp << endl;
    cout << ftell(fp) << "\t1" << endl;
    
   fputs("This is javatpoint", fp);  
   
   cout << (long long int)fp << endl;
   cout << ftell(fp) << "\t1" << endl;
    
   fseek( fp, 7, SEEK_SET );  
   
    cout << (long long int)fp << endl;
    cout << ftell(fp) << "\t1" << endl;
    
   fputs("sonoo jaiswal", fp);  
   
    cout << (long long int)fp << endl;
    cout << ftell(fp) << "\t1" << endl;
   fclose(fp); 
   
   return 0; 
}  