from random import randrange
def partition(x,pivot_index = 0):
    i=0
    if pivot_index !=0: x[0],x[pivot_index]= x[pivot_index],x[0]
    for j in range(len(x)-1):
        if x[j+1] < x[0]:
            x[j+1],x[i+1] = x[i+1],x[j+1]
            i += 1
    x[0],x[i] = x[i],x[0]
    return x,i
def RSelect(x,k):
    if len(x) == 1:
        return x[0]
    else:
        xpart = partition(x,randrange(len(x)))
        x = xpart[0] #partitioned array.
        j = xpart[1] #pivot index.
        if j == k:
            return x[j]
        elif j>k:
            return RSelect(x[:j],k)
        else:
            k = k-j-1
            return RSelect(x[(j+1):],k)

x = [3,1,8,4,7,9]
for i in range(len(x)):
    print (RSelect(x,i))
    
Output:
Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python39/Bhavna Msc CS Part 1/Algorithms/randomized_sel.py
1
3
4
7
8
9
