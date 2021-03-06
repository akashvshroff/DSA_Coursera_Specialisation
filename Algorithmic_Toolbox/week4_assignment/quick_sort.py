def quick_sort(arr):
    """
    A less memory efficient version of quicksort where three lists 
    are made based on partition via a pivot and this process recursively continues.
    """
    less, same, more = [], [], []  # 3 partition lists
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                same.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + same + more


nums = [23, 41, 32, 43, 1, 2, 34, 323, 4, 3, 5, 7, 86, 5, 4, 4, 4, 2, 2, 2, 1, 1, 1, 3, 3, 3]
print(quick_sort(nums))
