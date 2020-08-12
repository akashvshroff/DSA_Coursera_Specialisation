# Uses python3
import sys


def merge_sort(A, inversions=0):
    """
    Implementation of the O(n log n) sorting algorithm which recursively splits
    the input array A into smaller and smaller sub-problems and then solves
    those finally building up to the main solution.
    """
    if len(A) == 1:  # base case
        return A
    m = len(A) // 2
    B = merge_sort(A[:m], inversions)
    C = merge_sort(A[m:], inversions)
    A_sorted, x = merge(B, C)
    inversions += x
    return A_sorted, inversions


def merge(B, C):
    """
    Merges the two arrays by choosing the min element at a time and counts the
    number of inversions. An inversion in an array A[1...n] is a pair of numbers
    at indices i,j where i < j but A[i] > A[j].
    """
    n = 0
    D = []
    b, c = len(B), len(C)
    i, j = 0, 0
    while i < b and j < c:
        if B[i] <= C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            n += b - i  # all remaining elements in array B since all are larger.

    D += B[i:]
    D += C[j:]

    return D, n


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a, num_inversions = merge_sort(a)
    print(num_inversions)
