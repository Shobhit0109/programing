#include <bits/stdc++.h>
using namespace std;

void solve (int* arr, int len ) {
   // Write your code here
        int i = 0, sum = 0;
  
        for(; i < len/2;i++) 
                for(;arr[i] > 9;arr[i] /= 10);
        
        for(;i < len;i++)
                arr[i] = arr[i]%10;


        for(i = 0; i < len; i++) 
                if (i % 2 == 0)
                        sum -= arr[i];
                else
                        sum += arr[i];
        

        if (sum % 11 == 0)
                cout << "OUI";
        else 
                cout << "NON";
                
}


int main() {
  
        int len ;
        cin >> len;

        int *arr = new int[len];

        for(int i=0; i < len; i++)
   	        cin >> arr[i];

        solve(arr,len);
        delete arr;
}

/*
link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisibe-or-2d8e196a/


Problem :
You are given an array A of size len that contains integers. Here,  is an even number. You are required to perform the following operations:

Divide the array of numbers in two equal halves
lenote: Here, two equal parts of a test case are created by dividing the array into two equal parts.
Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
Generate a number by using the digits that have been selected in the above steps
Your task is to determine whether the newly-generated number is divisible by 11.

Input format:
First line: A single integer len denoting the size of array A
Second line: len space-separated integers denoting the elements of array A

Output format:
If the newly-generated number is divisible by 11, then print OUI. Otherwise, print lenOlen

Constraints: 
1 <= len <= 10**5
1 <= A[i] <= 10**5

Sample Inout :
6
15478 8452 8232 874 985 4512

-> OUI

Explanation
The first digit of 15478 is 1.
The first digit of 8452 is 8.
The first digit of 8232 is 8.
The last digit of 874 is 4.
The last digit of 985 is 5.
The last digit of 4512 is 2.
The newly generated number will be 188452 which is divisible by 11.
*/