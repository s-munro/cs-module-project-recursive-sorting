# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start = None, end = None):
    # Your code here
    if start is None:
        start = 0
    if end is None:
        end = len(arr)

    if start > end:
        print("sorry get out of here")
        return -1


    middle = (start + end) // 2
    if arr[middle] == target:
        return middle
        
    elif arr[middle] < target: # arr less than target, so move right
        return binary_search(arr, target, middle + 1, end)
    
    else: # middle is greater than target, so move left
        return binary_search(arr, target, 0, middle - 1)

        


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target, start = None, end = None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr)
    
    if start > end:
        print("no way jose")
        return -1
    
    middle = (start + end) // 2
    if arr[middle] == target:
        return middle
    
    elif arr[middle] < target:
        return binary_search(arr, target, middle + 1, end)
    
    else:
        if
    # Your code here

