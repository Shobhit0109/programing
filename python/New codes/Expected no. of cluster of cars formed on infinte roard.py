"""
Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
Examples : 
 

Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9 
 2  5  8 
 1  4  7 
The given matrix is rotated by 90 degree 
in anti-clockwise direction.
Input:
 1  2  3  4 
 5  6  7  8 
 9 10 11 12 
13 14 15 16 
Output:
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13
The given matrix is rotated by 90 degree 
in anti-clockwise direction.

 


An approach that requires extra space is already discussed here.
Approach: To solve the question without any extra space, rotate the array in form of squares, dividing the matrix into squares or cycles. For example, 
A 4 X 4 matrix will have 2 cycles. The first cycle is formed by its 1st row, last column, last row and 1st column. The second cycle is formed by 2nd row, second-last column, second-last row and 2nd column. The idea is for each square cycle, swap the elements involved with the corresponding cell in the matrix in anti-clockwise direction i.e. from top to left, left to bottom, bottom to right and from right to top one at a time using nothing but a temporary variable to achieve this.
Demonstration: 
 

First Cycle (Involves Red Elements)
 1  2  3 4 
 5  6  7 8 
 9 10 11 12 
 13 14 15 16 
Moving first group of four elements (First
elements of 1st row, last row, 1st column 
and last column) of first cycle in counter
clockwise. 
 4  2  3 16
 5  6  7 8 
 9 10 11 12 
 1 14  15 13 
 Moving next group of four elements of 
first cycle in counter clockwise 
 4  8  3 16 
 5  6  7  15  
 2  10 11 12 
 1  14  9 13 
Moving final group of four elements of 
first cycle in counter clockwise 
 4  8 12 16 
 3  6  7 15 
 2 10 11 14 
 1  5  9 13 
Second Cycle (Involves Blue Elements)
 4  8 12 16 
 3  6 7  15 
 2  10 11 14 
 1  5  9 13 
Fixing second cycle
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13

Algorithm: 
 

There is N/2 squares or cycles in a matrix of side N. Process a square one at a time. Run a loop to traverse the matrix a cycle at a time, i.e loop from 0 to N/2 - 1, loop counter is i
Consider elements in group of 4 in current square, rotate the 4 elements at a time. So the number of such groups in a cycle is N - 2*i.
So run a loop in each cycle from x to N - x - 1, loop counter is y
The elements in the current group is (x, y), (y, N-1-x), (N-1-x, N-1-y), (N-1-y, x), now rotate the these 4 elements, i.e (x, y) <- (y, N-1-x), (y, N-1-x)<- (N-1-x, N-1-y), (N-1-x, N-1-y)<- (N-1-y, x), (N-1-y, x)<- (x, y)
Print the matrix.

 

 Code
<?php 
// PHP program to rotate a 
// matrix by 90 degrees
$N = 4;
// An Inplace function to 
// rotate a N x N matrix
// by 90 degrees in 
// anti-clockwise direction
function rotateMatrix(&$mat)
{
    global $N;
     // Consider all 
    // squares one by one
    for ($x = 0; $x < $N / 2; $x++)
    {
        // Consider elements 
        // in group of 4 in 
        // current square
        for ($y = $x; 
             $y < $N - $x - 1; $y++)
        {
            // store current cell
            // in temp variable
            $temp = $mat[$x][$y];
            // move values from
            // right to top
            $mat[$x][$y] = $mat[$y][$N - 1 - $x];
            // move values from
            // bottom to right
            $mat[$y][$N - 1 - $x] = 
                $mat[$N - 1 - $x][$N - 1 - $y];
            // move values from 
            // left to bottom
            $mat[$N - 1 - $x][$N - 1 - $y] = 
                         $mat[$N - 1 - $y][$x];
            // assign temp to left
            $mat[$N - 1 - $y][$x] = $temp;
        }
    }
}
// Function to 
// print the matrix
function displayMatrix(&$mat)
{
    global $N;
    for ($i = 0; $i < $N; $i++)
    {
        for ($j = 0; $j < $N; $j++)
            echo $mat[$i][$j] . " ";
        echo "
";
    }
    echo "
";
}
// Driver code
// Test Case 1
$mat =  array(array(1, 2, 3, 4),
              array(5, 6, 7, 8),
              array(9, 10, 11, 12),
              array(13, 14, 15, 16));
// Tese Case 2
/* $mat = array(array(1, 2, 3),
                array(4, 5, 6),
                array(7, 8, 9));
*/
// Tese Case 3
/*$mat = array(array(1, 2),
               array(4, 5));*/
// displayMatrix($mat);
rotateMatrix($mat);
// Print rotated matrix
displayMatrix($mat);
// This code is contributed 
// by ChitraNayal
?>
Output : 
 

 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13 

Complexity Analysis: 
 

Time Complexity: O(n*n), where n is side of array. 
A single traversal of the matrix is needed.
Space Complexity: O(1). 
As a constant space is needed
Please refer complete article on Inplace rotate square matrix by 90 degrees | Set 1 for more details!

Today at 08:11
Given an array speed[] of size N denoting the speed of N cars moving on an infinitely long single lane road (i.e. no overtaking is allowed) from left to right. Initially, the rightmost car is at the first position and whenever a car with higher speed reaches a car with lower speed they start moving with the speed to the slower car and form a cluster. The task is to find the total number of clusters that will form.

Note: A single car is also considered a cluster.

Examples:

Input: speed[] = {1, 4, 5, 2, 17, 4 }
Output: 3
Explanation: After a certain time, car with speed 17 will reach car with speed 4(car5) and will form a cluster. 
And similarly, cars with speed 4 and 5 will start moving with speed 2 on reaching car3.
The clusters will be (car0), (car1, car2, car3), (car4, car5).

Input: speed[] = {2, 3, 4, 7, 7}
Output: 5
Explanation: Each car will form a cluster.

 
Approach: The solution is based on greedy approach. Here, a car with less speed forms a cluster with all the cars behind it and having speeds greater than itself. Follow the steps below to solve the problem:

Start iterating from the last index of array speed[].
Store the speed of the car in a variable, say currentCar.
A cluster is formed till the speed of cars behind the currentCar is greater than itself. Therefore increase the value of clusters as soon as a car with less speed is found behind it or when the array is out of bounds.
Below is the implementation of the above approach.

 Code
// C++ code to implement above approach
#include <bits/stdc++.h>
#include <vector>
using namespace std;
// Function to count total number of clusters
int countClusters(vector<int>& speed)
{
    int N = speed.size();
     // For number of clusters
    int cluster = 0;
    for (int i = N - 1; i >= 0; i--) {
        int currentCar = speed[i];
         // comparing with previous car
        while (i != 0 and speed[i - 1] 
               > currentCar) {
            i--;
        }
        cluster++;
    }
    return cluster;
}
// Driver code
int main()
{
    vector<int> speed = { 1, 4, 5, 2, 17, 4 };
    int clusters = countClusters(speed);
    cout << clusters;
    return 0;
} Code
// Java program to implement
// the above approach
class GFG
{
  // Function to count total number of clusters
  static int countClusters(int []speed)
  {
    int N = speed.length;
    // For number of clusters
    int cluster = 0;
    for (int i = N - 1; i >= 0; i--) {
      int currentCar = speed[i];
      // comparing with previous car
      while (i != 0 && speed[i - 1] 
             > currentCar) {
        i--;
      }
      cluster++;
    }
    return cluster;
  }
  // Driver Code
  public static void main(String args[])
  {
    int []speed = { 1, 4, 5, 2, 17, 4 };
    int clusters = countClusters(speed);
    System.out.println(clusters);
  }
}
// This code is contributed by Saurabh Jaiswal Code
# Python code to implement above approach
# Function to count total number of clusters
def countClusters(speed):
    N = len(speed)
    clusters = 0
    i = N-1
    while(i >= 0):
        currentCar = speed[i]
        while(i != 0 and speed[i-1] > currentCar):
            i = i-1
        clusters = clusters+1
        i = i-1
    return clusters
# Driver code
if __name__ == '__main__':
    speed = [1, 4, 5, 2, 17, 4]
    clusters = countClusters(speed)
    print(clusters) Code
// C# program to implement
// the above approach
using System;
class GFG
{
  // Function to count total number of clusters
  static int countClusters(int []speed)
  {
    int N = speed.Length;
    // For number of clusters
    int cluster = 0;
    for (int i = N - 1; i >= 0; i--) {
      int currentCar = speed[i];
      // comparing with previous car
      while (i != 0 && speed[i - 1] 
             > currentCar) {
        i--;
      }
      cluster++;
    }
    return cluster;
  }
  // Driver Code
  public static void Main()
  {
    int []speed = { 1, 4, 5, 2, 17, 4 };
    int clusters = countClusters(speed);
    Console.Write(clusters);
  }
}
// This code is contributed by Samim Hossain Mondal. Code
 <script>
        // JavaScript code for the above approach 
        // Function to count total number of clusters
        function countClusters(speed) {
            let N = speed.length;
            // For number of clusters
            let cluster = 0;
            for (let i = N - 1; i >= 0; i--) {
                let currentCar = speed[i];
                // comparing with previous car
                while (i != 0 && speed[i - 1]
                    > currentCar) {
                    i--;
                }
                cluster++;
            }
            return cluster;
        }
        // Driver code
        let speed = [1, 4, 5, 2, 17, 4];
        let clusters = countClusters(speed);
        document.write(clusters);
  // This code is contributed by Potta Lokesh
    </script>
 
 


Output
3

 

Time Complexity: O(N)
Auxiliary Space: O(1)
"""
from os import system 
system('clear') #To clear output screen

try:    #taking input of speeds in single line
    speed = [int(i) for i in input("\n\tEnter values of speed in single line:").split()]
    if speed == []:
        raise ValueError()
except:
    print("\n\tYou write wrong input , therefore deafault values {1,4,5,2,17,4} is taken")
    speed = [1,4,5,2,17,4]
finally:
    cluster = 0 # Output variable
    i = 0
    
speed = speed[::-1] #Reversing the array bcz cars starts from right
size = len(speed)

while i < size: #It run to calculate every cluster
    num = speed[i]
    i += 1
    """
    the algo is:
        like after reversing the array it will start from first element and the inner loop will try to find a no. smaller than that initial no. and in b/w them are clusters 
        eg .
            in 1 4 5 2 17 4
            first 4 to 17
            then 2 to 4
            then only 1
    """
    while i < size and num < speed[i]: #it willl calculate and skip every i for that cluster
        i += 1
    cluster += 1
    
print(f"\n\tTotal clusters formed are:{cluster}")  #Printing the result