#include <stdio.h> 
#include <chrono> //Header file for time 
using namespace std::chrono;  //Refrence from :
// https://www.geeksforgeeks.org/measure-execution-time-function-cpp/
// Whole paragraph at end


int main(void) {

	//int choice;
	long int arr[] = {1,1,2}; //Just change it //query : {1,1,} this works how..?

	//printf("\n\t Which approach you want (1,2) :");
	//scanf("%d",&choice);

	//auto start = high_resolution_clock::now(); //Start to calculate time

	//printf("%d",choice);
	//if(choice == 1) 
	{ //Samrat approach 
		/*
		In this approach, the max value element of arr is taken 
		and then a new array with that max size is formed 
		now every small element is represented by the index like element - 1 = index 
		And then the printing occur
		its time is unpredictable
		At high values of max it depends on it
		*/
		printf("\nSamrat approach\n");

		auto start = high_resolution_clock::now(); //Start to calculate time

		size_t size = sizeof(arr)/sizeof(arr[0]) , k = 0 ;
	
		int f_size = arr[0]; //to calculate max num in arr that will b size of resultant array
		for(int i=0;i<size;i++) 
			if (f_size < arr[i])
				f_size = arr[i];

		int *f = new int[f_size]; // That resultant array 
		//used new bcz c++don't allow int f[max(arr,size)]
	
		for(k=0;k < size; k++) //Calculating the recurrence
			f[arr[k]-1] ++;
	
	
		for( k=0 ; k < f_size; k++) //Printing of result
			if (f[k] != 0)
				printf("\n\tNumber is %zu and its total recurrence is %d",k+1,f[k]);
		delete f;
		auto stop = high_resolution_clock::now();
		auto duration = duration_cast<microseconds>(stop - start);
	
		printf("\n\nTime taken is: %zu\n\n",duration.count());
	}
	//else if(choice == 2) 
	{ // My approach
		/*
			In this approoach , we find every unique element of arr 
			and for every unique value we calculate its refrence
			its time can be find by big O-notation
			referce python code is given below
		*/
		printf("\nShobhit approach\n");

		auto start = high_resolution_clock::now(); //Start to calculate time
	
		size_t size  = sizeof(arr)/sizeof(arr[0]) , i = 0 , j = 0 , k = 0 , num = 0;
    	int test[2*size] = {0}; //Result array of size 2*size at 2k == element at 2k+1 == its recurrence amount

    	for(i=0 ; i< size; i++) { //traversing in array
            j = -1;
            for(num = 0; num < k+1 ; num++)  //finding if it is prsent in array and if yes than at what position
                if (arr[i] == test[2*num]) { 
                    j = num;
                    break;
                }
                       
            if(j == -1) { //meaning element is unique
                
                test[2*k] = arr[i]; //entering the unique  element
                test[2*k + 1] = 1; //Entering  first recurrence
                k ++; //k reprsnt biggest index upto whih unique values are written
               
            }
            else  //if not uniqy=ue than increasing its recurrece value
                test[2*j + 1] ++;         
    	}
    	for( i=0 ; i < size ; i++) //printing
        	if (test[2*i+1] != 0)
		    	printf("\n\tNumber is %d and its total recurrence is %d",test[2*i],test[2*i+1]);

		auto stop = high_resolution_clock::now();
		auto duration = duration_cast<microseconds>(stop - start);
	
		printf("\n\nTime taken is: %zu\n\n",duration.count());

		//Referece Python code
	/* 
		try:
    		arr = input().split() #Input of array
		except:
			arr = [1,2,3,1]
    	test = set(arr) #converting to set
    	res = []
    
    	for i in test: #now for every unique element of arr == element of set we alculate its recurrence and store in anoother list
        	sum = 0
        	for j in arr:
            	if i == j:
                	sum += 1
        	result.append(sum)

    	for i in range(len(test)): #Printing
        	print(f"\tThe number is : {test[i]} and it's recurrence is : {res[i]}")
	*/
	}
	//else 
	//	printf("\n\tPlease only enter between (1,2)");

	//auto stop = high_resolution_clock::now();
	//auto duration = duration_cast<microseconds>(stop - start);
	
	//printf("\n\nTime taken is: %zu\n\n",duration.count());
	return 0;
}


/*

Measure execution time of a function in C++
Difficulty Level : Medium
Last Updated : 08 Sep, 2020
We can find out the time taken by different parts of a program by using the std::chrono library introduced in C++ 11. We have discussed at How to measure time taken by a program in C. The functions described there are supported in C++ too but they are C specific. For clean and robust C++ programs we should strive to use C++ specific language constructs only.

std::chrono has two distinct objects–timepoint and duration. A timepoint as the name suggests represents a point in time whereas a duration represents an interval or span of time. The C++ library allows us to subtract two timepoints to get the interval of time passed in between. Using provided methods we can also convert this duration to appropriate units.

The std::chrono provides us with three clocks with varying accuracy. The high_resolution_clock is the most accurate and hence it is used to measure execution time.

Step 1: Get the timepoint before the function is called

#include <chrono>
using namespace std::chrono;
  
// Use auto keyword to avoid typing long
// type definitions to get the timepoint
// at this instant use function now()
auto start = high_resolution_clock::now();
Step 2: Get the timepoint after the function is called

#include <chrono>
using namespace std::chrono;
  
// After function call
auto stop = high_resolution_clock::now();
Step 3: Get the difference in timepoints and cast it to required units

// Subtract stop and start timepoints and
// cast it to required unit. Predefined units
// are nanoseconds, microseconds, milliseconds,
// seconds, minutes, hours. Use duration_cast()
// function.
auto duration = duration_cast<microseconds>(stop - start);
  
// To get the value of duration use the count()
// member function on the duration object
cout << duration.count() << endl;

A complete C++ program demonstrating the procedure is given below. We fill up a vector with some random numbers and measure the time taken by sort() function to sort this vector.

// C++ program to find out execution time of
// of functions
#include <algorithm>
#include <chrono>
#include <iostream>
#include<vector>
using namespace std;
using namespace std::chrono;
  
// For demonstration purpose, we will fill up
// a vector with random integers and then sort
// them using sort function. We fill record
// and print the time required by sort function
int main()
{
  
    vector<int> values(10000);
  
    // Generate Random values
    auto f = []() -> int { return rand() % 10000; };
  
    // Fill up the vector
    generate(values.begin(), values.end(), f);
  
    // Get starting timepoint
    auto start = high_resolution_clock::now();
  
    // Call the function, here sort()
    sort(values.begin(), values.end());
  
    // Get ending timepoint
    auto stop = high_resolution_clock::now();
  
    // Get duration. Substart timepoints to 
    // get durarion. To cast it to proper unit
    // use duration cast method
    auto duration = duration_cast<microseconds>(stop - start);
  
    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;
  
    return 0;
}
Output: (Machine Dependent)

Time taken by function: 3062 microseconds
References
https://www.geeksforgeeks.org/chrono-in-c/

Want to learn from the best curated videos and practice problems, check out the C++ Foundation Course for Basic to Advanced C++ and C++ STL Course for foundation plus STL.  To complete your preparation from learning a language to DS Algo and many more,  please refer Complete Interview Preparation Course.

*/