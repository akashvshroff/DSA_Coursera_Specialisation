# python3


def left_child(i): return i*2+1


def right_child(i): return i*2+2


def sift_down(arr, i, size):
    """
    Bubbles down a value in the min-heap if its child is smaller than it. Swaps
    a parent node with the min of its child nodes and counts num swaps.
    """
    max_size = i
    l = left_child(i)
    r = right_child(i)
    if l <= size and arr[l][1] <= arr[max_size][1]:
        if arr[l][1] == arr[max_size][1]:
            if arr[l][0] < arr[max_size][0]:
                max_size = l
        else:
            max_size = l
    if r <= size and arr[r][1] <= arr[max_size][1]:
        if arr[r][1] == arr[max_size][1]:
            if arr[r][0] < arr[max_size][0]:
                max_size = r
        else:
            max_size = r

    if i != max_size:
        arr[i], arr[max_size] = arr[max_size], arr[i]
        sift_down(arr, max_size, size)


def change_priority(arr, i, p):
    arr[i][1] += p
    arr = sift_down(arr, i, len(arr)-1)


def assign_jobs(n_workers, jobs):
    min_heap = [[i, 0] for i in range(n_workers)]
    workers = []
    for job in jobs:
        # print(min_heap)
        workers.append(min_heap[0][::])
        curr_worker = min_heap[0]
        change_priority(min_heap, 0, job)
    return workers


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    assigments = assign_jobs(n_workers, jobs)
    for assigment in assigments:
        print('{} {}'.format(*assigment))


if __name__ == "__main__":
    main()
