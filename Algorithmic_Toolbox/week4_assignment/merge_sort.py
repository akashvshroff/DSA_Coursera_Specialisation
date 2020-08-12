def merge_sort(A):
    """
    Implementation of the O(n log n) sorting algorithm which recursively splits
    the input array A into smaller and smaller sub-problems and then solves
    those finally building up to the main solution.
    """
    if len(A) == 1:  # base case
        return A
    m = len(A) // 2
    B = merge_sort(A[:m])
    C = merge_sort(A[m:])
    A_sorted = merge(B, C)
    return A_sorted


def merge(B, C):
    """
    Given two sorted arrays B,C, this function creates a resultant array by
    choosing (and appending) the smallest element in either array (smallest is
    at position 0) until one of the arrays is empty and then it appends all the
    remaining elements, returning the resultant array. Serves as a helper to the
    merge_sort algorithm.
    """
    D = []
    while B and C:
        b, c = B[0], C[0]
        if b <= c:
            D.append(b)
            B.pop(0)
        else:
            D.append(c)
            C.pop(0)
    D += B if B else C
    return D


nums = [23, 41, 32, 43, 1, 2, 34, 323, 4, 3, 5, 7, 86, 5, 4]
print(merge_sort(nums))
