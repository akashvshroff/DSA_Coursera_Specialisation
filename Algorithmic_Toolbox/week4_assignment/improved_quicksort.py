# Uses python3
import sys


def quick_sort(A, l, r):
    """
    An alternate, more efficient approach to quick sort where the array is
    modified in place.
    """
    if l < r:
        m1, m2 = partition(A, l, r)
        quick_sort(A, l, m1-1)
        quick_sort(A, m2+1, r)


def partition(a, l, r):
    """
    Partitions the array into 2 after choosing a pivot and sorting. Returns 2
    index positions that mark the start and the end of the region with the pivot
    thereby accounting for non-unique integers.
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


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
