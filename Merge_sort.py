# Program for implementation of MergeSort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    else:
        # Finding the midpoint of the array
        mid = len(arr)//2

        # Left half of the array elements
        left = arr[:mid]

        # Right half of the array elements
        right = arr[mid:]

        # Sorting the left half elements
        left = merge_sort(left)

        # Sorting the right half elements
        right = merge_sort(right)

        # Merging the two sorted halves
        return merge_two_sorted_lists(left,right,arr)
    

def merge_two_sorted_lists(a,b,arr):
    # Finding the length of two sub-arrays
    len_a = len(a)
    len_b = len(b)
    # Initializing the index of the sub-arrays
    i = j = k = 0
    # Merging the two sub-arrays
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1
    return arr

arr = [4,3,1,2,5,8,9,0]
print(merge_sort(arr))