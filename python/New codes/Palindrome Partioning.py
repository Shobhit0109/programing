choice = 1 #for first code just hange hoice to 1
if choice == 1: #print smallest partition and first one
    def allCases(pal,n):
        #this approach is like N-queen matrix making approach 
        All = [pal[:]] #stores all strings
        test = [0 for i in range(n)] 
        #our index holder which specifies where to put '|' from right or in front of which index like [1,2] become [1,'|',2] if test[0] = 1 
        # tax is storing location of every '|' 
        while test[0] < len(pal): #similar to N-queen bcz at end test[0] become equal to len(pal) 
            string = pal[:]
            test[-1] += 1   #inc value of last '|'
            for i in range(n-1,0,-1): #from right,if '|' inc become equal to len(pal)  then makes it 0 and inc last one by one
            #simlar to making all N-queen matrixes combination
            # like ['|','|','|',a,b,c,d] becomes ['|','|',a,'|',b,c,d] after +1 and so on 
                if test[i] > len(pal):
                    test[i-1] += 1
                    test[i] = 0

            for i in range(1,n): #removing strings with same position of '|' in test 
                if test[i] == test[i-1]:
                    break
            else:
                for i in test[::-1]: #for every '|' position making that required string
                    string.insert(i,'|')

                All.append(string) #inserting it
            #ofcourse , their are lots of useless string but they will cancel out in testing in fun create

        return All #returning all string combinations


    def create(pal,n): #our create function

        test = allCases(pal,n) #all string combinations that can be made using pl and n -> '|' 

        for i in test: #for every string combination it check if it's sub-strings are palindrome or not
            for j in ("".join(i)).split('|'): #j will be sub-string in every string
                if j != "" and j[::-1] != j: #checking sub-string is palindrome or not as it should be mirror of itself
                    # j!= "" bcz some '|' are together and they should be neglected
                    break #break loop if it is not
            else: #if all sub-strings are palindrome then this is our right ans 
                return i
        return ""


    if __name__=="__main__": #If this file is run then this main during import
        try:    #taking input
            pal = input("\n\tEnter Palindrome:")
            if pal == "":  #If no string is taken so to cal except
                raise ValueError
        except:
            print("\n\tWrong input their for default value - \"ababbbabbababa\" is taken")
            pal = "ababbbabbababa"

        test = list(pal)    #declare variable in which result is taken
        for i in range(1,len(pal)):
            test = create(list(pal),i) #calling fuction that can return the first palindrome it catches
            if test != "":
                break

        #Printing the palindrome
        print(f"\n\tThe palindrome division is :\t{''.join(test)} \n\tAnd number of divisions are : \t{len(test)-len(pal)}")

# link: https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

    """
Palindrome Partitioning | DP-17
Difficulty Level : Hard
Last Updated : 21 Jan, 2022
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”. Determine the fewest cuts needed for a palindrome partitioning of a given string. For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”. If a string is a palindrome, then minimum 0 cuts are needed. If a string of length n containing all different characters, then minimum n-1 cuts are needed. 

palindrome-partitioning

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
Examples :  

Input : str = “geek” 
Output : 2 
We need to make minimum 2 cuts, i.e., “g ee k”
Input : str = “aaaa” 
Output : 0 
The string is already a palindrome.
Input : str = “abcde” 
Output : 4
Input : str = “abbac” 
Output : 1 
 

This problem is a variation of Matrix Chain Multiplication problem. If the string is a palindrome, then we simply return 0. Else, like the Matrix Chain Multiplication problem, we try making cuts at all possible places, recursively calculate the cost for each cut and return the minimum value. 
Let the given string be str and minPalPartion() be the function that returns the fewest cuts needed for palindrome partitioning. following is the optimal substructure property.

Using Recursion 

// i is the starting index and j is the ending index. i must be passed as 0 and j as n-1
minPalPartion(str, i, j) = 0 if i == j. // When string is of length 1.
minPalPartion(str, i, j) = 0 if str[i..j] is palindrome.

// If none of the above conditions is true, then minPalPartion(str, i, j) can be 
// calculated recursively using the following formula.
minPalPartion(str, i, j) = Min { minPalPartion(str, i, k) + 1 +
                                 minPalPartion(str, k+1, j) } 
                           where k varies from i to j-1

// C++ Code for Palindrome Partitioning
// Problem
#include <bits/stdc++.h>
using namespace std;
 
bool isPalindrome(string String, int i, int j)
{
    while(i < j)
    {
      if(String[i] != String[j])
        return false; 
      i++;
      j--;
    }
    return true;
}
int minPalPartion(string String, int i, int j)
{
    if( i >= j || isPalindrome(String, i, j) )
      return 0;
    int ans = INT_MAX, count;
    for(int k = i; k < j; k++)
    {
      count = minPalPartion(String, i, k) +
        minPalPartion(String, k + 1, j) + 1;
  
      ans = min(ans, count);
    }
    return ans;
}
// Driver code
int main() {
    string str = "ababbbabbababa";
    cout << "Min cuts needed for " <<
      "Palindrome Partitioning is " << 
      minPalPartion(str, 0, str.length() - 1) << endl;
    return 0;
}
// This code is contributed by rag2127
Output: 

Min cuts needed for Palindrome Partitioning is 3 
Using Dynamic Programming :
Following is Dynamic Programming solution. It stores the solutions to subproblems in two arrays P[][] and C[][], and reuses the calculated values. 


// Dynamic Programming Solution for
// Palindrome Partitioning Problem
#include <bits/stdc++.h>
using namespace std;
 
// Returns the minimum number of cuts
// needed to partition a string
// such that every part is a palindrome
int minPalPartion(string str)
{
    // Get the length of the string
    int n = str.length();
 
    /* Create two arrays to build the solution
       in bottom up manner
    C[i][j] = Minimum number of cuts needed for
              palindrome partitioning
              of substring str[i..j]
    P[i][j] = true if substring str[i..j] is
              palindrome, else false
    Note that C[i][j] is 0 if P[i][j] is true */
    int C[n][n];
    bool P[n][n];
 
    // Every substring of length 1 is a palindrome
    for (int i = 0; i < n; i++) {
        P[i][i] = true;
        C[i][i] = 0;
    }
 
    /* L is substring length. Build the
    solution in bottom up manner by
    considering all substrings of
    length starting from 2 to n.
    The loop structure is same as Matrix
    Chain Multiplication problem
    ( See https:// www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/ )*/
    for (int L = 2; L <= n; L++) {
 
        // For substring of length L, set
        // different possible starting indexes
        for (int i = 0; i < n - L + 1; i++) {
            int j = i + L - 1; // Set ending index
 
            // If L is 2, then we just need to
            // compare two characters. Else
            // need to check two corner characters
            // and value of P[i+1][j-1]
            if (L == 2)
                P[i][j] = (str[i] == str[j]);
            else
                P[i][j] = (str[i] == str[j]) && P[i + 1][j - 1];
 
            // IF str[i..j] is palindrome, then C[i][j] is 0
            if (P[i][j] == true)
                C[i][j] = 0;
            else {
 
                // Make a cut at every possible
                // location starting from i to j,
                // and get the minimum cost cut.
                C[i][j] = INT_MAX;
                for (int k = i; k <= j - 1; k++)
                    C[i][j] = min(C[i][j], C[i][k] + C[k + 1][j] + 1);
            }
        }
    }
 
    // Return the min cut value for
    // complete string. i.e., str[0..n-1]
    return C[0][n - 1];
}
 
// Driver code
int main()
{
    string str = "ababbbabbababa";
    cout << "Min cuts needed for Palindrome"
            " Partitioning is "
         << minPalPartion(str);
    return 0;
}
 
// This code is contributed by rathbhupendra
Output: 

Min cuts needed for Palindrome Partitioning is 3 
Time Complexity: O(n3)

We can optimize the above code a bit further. Instead of calculating C[i] separately in O(n^2), we can do it with the P[i] itself. Below is the highly optimized code of this problem:


#include <bits/stdc++.h>
using namespace std;
 
int minCut(string a)
{
    int cut[a.length()];
    bool palindrome[a.length()][a.length()];
    memset(palindrome, false, sizeof(palindrome));
    for (int i = 0; i < a.length(); i++)
    {
        int minCut = i;
        for (int j = 0; j <= i; j++)
        {
            if (a[i] == a[j] && (i - j < 2 || palindrome[j + 1][i - 1]))
            {
                palindrome[j][i] = true;
                minCut = min(minCut, j == 0 ? 0 : (cut[j - 1] + 1));
            }
        }
        cut[i] = minCut;
    }
    return cut[a.length() - 1];
}
 
// Driver code
int main()
{
    cout << minCut("aab") << endl;
    cout << minCut("aabababaxx") << endl;
    return 0;
}
 
// This code is contributed by divyesh072019.
An optimization to above approach 
In the above approach, we can calculate the minimum cut while finding all palindromic substring. If we find all palindromic substring 1st and then we calculate minimum cut, time complexity will reduce to O(n2). 
Thanks for Vivek for suggesting this optimization. 


// Dynamic Programming Solution for Palindrome Partitioning Problem
#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
using namespace std;
 
// A utility function to get minimum of two integers
int min(int a, int b) { return (a < b) ? a : b; }
 
// Returns the minimum number of cuts needed to partition a string
// such that every part is a palindrome
int minPalPartion(char* str)
{
   
    // Get the length of the string
    int n = strlen(str);
 
    /* Create two arrays to build the solution in bottom-up manner
       C[i] = Minimum number of cuts needed for a palindrome partitioning
                 of substring str[0..i]
       P[i][j] = true if substring str[i..j] is palindrome, else false
       Note that C[i] is 0 if P[0][i] is true */
    int C[n];
    bool P[n][n];
 
    int i, j, k, L; // different looping variables
 
    // Every substring of length 1 is a palindrome
    for (i = 0; i < n; i++) {
        P[i][i] = true;
    }
 
    /* L is substring length. Build the solution in bottom up manner by
       considering all substrings of length starting from 2 to n. */
    for (L = 2; L <= n; L++) {
        // For substring of length L, set different possible starting indexes
        for (i = 0; i < n - L + 1; i++) {
            j = i + L - 1; // Set ending index
 
            // If L is 2, then we just need to compare two characters. Else
            // need to check two corner characters and value of P[i+1][j-1]
            if (L == 2)
                P[i][j] = (str[i] == str[j]);
            else
                P[i][j] = (str[i] == str[j]) && P[i + 1][j - 1];
        }
    }
 
    for (i = 0; i < n; i++) {
        if (P[0][i] == true)
            C[i] = 0;
        else {
            C[i] = INT_MAX;
            for (j = 0; j < i; j++) {
                if (P[j + 1][i] == true && 1 + C[j] < C[i])
                    C[i] = 1 + C[j];
            }
        }
    }
 
    // Return the min cut value for complete string. i.e., str[0..n-1]
    return C[n - 1];
}
 
// Driver program to test above function
int main()
{
    char str[] = "ababbbabbababa";
    cout <<"Min cuts needed for Palindrome Partitioning is " << minPalPartion(str);
    return 0;
}
 
// This code is contributed by shivanisinghss2110
Output: 

Min cuts needed for Palindrome Partitioning is 3 
Time Complexity: O(n2)

Using Memorization to solve this problem. 
The basic idea is to cache the intermittent results calculated in recursive functions. We can put these results into a hashmap/unordered_map. 
To calculate the keys for the Hashmap we will use the starting and end index of the string as the key i.e. [“start_index”.append(“end_index”)] would be the key for the Hashmap. 

Below is the implementation of above approach :  


// Using memoizatoin to solve the partition problem.
#include <bits/stdc++.h>
using namespace std;
// Function to check if input string is palindrome or not
bool is palindrome(string input, int start, int end)
{
    // Using two pointer technique to check palindrome
    while (start < end) {
        if (input[start] != input[end])
            return false;
        start++;
        end--;
    }
    return true;
}
 
// Function to find keys for the Hashmap
string convert(int a, int b)
{
    return to_string(a) + "" + to_string(b);
}
 
// Returns the minimum number of cuts needed to partition a string
// such that every part is a palindrome
int minpalparti_memo(string input, int i, int j, unordered_map<string, int>& memo)
{
    if (i > j)
        return 0;
    // Key for the Input String
    string ij = convert(i, j);
 
    // If the no of partitions for string "ij" is already calculated
    // then return the calculated value using the Hashmap
    if (memo.find(ij) != memo.end()) {
        return memo[ij];
    }
    // Every String of length 1 is a palindrome
    if (i == j) {
        memo[ij] = 0;
        return 0;
    }
    if (ispalindrome(input, i, j)) {
        memo[ij] = 0;
        return 0;
    }
    int minimum = INT_MAX;
    // Make a cut at every possible location starting from i to j
    for (int k = i; k < j; k++) {
        int left_min = INT_MAX;
        int right_min = INT_MAX;
        string left = convert(i, k);
        string right = convert(k + 1, j);
 
        // If left cut is found already
        if (memo.find(left) != memo.end()) {
            left_min = memo[left];
        }
        // If right cut is found already
        if (memo.find(right) != memo.end()) {
            right_min = memo[right];
        }
 
        // Recursively calculating for left and right strings
        if (left_min == INT_MAX)
            left_min = minpalparti_memo(input, i, k, memo);
        if (right_min == INT_MAX)
            right_min = minpalparti_memo(input, k + 1, j, memo);
 
        // Taking minimum of all k possible cuts
        minimum = min(minimum, left_min + 1 + right_min);
    }
 
    memo[ij] = minimum;
    // Return the min cut value for complete string.
    return memo[ij];
}
int main()
{
    string input = "ababbbabbababa";
    unordered_map<string, int> memo;
    cout << minpalparti_memo(input, 0, input.length() - 1, memo) << endl;
    return 0;
}
Time Complexity: O(n2)
 
    """
else: #print all cases
    def allCases(pal,n):
        #this approach is like N-queen matrix making approach 
        All = [pal[:]] #stores all strings
        test = [0 for i in range(n)] 
        #our index holder which specifies where to put '|' from right or in front of which index like [1,2] become [1,'|',2] if test[0] = 1 
        # tax is storing location of every '|' 
        while test[0] < len(pal): #similar to N-queen bcz at end test[0] become equal to len(pal) 
            string = pal[:]
            test[-1] += 1   #inc value of last '|'
            for i in range(n-1,0,-1): #from right,if '|' inc become equal to len(pal)  then makes it 0 and inc last one by one
            #simlar to making all N-queen matrixes combination
            # like ['|','|','|',a,b,c,d] becomes ['|','|',a,'|',b,c,d] after +1 and so on 
                if test[i] > len(pal):
                    test[i-1] += 1
                    test[i] = 0

            for i in range(1,n): #removinng strings with same position of '|' in test 
                if test[i] == test[i-1]:
                    break
            else:
                for i in test[::-1]: #for every '|' position making that required string
                    string.insert(i,'|')

                All.append(string) #inserting it
            #ofcourse , their are lots of useless string but they will cancel out in testing in fun create


        return All #returning all string combinations


    def create(pal,n): #our create function

        test = allCases(pal,n) #all string combinations that can be made using pl and n -> '|' 
        result = []
        for i in test: #for every string combination it check if it's sub-strings are palindrome or not
            for j in ("".join(i)).split('|'): #j will be sub-string in every string
                if j != "" and j[::-1] != j: #checking sub-string is palindrome or not as it should be mirror of itself
                    # j!= "" bcz some '|' are together and they should be neglected
                    break #break loop if it is not
            else: #if all sub-strings are palindrome then this is our right ans 
                result.append(''.join(i))
        return result


    if __name__=="__main__": #If this file is run then this main during import
        try:    #taking input
            pal = input("\n\tEnter Palindrome:")
            if pal == "":  #If no string is taken so to cal except
                raise ValueError
        except:
            print("\n\tWrong input their for default value - \"ababbbabbababa\" is taken")
            pal = "ababbbabbababa"

        test = list(pal)    #declare variable in which result is taken
        for i in range(1,len(pal)):
            test = create(list(pal),i) #calling fuction that can return the first palindrome it catches
            if len(test) > 0:
                break

        #Printing the palindromes
        print("\n\tAll palindrome partitons are :")
        [print(f"\t Solution {i} \tAnd number of divisions are: {len(i)-len(pal)}") for i in test]

# link :https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
"""

// C++ program to print all palindromic partitions of a given string
#include<bits/stdc++.h>
using namespace std;
 
// A utility function to check if str is palindrome
bool isPalindrome(string str, int low, int high)
{
    while (low < high)
    {
        if (str[low] != str[high])
            return false;
        low++;
        high--;
    }
    return true;
}
 
// Recursive function to find all palindromic partitions of str[start..n-1]
// allPart --> A vector of vector of strings. Every vector inside it stores
//             a partition
// currPart --> A vector of strings to store current partition
void allPalPartUtil(vector<vector<string> >&allPart, vector<string> &currPart,
                   int start, int n, string str)
{
    // If 'start' has reached len
    if (start >= n)
    {
        allPart.push_back(currPart);
        return;
    }
 
    // Pick all possible ending points for substrings
    for (int i=start; i<n; i++)
    {
        // If substring str[start..i] is palindrome
        if (isPalindrome(str, start, i))
        {
            // Add the substring to result
            currPart.push_back(str.substr(start, i-start+1));
 
            // Recur for remaining remaining substring
            allPalPartUtil(allPart, currPart, i+1, n, str);
             
            // Remove substring str[start..i] from current
            // partition
            currPart.pop_back();
        }
    }
}
 
// Function to print all possible palindromic partitions of
// str. It mainly creates vectors and calls allPalPartUtil()
void allPalPartitions(string str)
{
    int n = str.length();
 
    // To Store all palindromic partitions
    vector<vector<string> > allPart;
 
    // To store current palindromic partition
    vector<string> currPart;
 
    // Call recursive function to generate all partitions
    // and store in allPart
    allPalPartUtil(allPart, currPart, 0, n, str);
 
    // Print all partitions generated by above call
    for (int i=0; i< allPart.size(); i++ )
    {
        for (int j=0; j<allPart[i].size(); j++)
            cout << allPart[i][j] << " ";
        cout << "\n";
    }
}
 
// Driver program
int main()
{
    string str = "nitin";
    allPalPartitions(str);
    return 0;
}
Output
n i t i n 
n iti n 
nitin 
Output: 
 

n i t i n
n iti n
nitin
Approach 2: Expand around every palindrome

The idea is to split the string into all palindromes of length 1 that is convert the string to a list of its characters (but as string data type) and then expand the smaller palindromes to bigger palindromes by checking if its left and right (reversed) are equal or not if they are equal then merge them and solve for new list recursively. Also if two adjacent strings of this list are equal (when one of them is reversed), merging them would also give a palindrome so merge them and solve recursively.


class GFG:
    def solve(self, arr):
        self.res.add(tuple(arr)) # add current partitioning to result
        if len(arr)<=1:  # Base case when there is nothing to merge
            return
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i][::-1]: # When two adjacent such that one is reverse of another
                brr = arr[:i-1] + [arr[i-1]+arr[i]] + arr[i+1:]
                self.solve(brr)
            if i+1<len(arr) and arr[i-1]==arr[i+1][::-1]:  # All are individually palindrome,
              # when one left and one right of i are reverse of each other then we can merge
              # the three of them to form a new partitioning way
                brr = arr[:i-1] + [arr[i-1]+arr[i]+arr[i+1]] + arr[i+2:]
                self.solve(brr)
    def getGray(self, S):
        self.res = set()  # result is a set of tuples to avoid same partition multiple times
        self.solve(list(S)) # Call recursive function to solve for S
        return sorted(list(self.res))
# Driver Code
if __name__ == '__main__':
    ob = GFG()
    allPart = ob.getGray("geeks")
    for i in range(len(allPart)):
        for j in range(len(allPart[i])):
            print(allPart[i][j], end = " ")
        print()
# This code is contributed by Gautam Wadhwani
Output
g e e k s 
g ee k s 
This article is contributed by Ekta Goel. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.

"""
