# python3


def left_child(i): return 2*i+1


def right_child(i): return 2*i+2


def sift_down(arr, i, size, swaps=[]):
    """
    Bubbles down a value in the min-heap if its child is smaller than it. Swaps
    a parent node with the min of its child nodes and counts num swaps.
    """
    max_size = i
    l = left_child(i)
    r = right_child(i)
    if l <= size and arr[l] < arr[max_size]:
        max_size = l
    if r <= size and arr[r] < arr[max_size]:
        max_size = r
    if i != max_size:
        swaps.append([i, max_size])
        arr[i], arr[max_size] = arr[max_size], arr[i]
        sift_down(arr, max_size, size, swaps)
    return swaps


def build_heap(data):
    """
    Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data)-1
    for i in range(n//2, -1, -1):
        # print(i)
        swaps.extend(sift_down(data, i, n, []))
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # print(data)


if __name__ == "__main__":
    main()
