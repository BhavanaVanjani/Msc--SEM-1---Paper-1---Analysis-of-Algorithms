#   To heapify subtree rooted at index i
#   n is size of heap
def heapify(arr,n,i):
    largest = i # Initialize largest as root.
    l = 2 * i + 1 #left = 2 * i + 1
    r = 2 * i  + 2 #right = 2 * i  + 2

    #See if left child of root exists and is greater than root.
    if l < n and arr[i] < arr[l] :
        largest = l
    #See if right child of root exists and is greater than root.
    if r < n and arr[largest] < arr[r]:
        largest = r

    #change root if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] #swap
        # Heapify the root.
        heapify(arr,n,largest)
#The main function to sort an array of given size.
def heapSort(arr):
    n = len(arr)

    #build a maxheap
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    #one by one extract elements.
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i] #swap.
        heapify(arr,i,0)
#Driver Code to test above
arr = [12,11,13,5,6,7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" %arr[i]),
    
Output:
Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/bhavana vanjani/AppData/Local/Programs/Python/Python39/Msc CS Pracs/heapsort.py
Sorted array is
5
6
7
11
12
13
>>> 
    
    
