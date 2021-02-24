# Write a program for found a subset with given sum.
# A recursive solution for subset sum
# problem.
# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(set,n,sum) : 
    
    # Base Cases 
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        return False
   
    # If last element is greater than 
    # sum, then ignore it 
    if (set[n - 1] > sum) : 
        return isSubsetSum(set, n - 1, sum); 
   
    # else, check if sum can be obtained 
    # by any of the following 
    # (a) including the last element 
    # (b) excluding the last element    
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1]) 
      
      
# Driver program to test above function 
set = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(set) 
if (isSubsetSum(set, n, sum) == True) : 
    print("Found a subset with given sum") 
else : 
    print("No subset with given sum")
    
Output:
Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\bhavana vanjani\Documents\Msc CS Part1  Pracs\Algorithm -paper 1\P8_SubsetWithAGivenSum.py
Found a subset with given sum
