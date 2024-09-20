
def find_duplicates(arr):
    """
    Function to find duplicates in an array O(1) memmort complexity
    """
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr): 
            if arr[i] == arr[j]:
                print(arr[i], end=" ")  
                arr.pop(j)  
            else:
                j += 1
        i += 1

arr = [1, 3, 4, 2, 2]
find_duplicates(arr)
