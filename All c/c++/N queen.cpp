#include <iostream>
using namespace std;

int main() {

    string str;

    while(true) {
        
        int *matrix; // Matrix of N-queen
        int i,j,k,n,totalCases;
        /*
        cout << "\033[2J\033[1;1H"; 
                    |
                    |
                    \/
        Clear screen command  
        don't use this it doesn't actually clean it it just prints previous results of output in current screen output mereko nhi pta pr yeh previous jo resulyys aaye n-queen ke bs unhe show krta hai baki jo bhi cout mali hai vo kuch nhi kr rha like jo bhi unimportant hai
        */
        system("clear"); //this works
        cout << "\n\tEnter size of Square Matrix:";
        cin >> n; //Enter not works no error occur manta nhi jb tk valid input na ho
        //we can use getline to get integer like in python 
        matrix = new int[n]; // in all 'j' columns it will store 'i' row value
        for (i = 0;i < n;i++) matrix[i] = 0;

        //Total square matrix formed by size n
        totalCases = n;
        for(i = n-1; i > 0; i-- )   totalCases *= n;

        for(i=0 ;i < totalCases;i++) { // For  All matrix's can be possible at 'n' size 

                // Check function
                int check = 1;
                for(j=0;j<n;j++) { // For row
                    for(k=1;k<j+1;k++)  // For column
                        if((matrix[j]== matrix[j-k]) ||(matrix[j]-k== matrix[j-k])||(matrix[j]+k== matrix[j-k])) {
                        // Condition for For same line      For upper diagonal dir.     For lower diagonal dir.
                            check = 0;
                            break;
                        }
                    if(check == 0) 
                    break;
                }
                // To print matrix which is N-queen will be print their         
                if( check == 1) { //To see its working replace check(matrix,n) with 1
                    cout << "\n\tA solution is:\n\n\t";
                    for (j=0;j < n;j++) { // For row
                        for (k=0; k < n;k++ ) //For column
                            if (j == matrix[k])
               
                 cout<<"|👸|";
                            else
                                cout<<"|__|";
                        cout << "\n\t";
                    }
                    cout << "\n\tThe positions are :\n\t";
                    for(j=0; j<n ; j++)
                        cout << '(' << matrix[j]+1 << ',' << j+1 << ") " ;
                    cout << endl;
                }

                //To make other marix 
                matrix[n-1] += 1;
                j = n-1;
                while(j>0) {
                    if(matrix[j] == n) {
                        matrix[j] = 0;
                        matrix[j-1] += 1;                       
                    }
                    j--;
                }          
        }
        delete matrix;  // Free the memory
        cout << "\n\tAbove Solutions are all solutions if you can't find any then "<< n << " size - square matrix doesn't have any solution";
        cout << "\n\tIf you want to continue then type anything (for exit hit any enter):";
        getline(cin,str); //bcz in first line "enter" or any that type of character is saved that just works without my input and automatically throws out of code by if statement 
        getline(cin,str); //iske through mai kuch input kr paunga
        // cin >> str; will not accept enter as input or an empty string is removed from input or comparing in c++ bcz str == '' creates an error
        if(!str.length()) //baki koi method kaam nhi aaya vo cin pr atk jata tha kyuki sirf enter doesn't works and one more thing i also try doing -> EOF ke equal rkh du aur ctrl+d ka use kru pr vo automatically agle looping pr chla jata tha
            break;
    }
    cout << "\n\tThank you come again";
    return 0;
}