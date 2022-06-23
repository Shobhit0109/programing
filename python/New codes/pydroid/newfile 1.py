# Function to find all n–digit binary numbers having
# more 1's than 0's at any position
def find(n, s='', zeros=0, ones=0):
 
    # continue only if the total number of ones is more than equal
    # to the number of zeroes
    if ones < zeros:
        return
 
    # if the number becomes n–digit, print it
    if n == 0:
        print(s)
        return
 
    # append 1 to the result and recur with one less digit
    find(n - 1, s + '1', zeros, ones + 1)
 
    # append 0 to the result and recur with one less digit
    find(n - 1, s + '0', zeros + 1, ones)
 
 
if __name__ == '__main__':
 
    # given the total number of digits
    n = 1
 
    find(n)