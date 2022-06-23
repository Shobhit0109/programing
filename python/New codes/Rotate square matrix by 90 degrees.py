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
 5  6  67  8 
 9 10 11 12 
13 14 15 16 
Output:
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13
The given matrix is rotated by 90 degree 
in anti-clockwise direction.

[i][j] [m][n]
[i*n+j]        [m*n]
 


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
"""
from os import system
system('clear')

def Print(matrix,size): #Function for printing 
    for i in range(size):
        print(end="\n\t") #For next line
        for j in range(size):
            print(matrix[i*size+j],end=' ')


try: #For input error handling
    #I use 1d array as 2d so to use i,j in 2d for 1s i need this function
    degree = int(input("\n\tEnter Degree in multiple of 90:"))
    if degree % 90 != 0:
        raise EOFError() #So that defaukt values will be taken
    
    size = int(input("\n\tEnter size of Square Matrix:"))
    print("\n\tEnter the elements along row wise like ( row*size + j = element no.)")
    matrix = [int(input(f"\n\tEnter {i+1} element :")) for i in range(size*size)]
    
except:
    print("\n\tError in input default size of 3 and matrix is taken and degree 90 is taken")
    degree = 90
    size = 3
    matrix = [i+1 for i in range(size*size)] 
    
finally:
    result = [] #Resultant matrix
    print("\n\tYour matrix is:") #Printing the given Matrix
    Print(matrix,size)

while degree >= 360: #Because in circle angles will repeat after 360
    degree -= 360
if degree == 0: #If degree is multiple of 360
    result = matrix
    
while(degree != 0): #Rotate by 90 degrees until Degree will be zero
    
    degree -= 90
    result = []
    j = 0
    
    while j < size: # this algo works like for every column  we will loop  row in reverse order and store elements in a new 2d emulated 1d matrix but at first element like 
        """
        eg:
            1 2 3         3 6 9
            4 5 6  -->>   2 5 8
            7 8 9         1 4 7
            
        emulated in 1d 
            1 2 3 4 5 6 7 8 9   to 3 6 9 2 5 8 1 4 7
            
            you can see element at column first and row last is at first position in reverse order and after that all element in same order are in that thing   
        """
        for i in range(size-1,-1,-1):
            result.insert(0,matrix[i*size + j])
            
        j += 1
        
    matrix = result[:]
    

print("\n\tYour rotated matrix is:")
Print(result,size)

# Question from geeks for geeks