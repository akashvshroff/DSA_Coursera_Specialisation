# python3


def left_child(i): return i*2+1


def right_child(i): return i*2+2


def sift_down(arr, i, size):
    """
    Bubbles down a value in the min-heap if its child is smaller than it. Swaps
    a parent node with the min of its child nodes.
    """
    min_size = i
    l = left_child(i)
    r = right_child(i)
    if l <= size:
        l_priority = arr[l][1]
        cur_priority = arr[min_size][1]
        if l_priority < cur_priority:
            min_size = l
        elif l_priority == cur_priority:
            if arr[l][0] < arr[min_size][0]:
                min_size = l
    if r <= size:
        r_priority = arr[r][1]
        cur_priority = arr[min_size][1]
        if r_priority < cur_priority:
            min_size = r
        elif r_priority == cur_priority:  # same priority
            if arr[r][0] < arr[min_size][0]:  # lower index
                min_size = r
    if i != min_size:
        arr[i], arr[min_size] = arr[min_size], arr[i]
        sift_down(arr, min_size, size)


def change_priority(arr, i, p):
    """
    Adds the time taken for a job and bubbles the node down.
    """
    arr[i][1] += p
    arr = sift_down(arr, i, len(arr)-1)


def assign_jobs(n_workers, jobs):
    """
    Program that simulates parallel processing in a program. Given a list of
    jobs where the ith index represents the time taken for the ith job.
    A min heap is used to make the program run at O(n) and the heap stores the
    worker id(index number) and next free time. At each stage the worker with
    the minimum next free time is chosen and if 2 workers are free
    the one with the lower index is given priority as the workers get the jobs
    chronologically. Workers are from 0 to n-1 where n is the number of workers.
    Output the worker chosen and time job started for each job.
    """
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
