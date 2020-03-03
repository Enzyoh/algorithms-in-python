def merge(arr, helper, low, middle, high):
    # copy both halves into the helper array
    for i in range(low, high + 1):
        helper[i] = arr[i]
    
    helperLeft = low
    helperRight = middle + 1
    current = low

    # Go through helper array. Compare left and right half, copying back the smaller element
    # from the two halves into the original array
    while helperLeft <= middle and helperRight <= high:
        if helper[helperLeft] <= helper[helperRight]:
            arr[current] = helper[helperLeft]
            helperLeft += 1
        else:
            arr[current] = helper[helperRight]
            helperRight += 1
        current+=1
    # copy over elements from the left side of the arr, elements on the right are already in the main array
    remaining = middle - helperLeft
    for i in range(0, remaining + 1):
        arr[current + i] = helper[helperLeft + i]

def merge_sort(arr, helper, low, high):
    if(low < high):
        middle = (low + high)//2
        merge_sort(arr, helper, low, middle) # sort left half 
        merge_sort(arr, helper, middle + 1, high) # sort right half
        merge(arr, helper, low, middle, high) # merge them

def merge_sort_arr(arr):
    helper = arr.copy()
    merge_sort(arr, helper, 0, len(arr) - 1)

arr = input().split(',')
merge_sort_arr(arr)
print(arr)