# Uses python3
import sys


def get_majority_element(a):
    """
    Uses a divide and conquer approach to find the majority element (occurs more
    than n/2 times where n = len(array)) in an array of elements in O(n log n)
    time. It is based on the idea that if there exists a majority element in
    the array, it must be the majority element in either or both
    halves of the array.
    """
    if not a:
        return -1
    if len(a) == 1:
        return a[0]
    mid = len(a)//2
    left_elem = get_majority_element(a[:mid])
    right_elem = get_majority_element(a[mid:])
    if left_elem == right_elem:
        return left_elem
    if a.count(left_elem) > mid:
        return left_elem
    elif a.count(right_elem) > mid:
        return right_elem
    return -1


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
