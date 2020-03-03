def swap(arr, left, right):
    temp = arr[right]
    arr[right] = arr[left]
    arr[left] = temp

def partition(arr, left, right):
    pivot = arr[(left + right)//2] # pick pivot point
    while left <= right:
        # find an element on the left that should be on the right
        while(arr[left] < pivot):
            left+=1
        while arr[right] > pivot:
            right-=1
        if left <= right:
            swap(arr, left, right)
            left+=1
            right-=1
    return left

def quick_sort(arr, left, right):
    index = partition(arr, left, right)

    if left < index - 1: #sort left half
        quick_sort(arr, index, index - 1)
    if index < right: #sort right half
        quick_sort(arr, index, right)
    return arr

def quick_sort_arr(arr):
    return quick_sort(arr, 0, len(arr) - 1)

print(quick_sort_arr(input("Enter comma list of numbers to sort: ").split(',')))