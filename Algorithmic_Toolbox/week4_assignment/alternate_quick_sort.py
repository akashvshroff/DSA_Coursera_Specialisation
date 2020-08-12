def quick_sort_alternate(A, l, r):
    """
    An alternate, more efficient approach to quick sort where the array is
    modified in place.
    """
    if l < r:
        m1, m2 = partition(A, l, r)
        quick_sort_alternate(A, l, m1-1)
        quick_sort_alternate(A, m2+1, r)


def partition(a, l, r):
    """
    Partitions the array into 2 after choosing a pivot and sorting.
    """
    x, j1, t = a[l], l, r
    i = j1
    j2 = r

    while i <= r:  # forward pass
        if a[i] < x:
            a[j1], a[i] = a[i], a[j1]
            j1 += 1
        i += 1

    while t >= j1:
        if a[t] > x:
            a[j2], a[t] = a[t], a[j2]
            j2 -= 1
        t -= 1

    return j1, j2


nums = [23, 41, 32, 43, 1, 2, 34, 323, 4, 3, 5, 7, 86, 5, 4, 4, 4, 2, 2, 2, 1, 1, 1, 3, 3, 3]
quick_sort_alternate(nums, 0, len(nums)-1)
print(nums)
