# python3


def left_child(i): return 2*i


def right_child(i): return 2*i+1


def sift_down(arr, i, size):
    """
    Bubbles down a value in the min-heap if its child is smaller than it. Swaps
    a parent node with the min of its child nodes and counts num swaps.
    """
    swaps = []
    max_size = None
    while True:
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
        else:
            break
    return swaps


def build_heap(data):
    """
    Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data)-1
    for i in range(n//2, 0, -1):
        swaps.extend(sift_down(data, i, n))


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
