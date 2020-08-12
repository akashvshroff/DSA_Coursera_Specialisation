from math import floor
import sys


def binary_search(A, k):
    """
    An extremely efficient searching technique in sorted arrays where the
    complexity is O(log n).
    """
    low, high = 0, len(A)-1
    while low <= high:
        mid = low + floor((high-low)/2)
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
