# python3
from collections import deque


def max_sliding_window(n, arr, k):
    """
    O(n) solution to the maximum sliding window problem that seeks to find the
    largest element in all contiguous subarrays of lenght k. Method uses dequeue
    and therefore O(k) extra space.
    """
    q = deque()
    for i in range(k):
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)

    for i in range(k, n):
        print(str(arr[q[0]]) + ' ', end='')
        while q and q[0] <= i - k:
            q.popleft()
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    print(str(arr[q[0]]))


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    max_sliding_window(n, input_sequence, window_size)
